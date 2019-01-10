import networkx as nx
from graphs.DFS import kosaraju
import random


test_graph = dict()
n = 99999
b = 10
for i in range(n):
    test_graph[i] = list(set([random.randint(0, n-1) for j in range(random.randint(0, b))]))
    # test_graph[i].extend(list(set([random.randint(i+1, n-1) for j in range(random.randint(0, 1))])))
print(test_graph)
sccs = kosaraju.kosaraju(test_graph)
# print(sccs)
sccs_dict = dict()
for key, val in sccs.items():
    if not sccs_dict.get(len(val)):
        sccs_dict[len(val)] = 1
    else:
        sccs_dict[len(val)] += 1
    # print(key, len(val))
print("By kojamaru: {}".format(sccs_dict))


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
    # print(len(elem))
print("By networkx: {}".format(next_sccs_dict))
print(next_sccs_dict == sccs_dict)

