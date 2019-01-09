
def search(graph, s, F, label, explored=None):
    """ Search a directed acyclic graph for topological sort
    :param dict graph: dictionary representing a directed graph.
    :param int s: the starting node
    :param dict F: the dictionary representing node labels
    :param int label: the current label, decremented as we find nodes
    :param list explored: the list of nodes already explored
    :return F, the dict of node labels, filled in"""
    explored.append(s)
    for node in graph[s]:
        if node not in explored:
            F, label = search(graph, node, F, label, explored)
    F[s] = label
    label = label - 1
    return F, label


def topological_sort(graph):
    explored = []
    label = len(graph.keys())
    ordering = dict()
    for node in graph.keys():
        if node not in explored:
            ordering, label = search(graph, node, ordering, label, explored)
    return ordering


if __name__ == '__main__':
    test_graph = {1: [2, 3],
                  2: [3, 4, 8],
                  3: [5],
                  4: [],
                  5: [6, 7],
                  6: [],
                  7: [],
                  8: [9],
                  9: [10],
                  10: []
                  }

    print(topological_sort(test_graph))
