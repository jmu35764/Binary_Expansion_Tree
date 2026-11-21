from stack import Stack
from collections import deque
from binary_expression_tree import Binary_Expression_Tree

def main():

    print("------ Expression to Tree Converter ------")    
    print("\nSingle Operator Expression")

    test_01 = Binary_Expression_Tree.expression_tree([3,8,'+'])
    print("Postfix Input: ", *test_01.expression)
    print("Fully Infix: ",*test_01.to_infix())
    print("Postfix Output: ", *test_01.postorder())
    print("Evaluated Result: ",*test_01.evaluate())
    
    print("\nMultiple Oprerator Expression")
    test_02 = Binary_Expression_Tree.expression_tree([5,3,8,'*','+'])
    print("Postfix Input: ", *test_02.expression)
    print("Fully Infix: ",*test_02.to_infix())
    print("Postfix Output: ", *test_02.postorder())
    print("Evaluated Result: ",*test_02.evaluate())

    print("\nNoncommutative Operator Expression: Subtraction")
    test_03 = Binary_Expression_Tree.expression_tree([8,2,'+',3,6,'*','-'])
    print("Postfix Input: ", *test_03.expression)
    print("Fully Infix: ",*test_03.to_infix())
    print("Postfix Output: ", *test_03.postorder())
    print("Evaluated Result: ",*test_03.evaluate())

    print("\nNoncommutative Operator Expression: Division")
    test_04 = Binary_Expression_Tree.expression_tree([5,3,8,'*','+',2,'/'])
    print("Postfix Input: ", *test_04.expression)
    print("Fully Infix: ",*test_04.to_infix())
    print("Postfix Output: ", *test_04.postorder())
    print("Evaluated Result: ",*test_04.evaluate())

    print("\nFloat Operator Expression")
    test_05 = Binary_Expression_Tree.expression_tree([5.5,3,8,'*','+',2,'/'])
    print("Postfix Input", *test_05.expression)
    print("Fully Infix: ",*test_05.to_infix())
    print("Postfix Output: ", *test_05.postorder())
    print("Evaluated Result: ",*test_05.evaluate())

    print("\nToo Many Operands Expression")
    test_06 = Binary_Expression_Tree.expression_tree([3,8, 5,'+'])

    print("\nToo Many Operators Expression")
    test_07 = Binary_Expression_Tree.expression_tree([3,8,'+', '-'])

    print("\nDivision by Zero Expression")
    test_08 = Binary_Expression_Tree.expression_tree([3,0,'/'])

    print("\nEmpty Operand Expression")
    test_09 = Binary_Expression_Tree.expression_tree([3,0,' '])

    print("\nInvalid Operand Expression")
    test_10 = Binary_Expression_Tree.expression_tree([3,0,';'])

if __name__ == "__main__":
    main()