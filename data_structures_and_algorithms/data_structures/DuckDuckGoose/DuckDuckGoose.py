class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top == None

    def peek(self):
        return self.top.data

    def push(self,data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            return temp.data
        self.size -= 1
        return 'stack is empty'

# def DuckDuckGoose(s1,k):
#     counter = 0
#     s2 = Stack()
#     s1_size = s1.size

#     print('start fun _ s1_size = ',s1.size)
#     print('start fun _ s2_size = ',s2.size)

#     for i in range(s1_size):
#         counter += 1
#         if counter == k:
#             s1.pop()
#             continue
#         s2.push(s1.pop())

#     print('after for 1_ s1_size = ',s1.size)
#     print('after for 1_ s2_size = ',s2.size)

#     for i in range(s2.size):
#         s1.push(s2.pop())

#     print('after for 2 _ s1_size = ',s1.size)
#     print('after for 2_ s2_size = ',s2.size)
#     print('-'*50)

#     if s1.size != 1:
#         DuckDuckGoose(s1,k)
#     return s1.top.data


# def DuckDuckGoose2 (lst,k):
#     lst_left = []
#     lst_right = []

#     for i in range(len(lst)):
#         if i+1 == k:
#             lst[i] = None
#             lst_left = lst[lst[i]:]
#             lst_right = lst[:lst[i]]
#         break
            
#     new_lst = lst_left + lst_right
#     print(new_lst)

def DuckDuckGoose3(lst,k): 

    len_list = (len(lst)) 
    pos = k - 1
    index = 0

    while len_list > 1:  

        index = (pos + index) % len_list
        lst.pop(index)
        len_list -= 1

    return lst[0]

        
  
if __name__ == '__main__':
    s1 = Stack()
    lst = ['A','B','C','D','E']
    for i in lst:
        s1.push(i)
    # print(DuckDuckGoose(s1,3))
    # print(s1.peek())
    # print(s1.peek())
    # DuckDuckGoose2(lst,3)
    # removeThirdName(lst,3)
    print(lst)
    print(DuckDuckGoose3(lst,3))


