from math import log as ln, sqrt
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA
import random


def alfa_preferential_attachment(grafo, x_m):
    """
    Calcula por maxima verosimilitud el valor del exponente de la ley de potencias a la que corresponde un grafo.
    :param grafo:
    :param x_m: valor a partir del cual se empieza a cumplir la ley de potencias
    :return: alfa
    """
    sumatoria = 0
    for v in grafo:
        cant_ady = len(list(grafo.neighbors(v)))
        if cant_ady >= x_m:
            sumatoria += ln(cant_ady / x_m)
    return 1 + len(grafo) / sumatoria


def distribucion_grados(grafo):
    """
    :param grafo:
    :return: distribucion de los grados del grafo
    """
    max_k = 0
    for v in grafo:
        k_v = len(list(grafo.neighbors(v)))
        if k_v > max_k:
            max_k = k_v

    grados = [0] * (max_k + 1)
    for v in grafo:
        grados[len(list(grafo.neighbors(v)))] += 1
    return np.array(grados)


def grado_promedio(grafo):
    """
    :param grafo:
    :return: grado promedio (k) del grafo
    """
    total = 0
    for v in grafo:
        total += len(list(grafo.neighbors(v)))
    return total / len(grafo)


def distrubucion_ccdf(grafo):
    distribucion = distribucion_grados(grafo)
    total = sum(distribucion)
    ccdf = [total]
    for i in range(1, len(distribucion)):
        ccdf.append(ccdf[i - 1] - distribucion[i - 1])
    return np.array(ccdf) / total


def graficar_distribuciones(distribucion_grados):
    rango = np.arange(len(distribucion_grados))
    plt.plot(rango, distribucion_grados)

    # Para obtener el valor de alfa vistualmente
    x_m = 4
    alpha_prima = 1.7
    exponencial = list(map(lambda k: 5 * k ** (-alpha_prima), rango[x_m:]))
    plt.plot(rango[x_m:], exponencial)
    print("Alfa: ", alpha_prima + 1)

    plt.xlabel("Grado k")
    plt.ylabel("Nk (Pk * N)")
    plt.xscale("log")
    plt.yscale("log")
    plt.title("Distribucion de grados")
    plt.show()


def coeficiente_clustering(grafo, v):
    adyacentes = list(grafo.neighbors(v))
    if (len(adyacentes)) < 2:
        return 0
    aristas_cl = 0
    visitados = set()
    for u in adyacentes:
        for w in adyacentes:
            if u == w or w in visitados:
                continue
            if grafo.has_edge(u, w):
                # ida y vuelta
                aristas_cl += 2
        visitados.add(u)
    grado = len(adyacentes)
    return aristas_cl / ((grado - 1) * grado)


def clustering(grafo):
    """
    :param grafo:
    :return: el coeficiente de clustering discriminado por grado de vertice, y el coeficiente de clustering total
    """
    grados = distribucion_grados(grafo)
    clustering_total = 0
    clustering_por_grado = [0] * len(grados)
    for v in grafo:
        cl_v = coeficiente_clustering(grafo, v)
        clustering_total += cl_v
        grado = len(list(grafo.neighbors(v)))
        clustering_por_grado[grado] += cl_v / (grados[grado])
    clustering_total /= len(grafo)
    return clustering_por_grado, clustering_total


def distancia_coseno(a, b):
    return 1 - np.inner(a, b) / (LA.norm(a) * LA.norm(b))


def distancia_euclidea(a, b):
    return LA.norm(a - b)


def knn(vectores, k=None, tipo_distancia="coseno"):
    if not k:
        k = int(sqrt(len(vectores)))
    if tipo_distancia == "coseno":
        distancia = distancia_coseno
    elif tipo_distancia == "euclidea":
        distancia = distancia_euclidea
    else:
        raise ValueError("Tipo de distancia desconocida")
    nucleos = random.sample(vectores, k)
    cores = {n[0]: [] for n in nucleos}
    for name, vec in vectores:
        mas_cercano = min(nucleos, key=lambda nuc: distancia(vec, nuc[1]))
        cores[mas_cercano[0]].append(name)
    return cores.values()
