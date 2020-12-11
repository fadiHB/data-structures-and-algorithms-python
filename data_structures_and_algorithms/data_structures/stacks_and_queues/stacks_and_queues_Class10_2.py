# from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues_Class10_1 import Node

class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
        self.prev = None

class Stacks:
    def __init__(self):
        self.top = None

    def push(self,data):
        '''
        method to add a new node to the stack
        '''
        node = Node(data)
        if self.top:
            node.prev = self.top
            node.next = self.top
        self.top = node


    def pop(self):
        if not self.top:
            return 'the stack is already empty ..!!'
        new_top = self.top.prev
        curret = self.top
        removed = self.top.data
        curret.prev = new_top
        self.top = new_top
        return removed

    def peek(self):
        if not self.top:
            return 'the stack is already empty ..!!'
        return self.top.data

    def isEmpty(self):
        if not self.top:
            return True
        return False
    
if __name__ == '__main__':
    my_stacks = Stacks()
    my_stacks.push(10)
    my_stacks.push(15)
    my_stacks.push(20)
    print(my_stacks.peek())
    print(my_stacks.pop())
    print(my_stacks.peek())
    print(my_stacks.isEmpty())


