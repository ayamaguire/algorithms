
class OperatorException(Exception):
    def __init__(self, message):
        self.message = message


class Tree(object):
    def __init__(self, operator=None, leaves=None):
        self.operator = operator
        self.leaves = leaves
        self.evaluation = None

    def __repr__(self):
        return "Tree with operator {} and leaves {}".format(self.operator, self.leaves)

    @classmethod
    def make_tree(cls, expr_list):
        """ turns a list into a tree object"""
        if len(expr_list) == 1:
            return NullTree(leaf=expr_list[0])
        operator = expr_list[0]
        current_leaves = expr_list[1:]
        new_leaves = []
        for leaf in current_leaves:
            new_leaves.append(Tree.make_tree(leaf))
        return cls(operator=operator, leaves=new_leaves)

    def evaluate(self):
        new_leaves = []
        for leaf in self.leaves:
            new_leaves.append(leaf.flatten())
        self.leaves = new_leaves
        if self.operator == '+':
            self.add()
        elif self.operator == '*':
            self.multiply()
        else:
            raise OperatorException("Unrecognized operator {}".format(self.operator))
        return self.evaluation

    def add(self):
        tree_sum = 0
        for item in self.leaves:
            tree_sum = tree_sum + int(item)
        self.evaluation = tree_sum

    def multiply(self):
        tree_product = 1
        for item in self.leaves:
            tree_product = tree_product * int(item)
        self.evaluation = tree_product


class NullTree(object):
    """ Represents a single int value"""
    def __init__(self, leaf=None):
        self.leaf = leaf

    def __repr__(self):
        return "Null tree representing {}".format(self.leaf)

    def evaluate(self):
        return int(self.leaf)


def get_sets(expr):
    """ finds how many layer one () there are, writes their location to the sets list"""
    stack = []
    psets = []
    for i, elem in enumerate(expr):
        if elem == '(':
            if not stack:
                psets.append([i])
            stack.append(0)
        elif elem == ')':
            stack.remove(0)
            if not stack:
                psets[-1].append(i)
    return psets


def parser(expr):
    """ want to turn '((A)(B))' into [[A], [B]] etc"""
    psets = get_sets(expr)
    if not psets:
        return expr

    prior = expr[:psets[0][0]]
    post = expr[psets[-1][1] + 1:]
    middle = expr[psets[-1][0] + 1:psets[-1][1]]
    parsed_middle = parser(middle)
    if not prior and not post:
        # we just have one open and close with nothing before or after, avoid extra []s
        return parsed_middle
    parsed = []
    for elem in prior:
        parsed.append(elem)

    for i, pset in enumerate(psets[:-1]):
        next = psets[i + 1]
        # recurse on what's in the paren
        parsed.append(parser(expr[pset[0]+1:pset[1]]))
        # add what's between parens
        between = expr[pset[1]+1:next[0]]
        if between:
            parsed.append(between)

    # and add whatever is in and after the last one
    parsed.append(parsed_middle)
    for elem in post:
        parsed.append(elem)
    return parsed


def math_parse(expr):
    """ Expects an expression like '( + 6 8 )'. Passes to parser."""
    parsed = expr.split(' ')
    parsed = parser(parsed)
    return parsed


if __name__ == "__main__":
    a = '( + ( * 2 3 ) ( * 2 4 ) 4 )'
    # a = '( * ( + 4 ( * 1 5 ) ) 3 )'
    parsed1 = math_parse(a)
    print(parsed1)
    tree = Tree.make_tree(parsed1)
    print("Tree: {}".format(tree))
    print(tree.evaluate())
