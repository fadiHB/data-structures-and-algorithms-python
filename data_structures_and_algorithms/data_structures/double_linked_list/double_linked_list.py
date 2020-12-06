class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class double_linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            node.prev = None
            self.head = node
        self.size += 1

    def includes(self, value):
        if self.head is None:
            return False
        else:
            current = self.head
            while current.value is not value:
                current = current.next
                # current.next = current.prev
                if current is None:
                    return False
            return True

    def __str__(self):
        current = self.head
        str1 = ''
        while current is not None:
            str1 += f'{{ {current.value} }} -> '
            current = current.next
        str1 += 'NULL'
        return str1

if __name__ == "__main__":
    dll = double_linked_list()
    dll.insert(0)
    dll.insert(5)
    dll.insert(10)
    dll.insert(15)
    print(dll.head.value)
    print(dll.__str__())
    print(dll.includes(7))