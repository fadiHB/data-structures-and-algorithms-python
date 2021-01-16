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
        if root.data < key: 
            root.right = BinaryTree.add(root.right, key) 
        else: 
            root.left = BinaryTree.add(root.left, key) 
        return root

    def find_maximum_value(self):
        self.max_number = 0
        def _walk(node):
            if node.data > self.max_number:
                self.max_number = node.data
            if node.right:
                _walk(node.right)
            if node.left:
                _walk(node.left)
            return
        _walk(self.root)
        return self.max_number

    def find_minimum_value(self):
        self.min_number = 0
        def _walk(node):
            if node.data < self.min_number:
                self.min_number = node.data
            if node.right:
                _walk(node.right)
            if node.left:
                _walk(node.left)
            return
        _walk(self.root)
        return self.min_number

    def breadth_first(self):
        if self.isEmpty():
            return 'tree is empty'
        temp = []
        output = []
        temp.append(self.root)
        
        while len(temp) > 0:
            poped = temp.pop(0)
            output.append(poped.data)
            if poped.left:
                temp.append(poped.left)
            if poped.right:
                temp.append(poped.right)
        
        return output    


# Convert a array to Binary Search Tree (BST)

# def array_to_bst(array_nums):
#     if not array_nums:
#         return None
#     bst = BinaryTree()
#     mid_num = len(array_nums)//2
#     bst.root = Node(array_nums[mid_num])
#     bst.root.left = array_to_bst(array_nums[:mid_num])
#     bst.root.right = array_to_bst(array_nums[mid_num+1:])
#     return bst
def array_to_bst(array_nums):
    if not array_nums:
        return None
    mid_num = len(array_nums)//2
    node = Node(array_nums[mid_num])
    node.left = array_to_bst(array_nums[:mid_num])
    node.right = array_to_bst(array_nums[mid_num+1:])
    return node

def preOrder(node): 
    if not node: 
        return      
    print(node.data)
    preOrder(node.left) 
    preOrder(node.right)

################################################      
# Convert a skewed BST to Balanced BST
# to convert the bt to bst , do the same,but dont forget to sort the list
# cause the big idea is to have a sorted of nodr's list and make a new tree

def normalBST_to_balanceBST(root):

    # 1 : traverls (in order)and get all nodes from the skewed binary tree and append them to nodes's list
    nodes = []
    def storeBSTNodes(root,nodes): 
        if not root: 
            return 
        storeBSTNodes(root.left,nodes) 
        nodes.append(root) 
        storeBSTNodes(root.right,nodes)

    # Recursive function to construct binary tree  
    def buildTreeUtil(nodes,start,end): 
        if start>end: 
            return None
    
        # Get the middle element and make it root  
        mid=(start+end)//2
        node=nodes[mid]
    
        # Using index in Inorder traversal, construct  
        # left and right subtress 
        node.left=buildTreeUtil(nodes,start,mid-1) 
        node.right=buildTreeUtil(nodes,mid+1,end) 
        return node


    storeBSTNodes(root,nodes) 
    n=len(nodes) 
    return buildTreeUtil(nodes,0,n-1)
        
######################################################
# Given a binary search tree and a key,
# delete the key and returns the new root


def minValueNode (node):
    current = node
 
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
 
    return current
 
def deleteNode(root, key):
 
    # Base Case
    if root is None:
        return root
 
    # If the key to be deleted 
    # is smaller than the root's
    # key then it lies in  left subtree
    if key < root.data:
        root.left = deleteNode(root.left, key)
 
    # If the kye to be delete 
    # is greater than the root's key
    # then it lies in right subtree
    elif(key > root.data):
        root.right = deleteNode(root.right, key)
 
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
 
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp # new root
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp # new
 
        # Node with two children: 
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)
 
        # Copy the inorder successor's 
        # content to this node
        root.data = temp.data
 
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.data)
 
    return root

##############################################################
# https://www.geeksforgeeks.org/deletion-binary-tree/
# Algorithm 
# 1. Starting at root, find the deepest and rightmost node in binary tree and node which we want to delete. 
# 2. Replace the deepest rightmost node’s data with node to be deleted. 
# 3. Then delete the deepest rightmost node.

# function to delete the given deepest node (d_node) in binary tree  
def deleteDeepest(root,d_node): 
    q = [] 
    q.append(root) 
    while(len(q)): 
        temp = q.pop(0) 
        if temp is d_node: 
            temp = None
            return
        if temp.right: 
            if temp.right is d_node: 
                temp.right = None
                return
            else: 
                q.append(temp.right) 
        if temp.left: 
            if temp.left is d_node: 
                temp.left = None
                return
            else: 
                q.append(temp.left) 
   
# function to delete element in binary tree  
def deletion(root, key): 
    if root == None : 
        return None
    if root.left == None and root.right == None: 
        if root.key == key :  
            return None
        else : 
            return root 
    
    # find the target node / log(n)
    key_node = None
    def _walk(root):
        if root.data == key:
            return root
        if root.left:
            return _walk(root.left)
        if root.right:
            return _walk(root.right)
        return None
    key_node = _walk(root)

    if not key_node:
        return 'the node does not exist'

    # find the deepest and rightmost node
    right_most = root
    while right_most.right:
        right_most = right_most.right.right

    save_right_most_data = right_most.data 
    # deleteDeepest(root,right_most)
    while root:
        if root.right == None:
            root = None
            break
        root = root.right
    key_node.data = save_right_most_data 

    return root 
##############################################################


if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(10)
    bt.root.left = Node(5)
    bt.root.left.left = Node(-1)
    bt.root.right.right = Node(15)
    bt.root.right.left = Node(20)
    print('pre order: ',bt.preOrder())
    print('in order : ',bt.inOrder())
    print('post order: ',bt.postOrder())
    # print(bt.contains(0))
    # bt.add(bt.root,0)
    # print(bt.contains(0))
    # print('pre order: ',bt.preOrder())
    print(bt.find_maximum_value())
    print(bt.find_minimum_value())
    print(bt.breadth_first())
    print('-'*30)
    x = deletion(bt.root,5)
    print(bt.breadth_first())

    # lst = [1,2,3,4]
    # lst.sort()
    # print(lst)
    # tree_1 = array_to_bst(lst)
    # print(preOrder(tree_1))

    # print('-'*30)
    # root = Node(10) 
    # root.left = Node(8) 
    # root.left.left = Node(7) 
    # root.left.left.left = Node(6) 
    # root.left.left.left.left = Node(5) 
    # root = normalBST_to_balanceBST(root) 
    # print("Preorder traversal of balanced BST is :") 
    # preOrder(root) 