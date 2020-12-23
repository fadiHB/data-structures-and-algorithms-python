# from data_structures_and_algorithms.data_structures.tree.tree import Node, BinaryTree

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None 

    def isEmpty(self):
        return self.root == None

    def preOrder(self):
        '''
        input: root from binary tree
        output: list with nodes' binary with the order: root -> left -> right
        '''
        if self.isEmpty():
            return 'the tree is empty'
        output = []
        def _walk(node):
            output.append(node.data)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
        
        _walk(self.root)
        return output


def FizzBuzzTree(root):
    '''
    input: root from binary tree
    output: list with nodes' binary with the order: root -> left -> right
    '''
    root2 = root

    def _walk(node,node2):
        if node.data:
            if node.data % 3 == 0 and  node.data % 5 == 0:
                node2.data = 'FizzBuzz'
            elif node.data % 3 == 0:
                node2.data = 'Fizz'
            elif node.data % 5 == 0:
                node2.data = 'Buzz'
            else:
                node2.data = str(node.data)
        if node.left:
            _walk(node.left,node2.left)
        if node.right:
            _walk(node.right,node2.right)

    _walk(root,root2)
    return root2


if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(10)
    bt.root.left = Node(5)
    bt.root.left.left = Node(7)
    bt.root.right.right = Node(15)
    bt.root.right.left = Node(20)
    print(bt.preOrder())
    root2 = FizzBuzzTree(bt.root)
    bt2 = BinaryTree()
    bt2.root = root2
    print(bt2.preOrder())
    # print(bt.preOrder())
