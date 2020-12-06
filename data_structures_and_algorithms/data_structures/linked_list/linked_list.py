# class LinkedList:
#     """
#     Put docstring here
#     """

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        # self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

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

    def __str__(self):
        current = self.head
        str1 = ''
        while current != None:
            str1 += f'{{ {current.value} }} -> '
            current = current.next
        str1 += 'NULL'
        return str1

    def append(self, num):
        node = Node(num)
        if (self.head is None):
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.next = None
            # node.prev = current
        self.size += 1

    def insertBefore(self, value, newVal):
        try:
            node = Node(newVal)
            if (self.head.value == value):
                self.insert(newVal)
            else:
                current = self.head
                while current:
                    if current.next.value == value:
                        node.next = current.next
                        current.next = node
                        break
                    current = current.next
                return('there is not number {newVal} in the linked-list')
            self.size += 1
        except Exception as error:
            print(f'error happened: {error}')
        

    def insertAfter(self, value, newVal):
        try:
            node = Node(newVal)
            if (self.head.value == value):
                self.insert(newVal)
            else:
                current = self.head
                while current:
                    if current.value == value:
                        node.next = current.next
                        current.next = node
                        break
                    else:
                        current = current.next
                return('there is not number {newVal} in the linked-list')
            self.size += 1
        except Exception as error:
            print(f'error happened: {error}')



if __name__ == '__main__':
    # ll = LinkedList()
    # ll.insert(10)
    # ll.insert(5)
    # print(ll.head.next.value)
    # print(ll)
    ll = LinkedList()
    ll.append(0)
    ll.append(3)
    ll.insertAfter(3,5)
    ll.__str__()
