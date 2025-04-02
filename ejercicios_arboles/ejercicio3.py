class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None

    def build_tree(self, postfix_expr):
        stack = []
        for char in postfix_expr:
            if char.isdigit():  
                stack.append(Node(char))
            else:  
                node = Node(char)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        self.root = stack.pop()

    def evaluate(self, node=None):
        if node is None:
            node = self.root

        if node.left is None and node.right is None:  
            return int(node.value)
        
        left_val = self.evaluate(node.left)
        right_val = self.evaluate(node.right)

        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            return left_val / right_val

    def infix_expression(self, node=None):
        if node is None:
            node = self.root

        if node.left is None and node.right is None: 
            return node.value

        left_expr = self.infix_expression(node.left)
        right_expr = self.infix_expression(node.right)

        return f"({left_expr} {node.value} {right_expr})"

def create_expression_tree(postfix_expr):
    tree = ExpressionTree()
    tree.build_tree(postfix_expr)
    return tree


postfix_expr = "34+2*7/"
tree = create_expression_tree(postfix_expr)


result = tree.evaluate()
print("Resultado de la evaluación:", result)


infix = tree.infix_expression()
print("Expresión en notación infija:", infix)
