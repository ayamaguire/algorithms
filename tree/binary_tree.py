from collections import deque


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "node {}".format(self.value)


class BinaryTree(object):
    def __init__(self, head):
        self.head = head

    def __repr__(self):
        q = deque([])
        retstring = str(self.head)
        if self.head.left:
            q.append(self.head.left)
        if self.head.right:
            q.append(self.head.right)
        while q:
            el = q.popleft()
            retstring = "{} {}".format(retstring, el)
            if el.left:
                q.append(el.left)
            if el.right:
                q.append(el.right)
        return retstring


if __name__ == '__main__':
    node4 = Node(4)
    node3 = Node(3)
    node2 = Node(2, node4)
    node1 = Node(1, node2, node3)
    a = BinaryTree(node1)
    print(a)
