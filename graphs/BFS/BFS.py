from collections import deque


def search(graph, s):
    """ Search an undirected graph to find all nodes connected to s
    :param dict graph: dictionary representing an undirected graph.
    :return a list of nodes reachable from s"""
    explored = [s]
    queue = deque()
    queue.append(s)
    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if node not in explored:
                explored.append(node)
                queue.append(node)
    return explored


if __name__ == '__main__':
    test_graph = {1: [2, 3],
                  2: [1, 3, 8, 9],
                  3: [1, 2, 4],
                  4: [],
                  5: [6, 7],
                  6: [5, 7, 10],
                  7: [5, 6, 12],
                  8: [2],
                  9: [2],
                  10: [6, 11],
                  11: [10, 12],
                  12: [7, 11]
                  }

    print(search(test_graph, 12))
