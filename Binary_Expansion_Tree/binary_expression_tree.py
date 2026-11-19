from collections import deque
from stack import Stack

class Binary_Expression_Tree:
    class _Node:
        def __init__(self, element, parent=None):
            self.element = element
            self.parent = parent
            self.left = None
            self.right = None

        def attatch(self, left, right):
            #self.parent  = parent
            self.left = left
            self.right = right
 
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node
 
        def element(self):
            return self._node.element
 
    def __init__(self):
        #self.expression = expression
        self._root = None
        self._num_node = None

 
    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None
 
    def _validate(self, p):
        if not isinstance(p, self.Position) or p._container is not self:
            raise ValueError("Position does not belong to this tree")
        return p._node
 
    def root(self):
        return self._make_position(self._root)
 
    def parent(self, p):
        return self._make_position(self._validate(p).parent)
 
    def left(self, p):
        return self._make_position(self._validate(p).left)
 
    def right(self, p):
        return self._make_position(self._validate(p).right)
 
    def is_leaf(self, p):
        n = self._validate(p)
        return n.left is None and n.right is None
 
    def add_root(self, element):
        if self._root is not None:
            raise ValueError("Root already exists")
        self._root = self._Node(element)
        return self.root()

    def add_node(self, element):
        node = self._Node(element)
        return node

    def attatch_subtree(self, p, left, right):
        #self.add_left(p, left)
        #self.add_right(p, right)
        p.left = left
        p.right = right


    def add_left(self, p, element):
        n = self._validate(p)
        if n.left is not None:
            raise ValueError("Left child already exists")
        n.left = self._Node(element, n)
        return self._make_position(n.left)
 
    def add_right(self, p, element):
        n = self._validate(p)
        if n.right is not None:
            raise ValueError("Right child already exists")
        n.right = self._Node(element, n)
        return self._make_position(n.right)


    def isOperand(self, char):
        #print(char, "Operand",type(char))
        #if isinstance(char, float):
        if type(char) is int or type(char) is float:
            return True

    def isOperator(self, char):
        #print(char, "Operator",type(char))
        if char in ('*', '+', '-', '/'):    
            return True

    #def convert_expression(self)


    @classmethod
    def from_level_order(cls, values):
        """Build a tree from indexed level-order slots; None means empty."""
        tree = cls()
        positions = {}
        for i, value in enumerate(values):
            if value is None:
                continue
            if i == 0:
                position = tree.add_root(value)
            else:
                parent_index = (i - 1) // 2
                if parent_index not in positions:
                    raise ValueError("Nonempty node has a missing parent")
                parent = positions[parent_index]
                if i % 2 == 1:
                    position = tree.add_left(parent, value)
                else:
                    position = tree.add_right(parent, value)
            positions[i] = position
        return tree

    @classmethod
    def expression_tree(cls, expression):

        tree = cls()
        Tree_stack = Stack()

        for char in expression:
            if isinstance(char, int) or isinstance (char, float):
                num_node = tree.add_node(char)
                Tree_stack.push(num_node)
                print(Tree_stack.peek().element)

            if tree.isOperator(char):
                if Tree_stack.size() > 1:
                    right = Tree_stack.pop()
                    left = Tree_stack.pop()
                    op_node = tree.add_node(char)
                    tree.attatch_subtree(op_node, left, right)
                    Tree_stack.push(op_node)
                    print(Tree_stack.peek().element)

        if Tree_stack.size() == 1:
            #print(Tree_stack.peek().left.element)
            root_test = Tree_stack.pop()
            tree._root = root_test
            print(root_test.element)
            

        return tree

    def preorder(self):
        def visit(p):
            if p is not None:
                yield p.element()
                yield from visit(self.left(p))
                yield from visit(self.right(p))
        yield from visit(self.root())
 
    def inorder(self):
        def visit(p):
            if p is not None:
                yield from visit(self.left(p))
                yield p.element()
                yield from visit(self.right(p))
        yield from visit(self.root())
 
    def postorder(self):
        def visit(p):
            if p is not None:
                yield from visit(self.left(p))
                yield from visit(self.right(p))
                yield p.element()
        yield from visit(self.root())
 
    def level_order(self):
        q = deque([self.root()]) if self.root() is not None else deque()
        while q:
            p = q.popleft()
            yield p.element()
            for child in (self.left(p), self.right(p)):
                if child is not None:
                    q.append(child)
 
    def depth(self, p):
        self._validate(p)
        distance = 0
        while self.parent(p) is not None:
            p = self.parent(p)
            distance += 1
        return distance
 
    def height(self, p=None):
        if p is None:
            p = self.root()
        else:
            self._validate(p)
        if p is None:
            return -1  # empty tree/subtree, edge-count convention
        return 1 + max(self.height_child(self.left(p)),
                       self.height_child(self.right(p)))
 
    def height_child(self, p):
        return -1 if p is None else self.height(p)

if __name__ == "__main__":

    
    test_01 = Binary_Expression_Tree.expression_tree([3,8,'+'])
    print(list(test_01.inorder()))
    
    test_02 = Binary_Expression_Tree.expression_tree([5,3,8,'*','+'])
    print(list(test_02.inorder()))

