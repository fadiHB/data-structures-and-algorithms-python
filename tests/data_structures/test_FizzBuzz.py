from data_structures_and_algorithms.data_structures.fizz_buzz_tree.fizz_buzz_tree import FizzBuzzTree,BinaryTree,Node

def test_fizz_buzz ():
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(10)
    bt.root.left = Node(5)
    bt.root.left.left = Node(7)
    bt.root.right.right = Node(15)
    bt.root.right.left = Node(20)

    bt2 = BinaryTree()
    root2 = FizzBuzzTree(bt.root)
    bt2.root = root2

    assert bt2.preOrder() == ['Fizz', 'Buzz', '7', 'Buzz', 'Buzz', 'FizzBuzz']


