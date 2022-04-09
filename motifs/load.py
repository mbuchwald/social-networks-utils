import networkx as nx

'''
GRAFOS NO DIRIGIDOS:
'''


def MOTIF_NO_DIR_3():
    g = []
    for i in range(2):
        g.append(nx.Graph())
    #g1
    g[0].add_edge(1, 2)
    g[0].add_edge(1, 3)
    g[0].nodes[1]["type"] = 2
    g[0].nodes[2]["type"] = 1
    g[0].nodes[3]["type"] = 1
    #g2
    g[1].add_edge(1, 2)
    g[1].add_edge(1, 3)
    g[1].add_edge(2, 3)
    g[1].nodes[1]["type"] = 3
    g[1].nodes[2]["type"] = 3
    g[1].nodes[3]["type"] = 3
    return g


def MOTIF_NO_DIR_4():
    g = []
    for i in range(6):
        g.append(nx.Graph())
    #g3
    g[0].add_edge(1, 2)
    g[0].add_edge(3, 2)
    g[0].add_edge(3, 4)
    g[0].nodes[1]["type"] = 4
    g[0].nodes[4]["type"] = 4
    g[0].nodes[2]["type"] = 5
    g[0].nodes[3]["type"] = 5
    #g4
    g[1].add_edge(1, 2)
    g[1].add_edge(3, 2)
    g[1].add_edge(2, 4)
    g[1].nodes[1]["type"] = 6
    g[1].nodes[2]["type"] = 7
    g[1].nodes[3]["type"] = 6
    g[1].nodes[4]["type"] = 6
    #g5
    g[2].add_edge(1, 2)
    g[2].add_edge(3, 2)
    g[2].add_edge(3, 4)
    g[2].add_edge(1, 4)
    g[2].nodes[1]["type"] = 8
    g[2].nodes[2]["type"] = 8
    g[2].nodes[3]["type"] = 8
    g[2].nodes[4]["type"] = 8
    #g6
    g[3].add_edge(1, 2)
    g[3].add_edge(3, 2)
    g[3].add_edge(3, 1)
    g[3].add_edge(3, 4)
    g[3].nodes[3]["type"] = 11
    g[3].nodes[4]["type"] = 9
    g[3].nodes[1]["type"] = 10
    g[3].nodes[2]["type"] = 10
    #g7
    g[4].add_edge(1, 2)
    g[4].add_edge(3, 2)
    g[4].add_edge(3, 4)
    g[4].add_edge(1, 4)
    g[4].add_edge(1, 3)
    g[4].nodes[1]["type"] = 13
    g[4].nodes[3]["type"] = 13
    g[4].nodes[2]["type"] = 12
    g[4].nodes[4]["type"] = 12
    #g8
    g[5].add_edge(1, 2)
    g[5].add_edge(3, 2)
    g[5].add_edge(3, 4)
    g[5].add_edge(1, 4)
    g[5].add_edge(1, 3)
    g[5].add_edge(2, 4)
    g[5].nodes[1]["type"] = 14
    g[5].nodes[2]["type"] = 14
    g[5].nodes[3]["type"] = 14
    g[5].nodes[4]["type"] = 14
    return g


