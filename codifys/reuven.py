
class ParserException(Exception):
    """General exception for the parse problem"""
    def __init__(self, message):
        self.message = message


class OperatorException(ParserException):
    """ Bad operator given to tree"""


class InvalidParensException(ParserException):
    """ Invalid parens, like )("""


class Tree(object):
    def __init__(self, operator=None, leaves=None):
        self.operator = operator
        self.leaves = leaves
        self.evaluation = None

    def __repr__(self):
        return "Tree with operator {} and leaves {}".format(self.operator, self.leaves)

    def evaluate(self):
        for leaf in self.leaves:
            if isinstance(leaf, Tree):
                leaf.evaluate()
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
        return [expr]

    # add whatever comes before the first paren
    parsed = []
    prior = expr[:psets[0][0]]
    if prior:
        parsed.append(prior)

    for i, pset in enumerate(psets[:-1]):
        next = psets[i + 1]
        # recurse on what's in the paren
        parsed.append(parser(expr[pset[0]+1:pset[1]]))
        # add what's between parens
        between = expr[pset[1]+1:next[0]]
        if between:
            parsed.append(between)

    # and add whatever is in and after the last one
    parsed.append(parser(expr[psets[-1][0] + 1:psets[-1][1]]))
    post = expr[psets[-1][1]+1:]
    if post:
        parsed.append(post)
    return parsed


def math_parse(expr):
    """ Expects an expression like '( + 6 8 )'. Passes to parser."""
    parsed = parser(expr)
    empty = []
    for i, elem in enumerate(parsed):
        if isinstance(elem, str):
            elem.strip()
        if not elem:
            empty.append(i)
    for elem in empty:
        parsed.pop(elem)
    return parsed


if __name__ == "__main__":
    print(math_parse('+ ( + 6 8 ) ( * 5 ( + 2 5 ) )'))

