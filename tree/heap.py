import math


class Heap(object):
    def __init__(self, elements, heapify=True):
        self.elements = elements
        self.heaped = False
        if heapify:
            self.heapify()

    def __bool__(self):
        if self.elements:
            return True
        return False

    def __repr__(self):
        if not self.heaped:
            return "Unorganized heap with elements {}. Call heapify to organize".format(self.elements)
        return "Heap with elements {}".format(self.elements)

    def parent(self, index):
        """ Returns the index of the parent of index."""
        if index == 0:
            return index
        return (index - 1) // 2

    def right(self, index):
        """ returns the index of the right child of index"""
        if 2 * index + 2 > len(self.elements) - 1:
            return index
        return 2 * index + 2

    def left(self, index):
        """ returns the index of the left child of index"""
        if 2 * index + 1 > len(self.elements) - 1:
            return index
        return 2 * index + 1

    def insert(self, element):
        self.elements.append(element)
        self.bubble_up(len(self.elements) - 1)

    def extract(self):
        self.elements[0], self.elements[-1] = self.elements[-1], self.elements[0]
        minimum = self.elements.pop(-1)
        if self.elements:
            self.bubble_down(0)
        return minimum

    def heapify(self):
        n = len(self.elements)
        for k in range(n-1, n // 2 - 1, -1):
            self.bubble_up(k)
        self.heaped = True

    def bubble_up(self, index):
        p = self.parent(index)
        while self.elements[index] < self.elements[p]:
            self.elements[index], self.elements[p] = self.elements[p], self.elements[index]
            index = p
            p = self.parent(index)

    def bubble_down(self, index):
        l, r = self.left(index), self.right(index)
        if self.elements[l] < self.elements[r]:
            minindex = l
        else:
            minindex = r
        while self.elements[index] > self.elements[minindex]:
            self.elements[minindex], self.elements[index] = self.elements[index], self.elements[minindex]
            index = minindex
            l, r = self.left(index), self.right(index)
            if self.elements[l] < self.elements[r]:
                minindex = l
            else:
                minindex = r

    def delete(self, index):
        self.elements[index], self.elements[-1] = self.elements[-1], self.elements[index]
        self.elements.pop(-1)
        if self.elements:
            self.bubble_down(index)


if __name__ == '__main__':
    a = [5, 8, 6, 9, 1, 2, 4, 3, 7]
    heap = Heap(a)
    print(heap)
    while heap:
        a = heap.extract()
        print(a, heap)

