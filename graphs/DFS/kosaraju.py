import pickle


def recursive_search(graph, i, F, t, s, explored, leaders):
    """ Search a directed acyclic graph for topological sort
    :param dict graph: dictionary representing a directed graph.
    :param int i: the starting node
    :param dict F: the dictionary representing finishing times
    :param int t: processed nodes so far
    :param int s: current leader
    :param list explored: the list of nodes already explored
    :param dict leaders: dict of leaders for each node marking SCCs
    :return F, the dict of node labels, filled in"""
    explored.append(i)
    leaders[i] = s
    for node in graph[i]:
        if node not in explored:
            F, t, leaders = recursive_search(graph, node, F, t, s, explored, leaders)
    t += 1
    F[i] = t
    return F, t, leaders


def search(graph, i, F, t, s, explored, leaders):
    """ Search a directed acyclic graph for topological sort
    :param dict graph: dictionary representing a directed graph.
    :param int i: the starting node
    :param dict F: the dictionary representing finishing times
    :param int t: processed nodes so far
    :param int s: current leader
    :param list explored: the list of nodes already explored
    :param dict leaders: dict of leaders for each node marking SCCs
    :return F, the dict of node labels, filled in"""
    explored.append(i)
    # leaders[i] = s
    stack = [i]
    order = [i]
    while stack:
        v = stack.pop()
        for node in graph[v]:
            if node not in explored:
                explored.append(node)
                stack.append(node)
                order.append(node)

    print("order: {}".format(order))
    for elem in order[::-1]:
        leaders[elem] = s
        F[elem] = t
        t += 1
    return F, t, leaders, explored


def reverse_search(graph, i, F, t, s, explored, leaders):
    """ Search a directed acyclic graph for topological sort
    :param dict graph: dictionary representing a directed graph.
    :param int i: the starting node
    :param dict F: the dictionary representing finishing times
    :param int t: processed nodes so far
    :param int s: current leader
    :param list explored: the list of nodes already explored
    :param dict leaders: dict of leaders for each node marking SCCs
    :return F, the dict of node labels, filled in"""
    graph_rev = reverse_graph(graph)
    explored.append(i)
    leaders[i] = s
    stack = [i]
    while stack:
        v = stack.pop(0)
        for node in graph_rev[v]:
            if node not in explored:
                explored.append(node)
                stack.insert(0, node)
                leaders[node] = s
                F[node] = t
                t += 1
        if v not in F.keys():
            F[v] = t
            t += 1

    return F, t, leaders


def search_loop(graph, rev=True):
    t = 0
    finishing_times = dict()
    leaders = dict()
    explored = []
    nodes = list(graph.keys())
    nodes.sort()
    if rev:
        nodes.reverse()
    for node in nodes:
        # print("node: {}. explored {}".format(node, explored))
        if node not in explored:
            leader = node
            # print("searching on: {}".format(node))
            finishing_times, t, leaders, explored = search(graph, node, finishing_times, t, leader, explored, leaders)
    return finishing_times, leaders


def relabel_graph(graph, finishing_times):
    # is there an easy way to do this inplace?
    new_graph = dict()
    for key in graph.keys():
        new_graph[finishing_times[key]] = [finishing_times[elem] for elem in graph[key]]
    return new_graph


def reverse_graph(graph):
    graph_rev = dict()
    for key in graph.keys():
        if not graph_rev.get(key):
            graph_rev[key] = []
        for node in graph[key]:
            if graph_rev.get(node):
                graph_rev[node].append(key)
            else:
                graph_rev[node] = [key]
    return graph_rev


def kosaraju(graph):
    print("Graph rev: {}".format(graph))
    f1, l1 = search_loop(graph, True)
    # print("searched backwards")
    print("finishing times: {}".format(f1))
    graph = relabel_graph(graph, f1)
    graph_rev = reverse_graph(graph)
    print("Relabelled graph: {}".format(graph_rev))
    f2, l2 = search_loop(graph_rev)
    # print("searched forward")
    print("leaders: {}".format(l2))
    sccs = dict()
    for key, val in l2.items():
        if not sccs.get(val):
            sccs[val] = [key]
        else:
            sccs[val].append(key)
    return sccs


if __name__ == '__main__':
    # test_graph = {0: [], 1: [2, 3, 5], 2: [4], 3: [], 4: [9], 5: [8, 1, 5], 6: [1, 4, 7], 7: [4], 8: [0], 9: [7]}
    # test_graph = {1: [2, 4], 2: [3], 3: [1], 4: [5, 7], 5: [6], 6: [4], 7: [8], 8: [9], 9: [7]}
    # test_graph = {0: [1, 7], 1: [8], 2: [0, 1], 3: [8, 1], 4: [2, 5], 5: [1, 9], 6: [3, 6], 7: [5], 8: [0, 6, 7], 9: [1, 5]}

    test_graph = {0: [], 1: [2, 3, 7], 2: [0, 7], 3: [], 4: [], 5: [8, 2, 6], 6: [6], 7: [3, 6], 8: [8, 2], 9: [2]}

    #graph_rev = reverse_graph(test_graph)
    # print(graph_rev)
    # print(search_loop(graph_rev))
    print("kosaraju says: {}".format(kosaraju(test_graph)))

    # scc_graph = dict()
    #
    # with open('graphs/DFS/scc.txt', 'r') as file:
    #     for line in file:
    #         vals = line.split()
    #         if not scc_graph.get(vals[0]):
    #             scc_graph[vals[0]] = [elem for elem in vals[1:]]
    #         else:
    #             scc_graph[vals[0]].extend([elem for elem in vals[1:]])
    #
    # with open('graphs/DFS/scc.pkl', 'wb') as file:
    #     pickle.dump(scc_graph, file, pickle.HIGHEST_PROTOCOL)

    # RUN KOSARAJU ON THE BIG GRAPH!
    # with open('graphs/DFS/scc.pkl', 'rb') as file:
    #     scc_graph = pickle.load(file)
    #
    # leaders = kosaraju(scc_graph)
    # print(leaders)
    #
    # with open('graphs/DFS/leaders.pkl', 'wb') as file:
    #     pickle.dump(leaders, file, pickle.HIGHEST_PROTOCOL)
