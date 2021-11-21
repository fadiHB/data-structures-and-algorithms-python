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
        if root is None:    # check current
            root = Node(key)
            return root
        if root.data < key: # check befor go right
            root.right = BinaryTree.add(root.right, key) 
        else:               # check befor go left
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
    
    def breadth_first_2(tree: BinaryTree):
        if not tree.root:
            return None
        breadth = Queue()
        breadth.enqueue(tree.root)

        list_of_items = []

        while breadth.peek():
            front = breadth.dequeue()
            list_of_items += [front.data]

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)

        return list_of_items


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

        return array_to_bst(nodes)

    def array_to_bst(array_nums):
        if not array_nums:
            return None
        mid_num = len(array_nums)//2
        node = Node(array_nums[mid_num])
        node.left = array_to_bst(array_nums[:mid_num])
        node.right = array_to_bst(array_nums[mid_num+1:])
        return node

        
######################################################
# Given a binary search tree and a key,
# delete the key and returns the new root
# Delete a node from BST


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
# DELETE NODE FROM BT, NOT BST
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

    # find the rightmost node and the node that want to delete it.
    key_node = None
    q = [] 

    # 3 option here :
    # 1- append(root) -> to get the right/left most for the whole tree
    # 2- append(root.left) -> to get the right/left most for the left side of the tree
    # 3- append(root.right) -> to get the right/left most for the right side of the tree
    q.append(root)    

    while(len(q)): 
        temp = q.pop(0)             
        if temp.data == key:        
            key_node = temp         
        if temp.left:               
            q.append(temp.left)     # this order to get the right most
        if temp.right:              # to get the left mose
            q.append(temp.right)    # make swap between 345 and 347,on the other world,make the append.left at the last
    if key_node :  
        x = temp.data 
        deleteDeepest(root,temp) 
        key_node.data = x 
    return root

###################################################################################################
# hight depth from node: is how many nodes are there from the ground level to that node
# hight = 1 + number of edges for the longets path from the node to the ground level
# https://www.youtube.com/watch?v=_O-mK2g_jhI

# algorithm ( 3 main steps that shuld appley for each node)
#  maxDepth()
# 1. If tree is empty then return 0
# 2. Else
#      (a) Get the max depth of left subtree recursively  i.e., # step 1
#           call maxDepth( tree->left-subtree)
#      (a) Get the max depth of right subtree recursively  i.e., # step 2
#           call maxDepth( tree->right-subtree)
#      (c) Get the max of max depths of left and right  # step 3
#           subtrees and add 1 to it for the current node.
#          max_depth = max(max dept of left subtree,  
#                              max depth of right subtree) 
#                              + 1
#      (d) Return max_depth
def maxDepth(node): 
    if node is None: 
        return 0
    else : 
  
        # Compute the depth of left subtree 
        lDepth = maxDepth(node.left) #1

        # Compute the depth of right subtree 
        rDepth = maxDepth(node.right) #2

        # Use the larger one            #3
        if (lDepth > rDepth): 
            hight = 1 + lDepth
            return hight
        else: 
            hight = 1 + rDepth
            return hight
#######################################################################################################

# Check if two binary trees are Isomorphic

def Isomorphic(root1,root2):
    lst1 = root1.inOrder()
    lst2 = root2.inOrder()
    if len(lst1) == len(lst2):
        i = 0
        j = len(lst2)//2
        for k in range(len(lst1)//2):
            if lst1[i] != lst2[j]:
                return False
            i += 1
            j -= 1

            if i > j:
                return True
        return True
        
############################################################################################################

def find_the_path(root, x): 
      
    # vector to store the path  
    arr = []

    def _walk (root, arr, x):
        arr.append(root.data)

    # if it is the required node return true  
        if root.data == x:
            return True

        # else check whether the required node exists in the left subtree or right subtree of the current node  
        if _walk(root.left, arr, x) or _walk(root.right, arr, x):
            return True

        arr.pop(-1) # just to make space complexity O(1) 
        return False

    has_path = _walk(root, arr, x)

    if (has_path): 
        print(arr)
 
    else: 
        print("No Path")

###############################################################################################################
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
    print(bt.breadth_first() , 'hoooooon')
    print('-'*30)
    x = deletion(bt.root,5)
    print(bt.breadth_first())
    print('----- max depth ------')
    print(maxDepth(bt.root))

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
