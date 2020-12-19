class Node:
    def __init__(self,data):
        self.data = data
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


    def inOrder(self):
        '''
        input: root from binary tree
        output: list with nodes' binary with the order: left -> root -> right
        '''
        if self.isEmpty():
            return 'the tree is empty'
        output = []
        def _walk(node):
            if (node.left):
                _walk(node.left)
            output.append(node.data)
            if (node.right):
                _walk(node.right)
        _walk(self.root)
        return output


    def postOrder(self):
        '''
        input: root from binary tree
        output: list with nodes' binary with the order: left -> right -> root
        '''
        if self.isEmpty():
            return 'the tree is empty'
        output = []
        def _walk(node):
            if (node.left):
                _walk(node.left)
            if (node.right):
                _walk(node.right)
            output.append(node.data)
        _walk(self.root)
        return output

        
    def contains(self,key):
        '''
        input: int
        output: bool (True if the key is exist in the tree,otherwise that ,return False)
        '''
        if self.isEmpty():
            return 'the tree is empty'

        # looping way
        '''        
        def _walk(root,key):
            while root:
                if root.data == key:
                    return True

                if root.data >= key:
                    return _walk(root.left,key)

                if root.data < key:
                    return _walk(root.right,key)

            return False
        return _walk(self.root,key)
        '''
        #recursion way
        def _walk(root,key):
            if root is None:
                return False

            if root.data == key :
                return True

            if root.data < key:
               return _walk(root.right,key)

            if root.data >= key:
                return _walk(root.left,key)

        return _walk(self.root,key) 

    @staticmethod
    def add(root, key): 
        if root is None:
            root = Node(key)
            return root 
        else: 
            if root.data < key: 
                root.right = BinaryTree.add(root.right, key) 
            else: 
                root.left = BinaryTree.add(root.left, key) 
        return root

if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(10)
    bt.root.left = Node(5)
    bt.root.left.left = Node(-1)
    bt.root.right.right = Node(15)
    bt.root.right.left = Node(7)
    print('pre order: ',bt.preOrder())
    print('in order : ',bt.inOrder())
    print('post order: ',bt.postOrder())
    print(bt.contains(0))
    bt.add(bt.root,0)
    print(bt.contains(0))
    print('pre order: ',bt.preOrder())
