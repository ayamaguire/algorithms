import pickle
import copy
import random


def create_graph():
    graph = dict()
    with open('graphs/graph.txt', 'r') as file:
        for line in file:
            data = line.split()
            node = data.pop(0)
            graph[node] = data
    return graph


def contract(graph, v1, v2):
    # we will delete v1 and send all of v1s connections to v2
    # first, append all of v1's connections to v2
    graph[v2].extend(graph[v1])
    # now for each vertex, if v1 is in its connections, delete it. Add v2 as a connection.
    for key in graph.keys():
        while v1 in graph[key]:
            graph[key].remove(v1)
            graph[key].append(v2)

    # remove self loops
    while v1 in graph[v2]:
        graph[v2].remove(v1)
    while v2 in graph[v2]:
        graph[v2].remove(v2)
    del graph[v1]


def karger(graph):
    while len(graph.keys()) > 2:
        v1, v2 = 0, 0
        while v1 == v2:
            v1 = random.choice(list(graph.keys()))
            v2 = random.choice(graph[v1])
        contract(graph, v1, v2)


if __name__ == '__main__':
    min = float('inf')
    for i in range(100):
        graph = create_graph()
        karger(graph)
        for key in graph.keys():
            x = len(graph[key])
            if x < min:
                min = x
            print("Iteration {}. Found: {}. min: {}".format(i, x, min))
