# class LinkedList:
#     """
#     Put docstring here
#     """

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"{self.value} -> {self.next} "


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = -1

    def insert(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def append (self,value):
        node = Node(value)
        current = self.head
        if current == None:
            self.insert(value)
        else:
            while current.next:
                current = current.next
            current.next = node
            node.next = None
        self.size += 1

    # not works yet
    def insert_befor(self,n,k):
        if k ==  None:
            return 'k is none'
        if k == self.head.value:
            self.insert(k)
            return
        temp = self.head
        while temp:
            if temp.next.next.value == k:
                node = Node(n)
                node.next = temp.next.next
                temp.next.next = node
                return
        self.append(k)
     

    def insert_after(self,n,k):
        if k ==  None:
            return 'k is none'
        if k == self.head.value:
            self.insert(k)
            return
        temp = self.head
        while temp:
            if temp.value == k:
                node = Node(n)
                node.next = temp.next
                temp.next = node
                return
            temp = temp.next
        self.append(k)

    # not worked yet
    def delete(self,k):
        temp = self.head

        # best case _ the k in the head
        if temp:
            if temp.value == k:
                self.head = temp.next
                temp = None
                return
    
        # looping through the linked_list
        while temp:
            if temp.value == k:
                break
            prev = temp
            temp = temp.next

        # if we reach to the end of the linked list, without any match !
        if temp == None:
            return 'your data in so inclde in the linked_list to deleted'

        prev.next = temp.next
        temp = None


    def find_middel(self):
        if not self.head:
            return False
        counter = 0
        temp = self.head
        while counter != self.size // 2:
            temp = temp.next
            counter += 1
        return temp.value
         
    def includes(self, value):
        # node = Node(self.head)
        if self.size == 0:
            return False
        else:
            current = self.head
            while current != None:
                if current.value == value:
                    return True
                current = current.next
            return False

    def deleteDuplicates(self):
        temp = self.head
        while not temp and not temp.next:
            if temp.next.value == temp.value:
                temp.next = temp.next.next
            temp = temp.next

    def __str__(self):
        current = self.head
        str1 = ''
        while current != None:
            str1 += f'{{ {current.value} }} -> '
            current = current.next
        str1 += 'NULL'
        return str1



def zip_lists(list1,list2):
    """
    this function , is takes two linked list
    and returned a new linked list-withc is merged of the two before
    """
    current_one = list1.head  
    current_two = list2.head
    if current_one == None:
        return print(list2)

    if current_two == None:
        return print(list1)

    new_list = LinkedList()
    while current_one or current_two:
        if current_one:
            if new_list.head == None:
                new_list.insert(current_one.value)
            else:
                new_list.append(current_one.value)
        if current_two:
            if new_list.head == None:
                new_list.insert(current_two.value)
            else:
                new_list.append(current_two.value)

        if current_one and current_one.next:
            current_one = current_one.next
        else:
            current_one= False

        if current_two and current_two.next:
            current_two = current_two.next
        else:
            current_two=False


    return new_list

    
# def ll_zip(list1,list2):
#     current_one = list1.head  
#     current_two = list2.head
#     print(current_one)
#     print(current_two)

#     if current_one == None:
#         return list2
    
#     if current_two == None:
#         return list1

#     while  current_one and current_two:
#         temp1 = current_one.next
#         temp2 = current_two.next
        
#         current_one.next = current_two
#         current_two.next = temp1

#         current_one = temp1
#         current_two = temp2
#         # if not current_one.next :
#         #     while current_two:
#         #         temp = current_one
#         #         temp.next = current_two
#         #         current_two = current_two.next
#         #         temp = current_two
#         #     return list1
#     return list1




if __name__ == '__main__': 
    ll1 = LinkedList()
    ll1.append(3)
    ll1.append(2)
    ll1.append(1)
    ll2 = LinkedList()
    ll2.append(3)
    ll2.append(2)
    ll2.append(1)
    # print(ll1)
    print(ll2.__str__())
    print(ll2.size)
    print(ll2.find_middel())
    ll2.insert_befor('A',2)
    print(ll2.__str__())
    # print(ll2.__str__())
    # print(zip_lists(ll1,ll2))
    


    