def MOTIF_NO_DIR_5():
    g = []
    for i in range(21):
        g.append(nx.Graph())
    #g9
    g[0].add_edge(1, 2)
    g[0].add_edge(3, 2)
    g[0].add_edge(3, 4)
    g[0].add_edge(4, 5)
    g[0].nodes[1]["type"] = 15
    g[0].nodes[2]["type"] = 16
    g[0].nodes[3]["type"] = 17
    g[0].nodes[4]["type"] = 16
    g[0].nodes[5]["type"] = 15
    #g10
    g[1].add_edge(1, 2)
    g[1].add_edge(3, 2)
    g[1].add_edge(2, 4)
    g[1].add_edge(5, 1)
    g[1].nodes[5]["type"] = 18
    g[1].nodes[4]["type"] = 19
    g[1].nodes[5]["type"] = 19
    g[1].nodes[1]["type"] = 20
    g[1].nodes[2]["type"] = 21
    #g11
    g[2].add_edge(1, 2)
    g[2].add_edge(1, 3)
    g[2].add_edge(1, 4)
    g[2].add_edge(1, 5)
    g[2].nodes[1]["type"] = 23
    g[2].nodes[2]["type"] = 22
    g[2].nodes[3]["type"] = 22
    g[2].nodes[4]["type"] = 22
    g[2].nodes[5]["type"] = 22
    #g12
    g[3].add_edge(1, 2)
    g[3].add_edge(3, 2)
    g[3].add_edge(3, 1)
    g[3].add_edge(3, 4)
    g[3].add_edge(5, 2)
    g[3].nodes[5]["type"] = 24
    g[3].nodes[4]["type"] = 24
    g[3].nodes[1]["type"] = 25
    g[3].nodes[2]["type"] = 26
    g[3].nodes[3]["type"] = 26
    #g13
    g[4].add_edge(1, 2)
    g[4].add_edge(3, 2)
    g[4].add_edge(3, 1)
    g[4].add_edge(3, 4)
    g[4].add_edge(4, 5)
    g[4].nodes[5]["type"] = 27
    g[4].nodes[4]["type"] = 28
    g[4].nodes[3]["type"] = 30
    g[4].nodes[2]["type"] = 29
    g[4].nodes[1]["type"] = 29
    #g14
    g[5].add_edge(1, 2)
    g[5].add_edge(3, 2)
    g[5].add_edge(3, 1)
    g[5].add_edge(3, 4)
    g[5].add_edge(3, 5)
    g[5].nodes[4]["type"] = 31
    g[5].nodes[5]["type"] = 31
    g[5].nodes[3]["type"] = 33
    g[5].nodes[1]["type"] = 32
    g[5].nodes[2]["type"] = 32
    #g15
    g[6].add_edge(1, 2)
    g[6].add_edge(3, 2)
    g[6].add_edge(3, 4)
    g[6].add_edge(5, 4)
    g[6].add_edge(5, 1)
    g[6].nodes[1]["type"] = 34
    g[6].nodes[2]["type"] = 34
    g[6].nodes[3]["type"] = 34
    g[6].nodes[4]["type"] = 34
    g[6].nodes[5]["type"] = 34
    #g16
    g[7].add_edge(1, 2)
    g[7].add_edge(3, 2)
    g[7].add_edge(3, 4)
    g[7].add_edge(1, 4)
    g[7].add_edge(5, 1)
    g[7].nodes[5]["type"] = 35
    g[7].nodes[1]["type"] = 38
    g[7].nodes[2]["type"] = 37
    g[7].nodes[4]["type"] = 37
    g[7].nodes[3]["type"] = 36
    #17
    g[8].add_edge(1, 2)
    g[8].add_edge(3, 2)
    g[8].add_edge(3, 4)
    g[8].add_edge(1, 4)
    g[8].add_edge(1, 3)
    g[8].add_edge(5, 1)
    g[8].nodes[5]["type"] = 39
    g[8].nodes[1]["type"] = 42
    g[8].nodes[2]["type"] = 40
    g[8].nodes[4]["type"] = 40
    g[8].nodes[3]["type"] = 41
    #18
    g[9].add_edge(1, 2)
    g[9].add_edge(1, 3)
    g[9].add_edge(2, 3)
    g[9].add_edge(1, 4)
    g[9].add_edge(1, 5)
    g[9].add_edge(4, 5)
    g[9].nodes[1]["type"] = 44
    g[9].nodes[2]["type"] = 43
    g[9].nodes[3]["type"] = 43
    g[9].nodes[4]["type"] = 43
    g[9].nodes[5]["type"] = 43
    #19
    g[10].add_edge(1, 2)
    g[10].add_edge(3, 2)
    g[10].add_edge(3, 4)
    g[10].add_edge(1, 4)
    g[10].add_edge(5, 1)
    g[10].add_edge(2, 4)
    g[10].nodes[5]["type"] = 45
    g[10].nodes[1]["type"] = 47
    g[10].nodes[2]["type"] = 48
    g[10].nodes[4]["type"] = 48
    g[10].nodes[3]["type"] = 46
    #g20
    g[11].add_edge(1, 2)
    g[11].add_edge(1, 3)
    g[11].add_edge(1, 4)
    g[11].add_edge(5, 2)
    g[11].add_edge(5, 3)
    g[11].add_edge(5, 4)
    g[11].nodes[1]["type"] = 50
    g[11].nodes[5]["type"] = 50
    g[11].nodes[2]["type"] = 49
    g[11].nodes[3]["type"] = 49
    g[11].nodes[4]["type"] = 49
    #g21
    g[12].add_edge(1, 2)
    g[12].add_edge(3, 2)
    g[12].add_edge(3, 1)
    g[12].add_edge(3, 4)
    g[12].add_edge(4, 5)
    g[12].add_edge(5, 2)
    g[12].nodes[2]["type"] = 53
    g[12].nodes[3]["type"] = 53
    g[12].nodes[5]["type"] = 51
    g[12].nodes[1]["type"] = 52
    g[12].nodes[4]["type"] = 51
    #g22
    g[13].add_edge(1, 2)
    g[13].add_edge(3, 2)
    g[13].add_edge(1, 3)
    g[13].add_edge(4, 2)
    g[13].add_edge(4, 3)
    g[13].add_edge(5, 2)
    g[13].add_edge(5, 3)
    g[13].nodes[2]["type"] = 55
    g[13].nodes[3]["type"] = 55
    g[13].nodes[1]["type"] = 54
    g[13].nodes[4]["type"] = 54
    g[13].nodes[5]["type"] = 54
    #g23
    g[14].add_edge(1, 2)
    g[14].add_edge(1, 3)
    g[14].add_edge(1, 4)
    g[14].add_edge(3, 2)
    g[14].add_edge(3, 4)
    g[14].add_edge(2, 4)
    g[14].add_edge(1, 5)
    g[14].nodes[5]["type"] = 56
    g[14].nodes[1]["type"] = 58
    g[14].nodes[2]["type"] = 57
    g[14].nodes[3]["type"] = 57
    g[14].nodes[4]["type"] = 57
    #g24
    g[15].add_edge(1, 2)
    g[15].add_edge(2, 3)
    g[15].add_edge(1, 3)
    g[15].add_edge(2, 4)
    g[15].add_edge(3, 4)
    g[15].add_edge(2, 5)
    g[15].add_edge(4, 5)
    g[15].nodes[2]["type"] = 61
    g[15].nodes[5]["type"] = 59
    g[15].nodes[1]["type"] = 59
    g[15].nodes[4]["type"] = 60
    g[15].nodes[3]["type"] = 60
    #g25
    g[16].add_edge(1, 2)
    g[16].add_edge(1, 3)
    g[16].add_edge(1, 4)
    g[16].add_edge(5, 2)
    g[16].add_edge(5, 3)
    g[16].add_edge(5, 4)
    g[16].add_edge(3, 4)
    g[16].nodes[2]["type"] = 62
    g[16].nodes[5]["type"] = 63
    g[16].nodes[1]["type"] = 63
    g[16].nodes[4]["type"] = 64
    g[16].nodes[3]["type"] = 64
    #g26
    g[17].add_edge(1, 2)
    g[17].add_edge(3, 2)
    g[17].add_edge(1, 3)
    g[17].add_edge(4, 2)
    g[17].add_edge(4, 3)
    g[17].add_edge(5, 2)
    g[17].add_edge(5, 3)
    g[17].add_edge(4, 5)
    g[17].nodes[1]["type"] = 65
    g[17].nodes[2]["type"] = 67
    g[17].nodes[3]["type"] = 67
    g[17].nodes[4]["type"] = 66
    g[17].nodes[5]["type"] = 66
    #g27
    g[18].add_edge(1, 2)
    g[18].add_edge(2, 3)
    g[18].add_edge(3, 4)
    g[18].add_edge(4, 1)
    g[18].add_edge(5, 1)
    g[18].add_edge(5, 2)
    g[18].add_edge(5, 3)
    g[18].add_edge(5, 4)
    g[18].nodes[1]["type"] = 68
    g[18].nodes[2]["type"] = 68
    g[18].nodes[3]["type"] = 68
    g[18].nodes[4]["type"] = 68
    g[18].nodes[5]["type"] = 69
    #g28
    g[19].add_edge(1, 2)
    g[19].add_edge(1, 3)
    g[19].add_edge(1, 4)
    g[19].add_edge(2, 3)
    g[19].add_edge(2, 4)
    g[19].add_edge(2, 5)
    g[19].add_edge(3, 4)
    g[19].add_edge(3, 5)
    g[19].add_edge(4, 5)
    g[19].nodes[1]["type"] = 70
    g[19].nodes[2]["type"] = 71
    g[19].nodes[3]["type"] = 71
    g[19].nodes[4]["type"] = 71
    g[19].nodes[5]["type"] = 70
    #g29
    g[20].add_edge(1, 2)
    g[20].add_edge(1, 3)
    g[20].add_edge(1, 4)
    g[20].add_edge(1, 5)
    g[20].add_edge(2, 3)
    g[20].add_edge(2, 4)
    g[20].add_edge(2, 5)
    g[20].add_edge(3, 4)
    g[20].add_edge(3, 5)
    g[20].add_edge(4, 5)
    g[20].nodes[1]["type"] = 72
    g[20].nodes[2]["type"] = 72
    g[20].nodes[3]["type"] = 72
    g[20].nodes[4]["type"] = 72
    g[20].nodes[5]["type"] = 72

    return g


