# from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues_Class10_1 import Node

class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
        self.prev = None

class Stacks:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def push(self,data):
        '''
        method to add a new node to the stack
        '''
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        self.top = node


    def pop(self):
        if self.isEmpty():
            return 'the stack is already empty ..!!'
        removed = self.top.data
        self.top = self.top.next
        return removed

    def peek(self):
        if self.isEmpty():
            return 'the stack is already empty ..!!'
        return self.top.data

    
if __name__ == '__main__':
    my_stacks = Stacks()
    my_stacks.push(10)
    my_stacks.push(15)
    my_stacks.push(20)
    print(my_stacks.peek())
    print(my_stacks.pop())
    print(my_stacks.peek())
    print(my_stacks.isEmpty())


