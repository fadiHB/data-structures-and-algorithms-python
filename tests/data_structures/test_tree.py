from data_structures_and_algorithms.data_structures.tree.tree import Node,BinaryTree
import pytest

def test_preOrder(prep):
    actual = prep.preOrder()
    expected =[6, 5, -1, 10, 7, 15]
    assert actual == expected

def test_inOrder(prep):
    actual = prep.inOrder()
    expected = [-1, 5, 7, 15, 10, 6]
    actual = expected

def test_postOrder(prep):
    actual = prep.postOrder()
    expected = [-1, 5, 7, 15, 10, 6]
    actual = expected

def test_contains_true(prep):
    actual = prep.contains(5)
    expected = True
    actual = expected 

def test_contains_false(prep):
    actual = prep.contains(0)
    expected = False
    actual = expected 

def test_add(prep):
    actual = prep.add(prep.root,0)
    expected = [6, 5, -1, 0, 10, 7, 15]
    actual = expected

@pytest.fixture
def prep():
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(10)
    bt.root.left = Node(5)
    bt.root.left.left = Node(-1)
    bt.root.right.right = Node(15)
    bt.root.right.left = Node(7)
    return bt