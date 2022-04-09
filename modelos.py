import networkx as nx
import random


def erdos_renyi(cant, k):
    valores = list(range(cant))
    g = nx.Graph()
    g.add_nodes_from(valores)
    p = k / (cant - 1)
    for v in range(cant):
        for w in range(v + 1, cant):
            if v == w: continue
            if random.uniform(0, 1) < p:
                g.add_edge(v, w)
    return g


def elegir_preferntial(grafo, banned):
    grados_entrada = [0] * len(grafo)
    total = 0
    for v in range(len(grafo)):
        for w in grafo.neighbors(v):
            if w in banned:
                continue
            grados_entrada[w] += 1
            total += 1
    if total == 0:
        return None

    aleat = random.uniform(0, total)
    sumando = 0
    for i in range(len(grafo)):
        sumando += grados_entrada[i]
        if sumando > aleat:
            return i


def preferential_attachment(dirigido, alfa, cant, k):
    p = 1 - (1/(alfa - 1))
    valores = list(range(cant))
    g = nx.DiGraph() if dirigido else nx.Graph()
    g.add_nodes_from(valores)
    for v in range(cant):
        banned = set([v])
        for i in range(int(k)):
            preferential = random.uniform(0, 1) < p
            ya_agregado = False
            if preferential and v > 0:
                w = elegir_preferntial(g, banned)
                if w is not None:
                    banned.add(w)
                    g.add_edge(v, w)
                    ya_agregado = False
            if not ya_agregado:
                w = random.choice(list(set(range(cant)) - set([v])))
                g.add_edge(v, w)

    return g


def configuration_model(distribucion_grados, n=None):
    if n is None:
        n = sum(distribucion_grados)
    g = nx.Graph()
    g.add_nodes_from(range(n))
    num_v = 0
    spokes = []
    for grado in range(len(distribucion_grados)):
        cant_con_grado = distribucion_grados[grado]
        for i in range(cant_con_grado):
            for j in range(grado):
                spokes.append(num_v)
            num_v += 1

    uniones = []
    while len(spokes) >= 2:
        v = random.choice(spokes)
        spokes.remove(v)
        w = random.choice(spokes)
        spokes.remove(w)
        uniones.append((v, w))

    for v, w in uniones:
        if v == w:
            continue
        g.add_edge(v, w)

    return g