MOTIF_NO_DIR = {3: MOTIF_NO_DIR_3, 4: MOTIF_NO_DIR_4, 5: MOTIF_NO_DIR_5}


'''
GRAFOS DIRIGIDOS:
'''


def MOTIF_DIR_2():
    g = []
    for i in range(2):
        g.append(nx.DiGraph())
    g[0].add_edge(1, 2)
    g[1].add_edge(1, 2)
    g[1].add_edge(2, 1)
    return g


def MOTIF_DIR_3():
    g = []
    for i in range(13):
        g.append(nx.DiGraph())

    g[0].add_edge(1, 2)
    g[0].add_edge(1, 3)
    g[1].add_edge(2, 1)
    g[1].add_edge(3, 1)
    g[2].add_edge(1, 2)
    g[2].add_edge(2, 3)
    g[3].add_edge(1, 2)
    g[3].add_edge(2, 3)
    g[3].add_edge(3, 2)
    g[4].add_edge(1, 2)
    g[4].add_edge(2, 1)
    g[4].add_edge(2, 3)
    g[5].add_edge(1, 2)
    g[5].add_edge(2, 1)
    g[5].add_edge(3, 2)
    g[5].add_edge(2, 3)
    g[6].add_edge(1, 2)
    g[6].add_edge(1, 3)
    g[6].add_edge(2, 3)
    g[7].add_edge(1, 2)
    g[7].add_edge(2, 3)
    g[7].add_edge(3, 1)
    g[8].add_edge(1, 2)
    g[8].add_edge(1, 3)
    g[8].add_edge(2, 3)
    g[8].add_edge(3, 2)
    g[9].add_edge(3, 2)
    g[9].add_edge(2, 3)
    g[9].add_edge(3, 1)
    g[9].add_edge(2, 1)
    g[10].add_edge(1, 2)
    g[10].add_edge(2, 3)
    g[10].add_edge(3, 1)
    g[10].add_edge(1, 3)
    g[11].add_edge(2, 3)
    g[11].add_edge(3, 2)
    g[11].add_edge(2, 1)
    g[11].add_edge(3, 1)
    g[11].add_edge(1, 3)
    g[12].add_edge(1, 2)
    g[12].add_edge(1, 3)
    g[12].add_edge(2, 1)
    g[12].add_edge(2, 3)
    g[12].add_edge(3, 1)
    g[12].add_edge(3, 2)
    return g


MOTIF_DIR = {2: MOTIF_DIR_2, 3: MOTIF_DIR_3}

'''
GRAFOS HOMOFILIA NO DIRIGIDO:
'''

'''
GRAFOS HOMOFILIA DIRIGIDO:
'''

'''
GRAFOS TEMPORAL NO DIRIGIDO:
'''

'''
GRAFOS TEMPORAL DIRIGIDO:
'''
