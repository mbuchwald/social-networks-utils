import networkx as nx


def contar_aristas(grafo):
    contador = 0
    for v in grafo:
        contador += len(list(grafo.neighbors(v)))
    return contador if nx.is_directed(grafo) else contador // 2


def proporcion_cruzan_campo(grafo, mapper=None):
    """
    :param grafo:
    :param mapper: un mapper de vertice a un tipo (por defecto, grafo[v])
    :return: devuelve la proporcion real que se obtiene de cruces respecto del total de aristas
    """
    aristas_totales = contar_aristas(grafo)
    cruzan_bloque = 0
    visitados = set()
    mapper = mapper if mapper is not None else (lambda k: grafo[k]["type"])

    for v in grafo:
        for w in grafo.neighbors(v):
            if not nx.is_directed(grafo) and w in visitados:
                continue
            if mapper(v) != mapper(w):
                cruzan_bloque += 1
        visitados.add(v)
    return cruzan_bloque / aristas_totales


def proporcion_cruzan_campo_de_tipo(grafo, tipo, mapper=None):
    """
    :param grafo:
    :param tipo: por el cual se quiere calcular especificamente
    :param mapper: un mapper de vertice a un tipo (por defecto, grafo[v])
    :return: devuelve la proporcion real que se obtiene de cruces respecto del total de aristas,
    de un tipo en particular (para ver si hay homofilia/segregacion por parte de un grupo en particular)
    """
    cruzan_bloque = 0
    visitados = set()
    aristas = 0
    mapper = mapper if mapper is not None else (lambda k: grafo[k]["type"])

    for v in grafo:
        if mapper(v) != tipo:
            continue
        for w in grafo.neighbors(v):
            aristas += 1
            if mapper(v) != mapper(w):
                cruzan_bloque += 1
        visitados.add(v)
    return cruzan_bloque / aristas


def proporcion_por_tipo(grafo, mapper=None):
    """
    :param grafo:
    :param mapper: un mapper de vertice a un tipo (por defecto, grafo[v])
    :return: la proporcion que hay de cada tipo
    """
    mapper = mapper if mapper is not None else (lambda k: grafo[k]["type"])
    cantidades = {}
    for v in grafo:
        cantidades[mapper(v)] = cantidades.get(mapper(v), 0) + 1
    props = {}
    for c in cantidades:
        props[c] = cantidades[c] / len(grafo)
    return props
