import pickle


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
    leaders[i] = s
    for node in graph[i]:
        if node not in explored:
            F, t, leaders = search(graph, node, F, t, s, explored, leaders)
    t += 1
    F[i] = t
    return F, t, leaders


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
    # explored.append(i)
    # leaders[i] = s
    # for node in graph[i]:
    #     if node not in explored:
    #         F, t, leaders = reverse_search(graph, node, F, t, s, explored, leaders)
    # t = t - 1
    # F[i] = t
    # return F, t, leaders
    graph_rev = reverse_graph(graph)
    return search(graph_rev, i, F, t, s, explored, leaders)


def search_loop(graph, direction):
    if direction == 'forward':
        t = 0
    elif direction == 'reverse':
        t = len(graph.keys()) + 1
    else:
        assert False
    s = None
    finishing_times = dict()
    leaders = dict()
    explored = []
    keys = list(graph.keys())
    keys.sort()
    keys.reverse()
    for node in keys:
        if node not in explored:
            s = node
            print("searching on: {}".format(node))
            if direction == 'forward':
                finishing_times, t, leaders = search(graph, node, finishing_times, t, s, explored, leaders)
            elif direction == 'reverse':
                finishing_times, t, leaders = reverse_search(graph, node, finishing_times, t, s, explored, leaders)
            else:
                assert False
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
    f1, l1 = search_loop(graph, 'reverse')
    print("searched backwards")
    graph = relabel_graph(graph, f1)
    print("Relabelled graph")
    f2, l2 = search_loop(graph, 'forward')
    print("searched forward")
    sccs = dict()
    for key, val in l2.items():
        if not sccs.get(val):
            sccs[val] = [key]
        else:
            sccs[val].append(key)
    return sccs


if __name__ == '__main__':
    # test_graph = {1: [2],
    #               2: [3, 4],
    #               3: [1],
    #               4: [5],
    #               5: [6],
    #               6: [4]
    #               }

    # test_graph = {0: [1, 2], 1: [3], 2: [4], 3: [1, 4], 4: [2], 5: [3, 5]}
    #
    # print(kosaraju(test_graph))

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
    with open('graphs/DFS/scc.pkl', 'rb') as file:
        scc_graph = pickle.load(file)

    leaders = kosaraju(scc_graph)
    print(leaders)

    with open('graphs/DFS/leaders.pkl', 'wb') as file:
        pickle.dump(leaders, file, pickle.HIGHEST_PROTOCOL)
