from graphs.DFS import db
import pickle
# from graphs.DFS.kosaraju import recursive_search

db.Database.initialize()


def recursive_search(i, F, t, s, explored, leaders, order):
    """ Search a directed acyclic graph for topological sort
    :param dict graph: dictionary representing a directed graph.
    :param int i: the starting node
    :param dict F: the dictionary representing finishing times
    :param int t: processed nodes so far
    :param int s: current leader
    :param list explored: the list of nodes already explored
    :param dict leaders: dict of leaders for each node marking SCCs
    :return F, the dict of node labels, filled in"""
    x = len(explored)
    if x % 10 == 0:
        print("Length of explored: {}".format(x))
    explored.append(i)
    if order == 2:
        leaders[i] = s
    arc_list = db.Database.find_one(collection="biggraph", query={"key": i})
    if arc_list:
        for node in arc_list['value']:
            if node not in explored:
                F, t, leaders, explored = recursive_search(node, F, t, s, explored, leaders, order)
        if order == 1:
            t += 1
            F[i] = t
    return F, t, leaders, explored


print(db.Database.find_one(collection="biggraph", query={"key": 875709}))


t = 0
finishing_times = dict()
leaders = dict()
explored = []

for node in range(875714, 0, -1):
    # print("node: {}".format(node))
    if node not in explored:
        leader = node
        # print("searching on: {}".format(node))
        finishing_times, t, leaders, explored = recursive_search(node, finishing_times, t, leader, explored, leaders, 1)

with open('graphs/DFS/finishing_times.pkl', 'wb') as file:
    pickle.dump(finishing_times, file, pickle.HIGHEST_PROTOCOL)

