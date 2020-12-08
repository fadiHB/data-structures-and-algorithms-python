# class LinkedList:
#     """
#     Put docstring here
#     """

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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

    def zipLists(self, list1, list2):



        primary_current = list1.head
        second_current = list2.head

        while primary_current and second_current :

            primary_current.next  = second_current#
            second_current.next = primary_current.next.next#

            # second_current.next.next = primary_current
            # primary_current.next.next = second_current 

            return list1


if __name__ == '__main__':
    # ll = LinkedList()
    # ll.insert(10)
    # ll.insert(5)
    # print(ll.head.next.value)
    # print(ll)
    ll1 = LinkedList()
    ll1.insert(1)
    ll1.insert(2)
    ll1.insert(3)
    ll2 = LinkedList()
    ll2.insert(1)
    ll2.insert(2)
    ll2.insert(3)
    ll3 = LinkedList()
    ll2.zipLists(ll1,ll2)
    print(ll1.__str__())


    