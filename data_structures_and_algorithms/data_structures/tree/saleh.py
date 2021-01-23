class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None 

def last_leaves (root):
    # temp = root.copy()
    output = []
    def _walk(root):
        if not root:
            return

        _walk(root.left)
        if root.left is None and  root.right is None:
            output.append(root.data)
        _walk(root.right)
        
    _walk(root)
    return output

def second_leavs(root):
    output = []
    if root.left:
        output.append(root.left.data)
    if root.right:
        output.append(root.right.data)

def breadth_first(root):
    output = []
    temp = []
    temp.append(root)
    while len(temp) > 0:
        popped = temp.pop(0)
        output.append(popped.data)
        if popped.left:
            temp.append(popped.left)
        if popped.right:
            temp.append(popped.right)
    return output


def print_spacific_level(root, x):
    if x <= 0 :
        return 'wrong level number'

    output = []
    temp = []
    temp.append(root)
    counter = 0
    while len(temp) > 0:
        poped = temp.pop(0)
        output.append(poped.data)
        if poped.left:
            temp.append(poped.left)
        if poped.right:
            temp.append(poped.right)
        counter += 0.5

        if counter == x:
            return output[:len(output)-1]

    return output

def find_max_min(root):
    max = root.data
    min = root.data
    def _walk(root):
        if root is None:
            return
        _walk(root.left)
        if root.data > max:
            max = root.data
        if root.data < min:
            min = root.data
        _walk(root.right)

    return {'max':max,'min':min}

# def sum_odd(root):
#     sum = 0
#     def _walk(root):
#         if root is None:
#             return
#         _walk(root.left)
#         if root.data % 2 != 0:
#             sum += root.data
#         _walk(root.right) 
#     _walk(root)
#     return sum

def find_the_path(root, x):
    lst = []

    def _walk(root,lst,x):
        lst.append(root.data)

        if root.data == x:
            return True

        if root.left and root.right :
            if _walk(root.left, lst, x) or _walk(root.right, lst, x):
                return True
        
        return False

    if _walk(root,lst,x):
        return lst
    return None

def depth_hight(root):
    if not root:
        return 0
    left_depth = depth_hight(root.left)
    right_depth = depth_hight(root.right)
    if left_depth > right_depth:
        hight = 1 + left_depth
    else:
        hight = 1 + right_depth

    return hight


def inOrder(root):
    output = []
    def _walk(root):
        if root is None:
            return
        _walk(root.left)
        output.append(root.data)
        _walk(root.right)
    _walk(root)
    return output

def is_mirror(root):
    left_sub_tree = inOrder(root.left)
    right_sub_tree = inOrder(root.right)
    return left_sub_tree == right_sub_tree[::-1]

if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(100)
    bt.root.left = Node(2)
    bt.root.left.left = Node(3)
    bt.root.left.left.right = Node(4)
    bt.root.left.left.right.left = Node(5)

    bt.root.right = Node(2)
    bt.root.right.right = Node(3)
    bt.root.right.right.left = Node(4)
    bt.root.right.right.left.right = Node(5)

    # print(inOrder(bt.root))
    print(print_spacific_level(bt.root, 3))
    # print(is_mirror(bt.root))
        
    



    


# if __name__ == "__main__":

#             100
#         50         30
#     20      60          70
    
# [20,50,60,100,30,70]

