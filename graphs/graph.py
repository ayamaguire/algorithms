import random


class Graph(object):
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.n = None
        self.m = None

    def __repr__(self):
        return "Graph with vertices {} and edges {}".format(self.vertices, self.edges)

    def lengths(self):
        # since a graph can change let's recalculate sometimes
        self.n = len(self.vertices)
        self.m = len(self.edges)

    def contract(self):
        # print(len(self.edges))
        contracted_edge = self.edges[random.randint(0, len(self.edges)-1)]
        for elem in contracted_edge.end.children:
            contracted_edge.start.children.append(elem)
            contracted_edge.end.children.remove(elem)
        contracted_edge.start.children.append(contracted_edge.end)
        for edge in self.edges:
            if edge.start.value == contracted_edge.start.value and edge.end.value == contracted_edge.end.value:
                self.edges.remove(edge)
                break
        # self.edges.remove(contracted_edge)
        for vertex in self.vertices:
            if vertex.value == contracted_edge.end.value:
                self.vertices.remove(vertex)
                break
        # self.vertices.remove(contracted_edge.end)
        for edge in self.edges:
            if edge.start.value == contracted_edge.end.value:
                edge.start = contracted_edge.start
            if edge.end.value == contracted_edge.end.value:
                edge.end = contracted_edge.start
            if edge.start.value == edge.end.value:
                self.edges.remove(edge)

    def karger(self):
        """ contracts until only 2 vertices left, returns the cut."""
        while len(self.vertices) > 2:
            self.contract()
            # print(len(self.edges), len(self.vertices))
        partitions = [None, None]
        for i, vertex in enumerate(self.vertices):
            partitions[i] = [vertex]
            for elem in vertex.children:
                partitions[i].append(elem)
        return partitions, len(self.edges)


class Edge(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return "({} to {})".format(self.start, self.end)


class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        if self.children:
            return "S{} ({})".format(self.value, self.children)
        return "V{}".format(self.value)


if __name__ == '__main__':
    vertices = [Vertex(0), Vertex(1), Vertex(2), Vertex(3)]
    edges = [Edge(vertices[0], vertices[1]),
             Edge(vertices[1], vertices[2]),
             Edge(vertices[0], vertices[2]),
             Edge(vertices[2], vertices[3])]
    graph = Graph(vertices, edges)
    print(graph)
    print(graph.karger())
    print(graph)


