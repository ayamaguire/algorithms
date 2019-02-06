# given a sorted array, create a binary search tree w minimal height
from codifys.chapter4 import traversals


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}, {} , {}".format(self.root, self.left, self.right)

    @classmethod
    def make_tree(cls, arr):
        # take in a sorted array and return a balanced binary search tree
        n = len(arr)
        if arr:
            cls.root = arr[n // 2]
            # print(cls.root)
            cls.left = cls.make_tree(arr[:n//2])
            # print(cls.left)
            cls.right = cls.make_tree(arr[n//2 + 1:])
            return cls()


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    A = BinarySearchTree.make_tree(a)
    print(A)
    # for elem in traversals.in_order(A):
    #     print(elem)
