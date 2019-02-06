from collections import defaultdict
import random

# given a 2 dimensional graph with points on it, find the line that passes through the most of them

EPSILON = 0.001


class Line(object):
    def __init__(self):
        self.slope = None
        self.intercept = None

    def __eq__(self, other):
        if abs(self.slope - other.slope) < EPSILON and abs(self.intercept - other.intercept) < EPSILON:
            return True
        return False


class Point(object):
    def __init__(self):
        self.x = None
        self.y = None

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)


def points_to_line(p1, p2):
    L = Line()
    if abs(p1.x - p2.x) < EPSILON:
        L.slope = float('inf')
        L.intercept = p1.x
        return L

    L.slope = (p1.y - p2.y) / (p1.x - p2.x)
    L.intercept = ((p1.x * p2.y) - (p2.x * p1.y)) / (p1.x - p2.x)
    return L


def procedure(points):
    lines = defaultdict(set)
    for i, point1 in enumerate(points):
        for point2 in points[i+1:]:
            L = points_to_line(point1, point2)
            lines[(L.slope, L.intercept)].add(point1)
            lines[(L.slope, L.intercept)].add(point2)
    maximum = 0
    most_points = None
    for key, val in lines.items():
        if len(val) > maximum:
            maximum = len(val)
            most_points = key
    print("line: {} passes through {} points".format(most_points, lines[most_points]))
    return most_points


if __name__ == '__main__':
    points = [Point() for x in range(10)]
    for point in points:
        point.x = random.randint(0, 50)
        point.y = random.randint(0, 50)
    print("points: {}".format(points))
    print(procedure(points))
