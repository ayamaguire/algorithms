# implement the 3 common DFS traversals of binary trees
# in-order: L, root, R
# pre-order: root, L, R
# post-order: L, R, root


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def in_order(node):
    # yield each node, in order
    if node:
        yield from in_order(node.left)
        yield node.val
        yield from in_order(node.right)


def pre_order(node):
    # yield each node, starting with root then from L then from R subtrees
    if node:
        yield node.val
        yield from pre_order(node.left)
        yield from pre_order(node.right)


def post_order(node):
    # yield each node, starting with the L subtree then the R subtree then the root
    if node:
        yield from post_order(node.left)
        yield from post_order(node.right)
        yield node.val


if __name__ == '__main__':
    test_tree = Node(1)
    node2 = Node(2)
    node2.left = Node(4)
    node2.right = Node(5)
    test_tree.left = node2
    test_tree.right = Node(3)
    for item in post_order(test_tree):
        print(item)
