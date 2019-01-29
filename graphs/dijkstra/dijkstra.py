import networkx as nx


def naive(graph, s):
    """ From source node s, calculate shortest paths to nodes.
    :param dict graph: key val pairs where key is a node and val is a list of tuples, node and length to it
    :param int s: starting node
    """
    X = {s}
    vertices = set(graph.keys())
    A = {s: 0}
    while X != vertices:
        v, w = get_min(graph, X, A)
        X.add(w[0])
        # assert(v in X)
        A[w[0]] = w[1] + A[v]
    return A


def get_min(graph, X, A):
    d = float('inf')
    w = None
    v = None
    for node in X:
        for elem in graph[node]:
            if elem[0] not in X:
                if elem[1] + A[node] < d:
                    d = elem[1] + A[node]
                    w = elem
                    v = node
    return v, w


if __name__ == "__main__":
    graph = dict()
    with open('graphs/dijkstra/graph.txt', 'r') as file:
        for line in file:
            vals = line.split()
            print(vals)
            key = int(vals[0])
            arcs = vals[1:]
            if not graph.get(key):
                graph[key] = [(int(elem.split(',')[0]), int(elem.split(',')[1])) for elem in arcs]
            else:
                graph[key].extend([(int(elem.split(',')[0]), int(elem.split(',')[1])) for elem in arcs])

    print(graph)
    a = naive(graph, 1)

    # 7,37,59,82,99,115,133,165,188,197
    print(a[7], a[37], a[59], a[82], a[99], a[115], a[133], a[165], a[188], a[197])

    # next_graph = nx.DiGraph(graph)
    #
    # next_sccs = list(nx.strongly_connected_components(next_graph))

