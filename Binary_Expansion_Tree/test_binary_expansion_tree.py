import unittest
from stack import Stack
from binary_expression_tree import Binary_Expression_Tree

class TestBinaryExpressionTree(unittest.TestCase):

    def test_infix(self):
        test_01 = Binary_Expression_Tree.expression_tree([3,8,'+'])
        result = list(test_01.to_infix())
        evaluation = test_01.evaluate()
        self.assertEqual(result, ['(', 3, '+', 8, ')'])

    def test_addition(self):
        test_01 = Binary_Expression_Tree.expression_tree([3,8,'+'])
        result = list(test_01.to_infix())
        evaluation = test_01.evaluate()
        self.assertEqual(result, ['(', 3, '+', 8, ')'])
        self.assertEqual(list(test_01.evaluate()), [11])

    def test_nested_mixed_operators(self):
        test_01 = Binary_Expression_Tree.expression_tree([5,3,8,'*','+'])
        result = list(test_01.to_infix())
        evaluation = test_01.evaluate()
        self.assertEqual(result, ['(',5, '+','(', 3, '*', 8, ')', ')'])
        self.assertEqual(list(test_01.evaluate()), [29])

    def test_noncommutative_operators(self):
        test_01 = Binary_Expression_Tree.expression_tree([5,3,8,'*','+',2,'/'])
        result = list(test_01.to_infix())
        evaluation = test_01.evaluate()
        self.assertEqual(result, ['(','(',5, '+','(', 3, '*', 8, ')', ')', '/',2,')'])
        self.assertEqual(list(test_01.evaluate()), [14.5])

    def test_decimal_operand(self):
        test_01 = Binary_Expression_Tree.expression_tree([5,3,8,'*','+',2,'/'])
        result = list(test_01.to_infix())
        evaluation = test_01.evaluate()
        self.assertEqual(result, ['(','(',5, '+','(', 3, '*', 8, ')', ')', '/',2,')'])
        self.assertEqual(list(test_01.evaluate()), [14.5])

    def test_decimal_operand(self):
        test_01 = Binary_Expression_Tree.expression_tree([8,0,'/'])
        self.assertRaises(ZeroDivisionError)