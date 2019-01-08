
class InvalidOperator(Exception):
    """"""


class Tree(object):
    def __init__(self, primary):
        self.primary = primary
        self.children = []

    def __repr__(self):
        return "Tree object with primary {} and children {}".format(self.primary, self.children)

    def evaluate(self):
        if self.primary.isdigit():
            return int(self.primary)
        elif self.primary == '+':
            return self.add()
        elif self.primary == '*':
            return self.multiply()
        else:
            raise InvalidOperator

    def add(self):
        result = 0
        for elem in self.children:
            result = result + elem.evaluate()
        return result

    def multiply(self):
        result = 1
        for elem in self.children:
            result = result * elem.evaluate()
        return result

    @classmethod
    def build_tree(cls, tokens):
        if len(tokens) == 1:
            return cls(primary=tokens[0])
        stack = []
        for token in tokens:
            if token == '(':
                stack.append(cls(primary=None))
            elif token == ')':
                tree = stack.pop()
                if not stack:
                    # we've emptied the stack, so this paren matches the first
                    return tree
                else:
                    # we're not at the top level, so we need to put this tree as a child on the one above it
                    stack[-1].children.append(tree)
            elif token.isdigit():
                stack[-1].children.append(cls(primary=token))
            else:
                stack[-1].primary = token


if __name__ == '__main__':
    tree = Tree.build_tree('( * 3 ( + 2 3 ) )'.split(' '))
    print(tree)
    print(tree.evaluate())
