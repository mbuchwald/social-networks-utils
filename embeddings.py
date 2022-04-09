from math import log, e, ceil
import numpy as np
import random
from numpy import linalg as LA

DIFFERENT_WALKS = { # incluye bucles
    2: 2,
    3: 5,
    4: 15,
    5: 52,
    6: 203,
    7: 877,
    8: 4140,
    9: 21147,
    10: 115975,
    11: 678570,
    12: 4213597
}


def ln(num):
    return log(num, e)


def _cant_annonymous_walks(length, error=0.1, delta=0.01):
    nu = DIFFERENT_WALKS[length]
    return ceil((ln(2**nu - 2) - ln(delta)) * (2 / (error**2)))


def _camino_a_clave(camino):
    return "-".join(map(lambda v: str(v), camino))


def _annon_enum_rec(pasos_restantes, mapeo, camino=[], vs_en_camino=0, admite_bucles=False):
    if pasos_restantes == 0:
        mapeo[_camino_a_clave(camino)] = len(mapeo)
        return
    nuevo = vs_en_camino + 1
    ultimo = camino[-1] if len(camino) > 0 else None
    for i in range(1, nuevo + 1):
        if i == ultimo and not admite_bucles:
            continue
        camino.append(i)
        vs_en_este_camino = vs_en_camino + (1 if i == nuevo else 0)
        _annon_enum_rec(pasos_restantes - 1, mapeo, camino, vs_en_este_camino)
        camino.pop()


def _enumerar_anonymous_walks(length):
    mapeo = {}
    _annon_enum_rec(length, mapeo)
    return mapeo


def _random_walk(grafo, length):
    v = random.choice(list(grafo.nodes))
    camino = [v]
    while len(camino) < length:
        v = random.choice(list(grafo.neighbors(v)))
        camino.append(v)
    return camino


def _anonymize_walk(camino):
    translate = {}
    camino_trans = []
    for v in camino:
        if v not in translate:
            translate[v] = len(translate) + 1
        camino_trans.append(translate[v])
    return camino_trans


def anoymous_walks(grafo, length):
    '''
    :param grafo: Grafo a calcularle el embedding por anonymous_walk
    :param length:
    :return:
    '''
    cantidad = _cant_annonymous_walks(length)
    mapeo = _enumerar_anonymous_walks(length)
    contadores = [0] * len(mapeo)
    for i in range(cantidad):
        camino = _random_walk(grafo, length)
        contadores[mapeo[_camino_a_clave(_anonymize_walk(camino))]] += 1

    vector = np.array(contadores)
    return list(mapeo.keys()), vector / LA.norm(vector)


if __name__ == "__main__":
    print(_enumerar_anonymous_walks(7))
