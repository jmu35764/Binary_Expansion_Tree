from collections import deque
from stack import Stack

class Binary_Expression_Tree():
    class _Node:
        def __init__(self, element, parent=None):
            self.element = element
            self.parent = parent
            self.left = None
            self.right = None
 
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node
 
        def element(self):
            return self._node.element
 
    def __init__(self, expression):
        self.expression = expression
        self.tree_stack = Stack()
        self._root = None

 
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
        if type(char) is int:
            return True

    def isOperator(self, char):
        #print(char, "Operator",type(char))
        if char in ('*', '+', '-', '/'):    
            return True

    def convert_expression(self)


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

    TreeType = LinkedBinaryTree
 
    tree = TreeType()
    a = tree.add_root("A")
    b = tree.add_left(a, "B")
    c = tree.add_right(a, "C")
    tree.add_left(b, "D")
    tree.add_right(b, "E")
    tree.add_left(c, "F")
    tree.add_right(c, "G")
 
    print(list(tree.preorder()))    # ['A', 'B', 'D', 'E', 'C', 'F', 'G']
    print(list(tree.inorder()))     # ['D', 'B', 'E', 'A', 'F', 'C', 'G']
    print(list(tree.postorder()))   # ['D', 'E', 'B', 'F', 'G', 'C', 'A']
    print(list(tree.level_order())) # ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    print(tree.depth(b))            # 1
    print(tree.height())            # 2

    print("\nBuilding tree from level-order list with None for empty slots:")
    values = ["A", "B", "C", "D", "E", "F", "G"]
    tree_from_list = TreeType.from_level_order(values)
    print("Preorder:", list(tree_from_list.preorder()))    # ['A', 'B', 'D', 'E', 'C', 'F', 'G']
    print("Inorder:", list(tree_from_list.inorder()))     # ['D', 'B', 'E', 'A', 'F', 'C', 'G']
    print("Postorder:", list(tree_from_list.postorder()))   # ['D', 'E', 'B', 'F', 'G', 'C', 'A']
    print("Level-order:", list(tree_from_list.level_order())) # ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    print("\nBuilding tree from level-order list with None for empty slots:")
    values = ["A", "B", "C", "D", None, "F"]

    tree = TreeType.from_level_order(values)
    print("Preorder:", list(tree.preorder()))  # ['A', 'B', 'D', 'C', 'F']
    print("Inorder:", list(tree.inorder()))   # ['D', 'B', 'A', 'F', 'C']
    print("Postorder:", list(tree.postorder())) # ['D', 'B', 'F', 'C', 'A']
    print("Level-order:", list(tree.level_order()))  # ['A', 'B', 'C', 'D', 'F']
