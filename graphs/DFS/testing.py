import networkx as nx
import pickle
from graphs.DFS import kosaraju
import random


test_graph = dict()
n = 1000
b = 30
for i in range(1, n+1):
    test_graph[i] = list(set([random.randint(1, n) for j in range(random.randint(0, b))]))
print(test_graph)


sccs = kosaraju.kosaraju(test_graph, n)
sccs_dict = dict()
for key, val in sccs.items():
    if not sccs_dict.get(len(val)):
        sccs_dict[len(val)] = 1
    else:
        sccs_dict[len(val)] += 1
print("By kosaraju: {}".format(sccs_dict))


# by networkx package for confirmation
edges = []
for key, val in test_graph.items():
    for elem in val:
        edges.append((key, elem))

next_graph = nx.DiGraph()

next_graph.add_nodes_from(test_graph.keys())
next_graph.add_edges_from(edges)
next_sccs = list(nx.strongly_connected_components(next_graph))


# print(next_sccs)
next_sccs_dict = dict()
for elem in next_sccs:
    if not next_sccs_dict.get(len(elem)):
        next_sccs_dict[len(elem)] = 1
    else:
        next_sccs_dict[len(elem)] += 1
print("By networkx: {}".format(next_sccs_dict))
print(next_sccs_dict == sccs_dict)


# By networkx: {1: 358888, 18: 75, 8: 455, 6: 817, 15: 120, 67: 2, 2: 4169, 3: 1877, 10: 297, 37: 8, 7: 661, 4: 1462, 24: 20, 20: 72, 5: 1033, 14: 131, 11: 244, 29: 18, 22: 35, 16: 92, 23: 34, 9: 347, 32: 10, 47: 3, 19: 87, 12: 216, 13: 141, 28: 23, 30: 21, 34: 10, 197: 1, 69: 2, 211: 1, 968: 1, 21: 67, 17: 87, 38: 4, 56: 3, 48: 4, 33: 12, 78: 2, 51: 5, 44: 4, 45: 7, 205: 1, 27: 23, 68: 3, 25: 24, 40: 5, 36: 7, 26: 17, 54: 3, 49: 3, 77: 3, 53: 4, 72: 3, 52: 2, 96: 1, 59: 5, 71: 2, 63: 2, 64: 2, 31: 22, 149: 1, 55: 6, 459: 1, 35: 8, 90: 1, 41: 5, 138: 1, 101: 1, 43: 5, 39: 7, 85: 1, 434821: 1, 46: 1, 112: 1, 66: 1, 65: 2, 313: 1, 75: 1, 93: 1, 58: 2, 162: 1, 177: 1, 125: 1, 146: 1, 81: 1, 97: 1, 102: 2, 152: 1, 70: 1, 122: 1, 73: 1, 42: 2}
