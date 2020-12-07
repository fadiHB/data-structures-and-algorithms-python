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

    def kthFromEnd(self,k):
      current = self.head
      list_value = []
      while current:
        list_value.append(current.value)
        current = current.next
      reversed_list = list_value[::-1]
      if (k > len(reversed_list)):
          return 'the k is grater than list length'
      elif k < 0:
          return 'cant be negative number'
      return reversed_list[k]


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(10)
    ll.insert(5)
    print(ll.head.next.value)
    print(ll)