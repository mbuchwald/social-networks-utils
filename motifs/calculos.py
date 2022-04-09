import multiprocessing as mp
import itertools
from numpy import linalg as LA
from os import cpu_count
import metricas
import numpy as np
import logger
import time
from motifs.load import *
import networkx as nx

CORES = cpu_count()

LOG = logger.Logger(logger.LogLevel.INFO)


def sub_grafo(grafo, vertices):
    if nx.is_directed(grafo):
        g = nx.DiGraph()
    else:
        g = nx.Graph()
    g.add_nodes_from(vertices)
    for v in vertices:
        for w in vertices:
            if grafo.has_edge(v, w):
                g.add_edge(v, w)
    return g


def extension(grafo, w, v_ext_org, v_sub):
    new_ext = set(v_ext_org)
    # primero agrego todos
    for x in grafo.neighbors(w):
        for v in v_sub:
            if not grafo.has_edge(v, x):
                new_ext.add(x)

    # ahora saco todos los menores, que no se llegan gracias a mi
    for x in v_ext_org:
        if x <= w and x in new_ext:
            new_ext.remove(x)

    return new_ext


def _esu(grafo, v, k, v_sub, v_ext, q):
    if len(v_sub) == k:
        q.put(sub_grafo(grafo, v_sub))
        return

    for w in v_ext:
        if w in v_sub:
            continue
        v_ext_mod = extension(grafo, w, v_ext, v_sub) - set([w]) - v_sub
        _esu(grafo, w, k, v_sub | set([w]), v_ext_mod, q)


def esperar_procesos(proc):
    for p in proc:
        p.join()
    proc.clear()


def esu(grafo, k, q):
    processes = []
    i = 0
    for v in grafo:
        v_ext = set((w for w in grafo.neighbors(v) if w > v))
        v_sub = set()
        v_sub.add(v)
        p = mp.Process(target=_esu, args=(grafo, v, k, v_sub, v_ext, q))
        p.start()
        processes.append(p)
        i += 1
        if len(processes) == CORES:
            esperar_procesos(processes)
            LOG.trace("Termine con " + str(i))

    esperar_procesos(processes)
    LOG.trace("Termine todos")


def son_isomorfos(g1, g2):
    if sum(map(lambda v: len(list(g1.neighbors(v))), g1)) != sum(map(lambda v: len(list(g2.neighbors(v))), g2)):
        return False, None

    trans_g2 = []
    g1_names = [n for n in g1]
    for permutation in itertools.permutations(list(range(len(g1)))):
        rename = {}
        for i in range(len(permutation)):
            rename[i + 1] = g1_names[permutation[i]]
        trans_g2.append(rename)

    for trans in trans_g2:
        es_isomorfo = True
        for i in range(1, len(g1) + 1):
            if set(g1.neighbors(trans[i])) != set(map(lambda v: trans[v], g2.neighbors(i))):
                es_isomorfo = False
        if es_isomorfo:
            return True, trans

    return False, None


def calcular_motif(grafo, motifs):
    for i in range(len(motifs)):
        isom, trans = son_isomorfos(grafo, motifs[i])
        if isom:
            return i, trans
    raise ValueError("Grafo: " + str(grafo) + " NO FUE ISOMORFO CON NINGUNO")


def consumir_motifs(q, result_queue, motifs):
    conteo = [0] * len(motifs)
    while True:
        subg = q.get()
        if len(subg) == 0:
            break
        idx_motif, _ = calcular_motif(subg, motifs)
        conteo[idx_motif] += 1
    result_queue.put(conteo)


def consumir_graphlets(g, q, n, result_queue, motifs):
    conteos = {v: np.zeros(n) for v in g}
    while True:
        subg = q.get()
        if len(subg) == 0:
            break
        idx, tx = calcular_motif(subg, motifs)
        for num in tx:
            conteos[tx[num]][motifs[idx].nodes[num]["type"]] += 1
    result_queue.put(conteos)


def contar_motifs(motifs, q, paralelismo):
    procesos = []
    results = mp.Queue()
    for i in range(paralelismo):
        p = mp.Process(target=consumir_motifs, args=(q, results, motifs))
        p.start()
        procesos.append(p)

    conteo_final = [0] * len(motifs)
    for p in procesos:
        p.join()
        parcial = results.get()
        for i in range(len(conteo_final)):
            conteo_final[i] += parcial[i]

    return conteo_final


def calcular_graphlets(g, motifs, q, n, paralelismo):
    procesos = []
    results = mp.Queue()
    for i in range(paralelismo):
        p = mp.Process(target=consumir_graphlets, args=(g, q, n, results, motifs))
        p.start()
        procesos.append(p)

    conteo_final = {v: np.zeros(n) for v in g}
    for p in procesos:
        p.join()
        parcial = results.get()
        for v in g:
            conteo_final[v] += parcial[v]

    return conteo_final


def aplicar_conteo_motifs(motifs, q, paralelismo, queue=None):
    resultados = contar_motifs(motifs, q, paralelismo)
    if queue is not None:
        queue.put(resultados)
    else:
        print(resultados)


