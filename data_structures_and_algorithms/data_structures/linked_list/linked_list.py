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

    def insertBefore(self, n, k):
            node = Node(n)

            if not self.head:
                self.head = node
                return

            if k == self.head.value :
                self.insert(k)
                return

            temp = self.head
            while temp:
                if temp.next.value == k:
                    node.next = temp.next
                    temp.next = node
                    return
                temp = temp.next

            self.append(n)

    def insert_after(self,n,k):
        node = Node(n)

        if not self.head:
            self.head = node
            return

        if k == self.head.value:
            self.append(n)
            return

        temp = self.head
        while temp:
            if temp.value == k:
                node.next = temp.next
                temp.next = node
                return
            temp = temp.next

        self.append(n)

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
            return 'your data in not inclde in the linked_list to deleted'

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

    # not checked yet
    def deleteDuplicates(self):
        temp = self.head
        lst = set()
        while temp:
            set.add(temp.value)
            temp = temp.next
        return lst

    def reverse(self):
        prev = None
        current = self.head
        while not current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def __str__(self):
        current = self.head
        str1 = ''
        while current != None:
            str1 += f'{{ {current.value} }} -> '
            current = current.next
        str1 += 'NULL'
        return str1

    def palind(self):
        list2 = []
        current =self.head
        while current:
            list2.append(current.value)
            current= current.next

        isPalind =True
        while current: # take from the first
            value= list2.pop() # take from the last
            if current.value == value :#compair between the first and the last
                isPalind = True
            else:
                return False
            current = current.next
        return isPalind


# Function to merge the lists 
# Takes two lists which are sorted 
# joins them to get a single sorted list 
def marge_sorted_list(ll1, ll2):
    headA = ll1.head
    headB = ll2.head
    # A dummy node to store the result
    dummyNode = Node(0)
  
    # Tail stores the last node 
    tail = dummyNode
    while True:
  
        # If any of the list gets completely empty 
        # directly join all the elements of the other list 
        if  not headA: 
            tail.next = headB 
            break
        if not headB: 
            tail.next = headA 
            break
  
        # Compare the data of the lists
        ## append the smaller one to the last of the marged list
        ## update the head
        if headA.value <= headB.value: 
            tail.next = headA 
            headA = headA.next
        else: 
            tail.next = headB 
            headB = headB.next

        # update
        # Advance the tail # 
        # very important setp
        tail = tail.next
  
    # Returns the head of the merged list 
    return dummyNode.next


def zip_lists(list1,list2):
    """
    this function , is takes two linked list
    and returned a new linked list-withc is merged of the two before
    """
    current_one = list1.head  
    current_two = list2.head
    if not current_one:
        return list2

    if not current_two:
        return list1

    new_list = LinkedList()
    while current_one or current_two:#  False or False = False
        
        # check the head of the marged list if it None or not
        ## True  -> add the node to the bigeneng of the marger_lit
        ## False -> add the node to the last of the marged_list
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

        # update
        if current_one and current_one.next:
            current_one = current_one.next
        else:
            current_one= False

        if current_two and current_two.next:
            current_two = current_two.next
        else:
            current_two=False

    return new_list



if __name__ == '__main__': 
    ll1 = LinkedList()
    ll1.append(30)
    ll1.append(20)
    ll1.append(10)
    ll2 = LinkedList()
    ll2.append(3)
    ll2.append(2)
    ll2.append(1)
    # print(ll1)
    # print(ll1.__str__())
    # print(ll2.size)
    # print(ll2.find_middel())
    # ll2.insertBefore('A',2)
    # print(ll2.__str__())
    # print(ll2.__str__())
    print(zip_lists(ll1,ll2))
    # print(marge_sorted_list(ll1,ll2))
    # ll1.reverse
    # print(ll1.__str__())
    
    


    