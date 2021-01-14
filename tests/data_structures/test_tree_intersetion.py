# from data_structures_and_algorithms.data_structures.tree.tree_intersection.tree_intersection import Node, BinaryTree, tree_intersection

import pytest


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None 

    def preOrder(self):
        '''
        input: root from binary tree
        output: list with nodes' binary with the order: root -> left -> right
        '''
        output = []
        def _walk(node):
            output.append(node.data)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
        
        _walk(self.root)
        return output

def tree_intersection(bt1,bt2):
    data1 = bt1.preOrder()
    data2 = bt2.preOrder()
    common_data = []
    for i in data1:
        if i in data2:
            common_data.append(i)
    return common_data

def test_tree_intersection(prep):
    actual = tree_intersection(prep[0],prep[1])
    expected = [6, -1, 20]
    assert actual == expected


@pytest.fixture
def prep():
    bt1 = BinaryTree()
    bt1.root = Node(6)
    bt1.root.right = Node(10)
    bt1.root.left = Node(5)
    bt1.root.left.left = Node(-1)
    bt1.root.right.right = Node(15)
    bt1.root.right.left = Node(20)

    bt2 = BinaryTree()
    bt2.root = Node(6)
    bt2.root.right = Node(20)
    bt2.root.left = Node(1)
    bt2.root.left.left = Node(-1)
    bt2.root.right.right = Node(30)
    bt2.root.right.left = Node(20)

    return [bt1,bt2]
    