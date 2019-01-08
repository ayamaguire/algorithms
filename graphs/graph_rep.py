import random


class UndirectedGraph(object):
    def __init__(self, vertices=None, edges=None):
        self.vertices = vertices
        self.edges = edges

    def __repr__(self):
        return "Undirected Graph with vertices {} and edges {}".format(self.vertices, self.edges)

    def contract(self, edge):
        vt_remove = edge[1]
        vt_keep = edge[0]
        self.edges.remove(edge)
        self.vertices.remove(vt_remove)
        for elem in self.edges:
            if elem[0] == vt_remove:
                self.edges.remove(elem)
                self.edges.append((elem[1], vt_keep))
            elif elem[1] == vt_remove:
                self.edges.remove(elem)
                self.edges.append((elem[0], vt_keep))
            if elem[0] == elem[1]:
                self.edges.remove(elem)

    def karger(self):
        while len(self.vertices) > 2:
            edge = self.edges[random.randint(0, len(self.edges)-1)]
            self.contract(edge)


if __name__ == '__main__':
    graph = UndirectedGraph(vertices=[0, 1, 2, 3, 4], edges=[(0, 1), (1, 2), (2, 3), (3, 4)])
    print(graph)
    graph.karger()
    print(graph)
