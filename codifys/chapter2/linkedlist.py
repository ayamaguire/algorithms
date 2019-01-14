import math


NOTHING = object()


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return "{}".format(self.value)


class LinkedList(object):
    def __init__(self, head):
        self.head = head
        self.end = None
        self.length = None

    def __repr__(self):
        string = "{}, ".format(self.head.value)
        current = self.head
        while current.next:
            current = current.next
            string = string + "{}, ".format(current.value)
        return string

    def find_end(self):
        current = self.head
        length = 1
        while current.next:
            length += 1
            current = current.next
        self.length = length
        self.end = current

    def append(self, node):
        if not self.end:
            self.find_end()
        self.end.next = node
        self.end = node
        self.length += 1
        assert self.end.next is None

    def remove(self, node):
        if self.head.value == node.value:
            self.head = self.head.next
        current = self.head
        while current.next:
            previous = current
            current = current.next
            if current.value == node.value:
                previous.next = current.next
        self.length -= 1

    def remove_duplicates(self):
        values = [self.head.value]
        current = self.head
        while current.next:
            previous = current
            current = current.next
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.append(current.value)

    def get_k_to_last_with_len(self, k):
        if not self.length:
            self.find_end()
        if k > self.length:
            raise ListLengthError("element {} requested outside of list length {}".format(k, self.length))
        current = self.head
        for i in range(self.length-k):
            current = current.next
        return current

    def get_k_to_last(self, k):
        pass

    def get_k_to_last_helper(self, k, mook, head=None):
        if head is NOTHING:
            head = self.head
        if head is None:
            return 0
        i = self.get_k_to_last_helper(k, mook, head=head.next) + 1
        if i == k:
            mook.append(head.value)
        return i

    def get_k_to_last_iterative(self, k):
        mook = []
        self.get_k_to_last_helper(k, mook)
        return mook[0]

    def partition(self):
        if not self.head.next:
            # list length is one
            return
        i = self.head
        j = self.head.next
        while j:
            if j.value < self.head.value:
                i.next.value, j.value = j.value, i.next.value
                i = i.next
            j = j.next
        self.head.value, i.value = i.value, self.head.value


def delete_node(node):
    if not node.next:
        node = None
        return node
    node.value = node.next.value
    node.next = node.next.next
    return node


def add(lA, lB):
    digit, carry = helper([lA.head.value, lB.head.value])
    retlist = LinkedList(head=Node(digit))
    nA, nB = lA.head, lB.head
    retnode = retlist.head
    while nA.next and nB.next:
        nA, nB = nA.next, nB.next
        digit, carry = helper([nA.value, nB.value, carry])
        retnode.next = Node(digit)
        retnode = retnode.next
    # at least one has reached the end
    if nA.next:
        node = nA.next
    elif nB.next:
        node = nB.next
    else:
        retnode.next = Node(carry)
        return retlist
    while node:
        digit, carry = helper([node.value, carry])
        retnode.next = Node(digit)
        node = node.next
    return retlist


def helper(elems):
    result = 0
    for elem in elems:
        result = result + elem
    if result < 10:
        return result, 0
    return result % 10, math.floor(result / 10)


class ListLengthError(Exception):
    pass


class LastNodeError(Exception):
    pass


if __name__ == '__main__':
    node1, node2 = Node(3), Node(8)
    List1 = LinkedList(node1)
    List1.append(Node(5))
    List2 = LinkedList(node2)
    List2.append(Node(4))
    print("List1: {} List2: {} ".format(List1, List2))
    R = add(List1, List2)
    print(R)