def aplicar_conteo_graphlets(grafo, motifs, q, n, paralelismo, queue=None):
    resultados = calcular_graphlets(grafo, motifs, q, n, paralelismo)
    if queue is not None:
        queue.put(resultados)
    else:
        print(resultados)


def _elegir_motifs(grafo, n):
    return (MOTIF_DIR[n] if nx.is_directed(grafo) else MOTIF_NO_DIR[n])()


def calcular_motifs(grafo, n_motifs):
    """
    Algoritmo que calcula los motifs presentes dentro de grafo pasado por parámetro.
    Para optimizar, este procesamiento se paraleliza (con multiprocesamiento) con un modelo productor-consumidor:
    Se van calculando (en paralelo, con len(grafo) procesos) los subgrafos presentes con el algoritmo ESU, se
    envían estos subgrafos por una cola que luego unos consumidores irán consumiendo (también, en paralelo) para
    contar con los motifs.
    :param grafo:
    :param motifs: Los motifs a obtener. Tienen que corresponder todos a los motifs de misma cantidad de nodos
    y tienen que ser todos los motifs posibles.
    :param queue: Cola a la cual dejar los resultados. Si es null, simplemente se imprimirán los resultados
    """
    initial = 2 if nx.is_directed(grafo) else 3
    q = mp.Queue()
    r = mp.Queue()

    results = []
    for i in range(initial, n_motifs + 1):
        motifs = _elegir_motifs(grafo, i)
        k = len(motifs[0])
        p1 = mp.Process(target=esu, args=(grafo, k, q))
        p1.start()
        p2 = mp.Process(target=aplicar_conteo_motifs, args=(motifs, q, CORES, r))
        p2.start()
        p1.join()
        # ponemos grafo nulo para marcar fin
        for j in range(CORES):
            q.put(nx.Graph())
        p2.join()
        results += r.get()
    return np.array(results)


def significance_profile(N_real, N_rand_prom, N_rand_stds):
    """
    :param N_real: Cantidades de motifs encontrados en la red real
    :param N_rand_prom: promedio de motifs encontrados en red baseline simulada (varias veces)
    :param N_rand_stds: desviaciones standard de dichas cantidades simuladas
    :return: Significant profile (SP)
    """
    Z = (N_real - N_rand_prom) / (N_rand_stds + 0.001)
    norma = LA.norm(Z)
    SP = Z / norma
    return SP


def motif_grafo_eleatorios(generador_baseline, n_motifs, iters=100):
    """
    La funcion calcula baselines para luego hacer comparaciones de motifs
    :param generador_baseline: Una función sin parámetros (supplier) que devuelve un modelo
    aleatorizado (ver el módulo modelos.py)
    :param conjuntos_motifs: Conjuntos de motifs a calcular las metrias. Se debe reibir una
    lista de listas: [ [MOTIFS_2_VERTICES], [MOTIFS_3_VERTICES], ... ], dado que el calculo
    para cada motif se hace en funcion de la cantidad de nodos, como indica en #calcular_motifs_en_paralelo
    :param iters: cantidad de iteraciones a realizar
    :return: los promedios y desvios estándar de cada motif
    """
    conteos = []
    t = time.time()
    for i in range(iters):
        LOG.info("Iteracion {}".format(i + 1) + (("; anterior: {:.2f} segs".format(time.time() - t)) if i > 0 else ""))
        t = time.time()
        g = generador_baseline()
        LOG.debug("Grafo generado, vamos por motifs")
        conteos.append(calcular_motifs(g, n_motifs))
        LOG.debug(conteos[-1])

    valores = np.array(conteos)
    promedios = np.mean(valores, axis=0)
    stds = np.std(valores, axis=0)
    return promedios, stds


def graphlet_degree_vector(grafo, n):
    '''
    Por ahora solo funciona para no dirigido
    :param grafo:
    :param n:
    :return:
    '''
    max_graph = MOTIF_NO_DIR[n]()[-1]
    max_idx = max_graph[max(max_graph, key=lambda v:max_graph[v])]
    gdv = {v: np.zeros(max_idx + 1) for v in grafo}
    for v in grafo:
        gdv[v][0] = len(grafo.neighbors(v))

    paralellism = CORES // (1 if n == 3 else 2 if n == 4 else 8 if n == 5 else CORES)
    LOG.trace("paralellism: " + str(paralellism))
    for i in range(3, n+1):
        q = mp.Manager().Queue()
        result = mp.Queue()
        p1 = mp.Process(target=esu, args=(grafo, i, q))
        p1.start()
        motifs = MOTIF_NO_DIR[i]()
        p2 = mp.Process(target=aplicar_conteo_graphlets, args=(grafo, motifs, q, max_idx + 1, 1, result))
        p2.start()
        LOG.debug("Started, waiting to finish creating subgraphs")
        p1.join()
        LOG.debug("Finished creating subgraphs")
        # ponemos grafo nulo para marcar fin
        for i in range(CORES):
            q.put(nx.Graph())
        p2.join()
        LOG.debug("Finished to calculate, summing results")

        result = result.get()
        for v in grafo:
            gdv[v] += result[v]

    return gdv
