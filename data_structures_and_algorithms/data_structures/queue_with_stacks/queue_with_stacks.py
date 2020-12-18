# from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues_Class10_1 import Queue
# from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues_Class10_2 import Stacks,Node
class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
        self.prev = None

class Stacks:
    def __init__(self):
        self.top = None

    def push(self,data):
        node = Node(data)
        if self.top:
            node.prev = self.top
            node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            return 'the stack is already empty ..!!'
        removed = self.top.data
        self.top = self.top.next
        return removed

    def peek(self):
        if not self.top:
            return 'the stack is already empty ..!!'
        return self.top.data

    def isEmpty(self):
        return self.top == None

class PseudoQueue :
    def __init__(self):
      self.stack1 = Stacks()
      self.stack2 = Stacks()

    def enqueu(self,data):
      self.stack1.push(data)

    def dequeue(self):
      if self.stack1.isEmpty():
        return 'Ops .. the Stack is empty man !!'

      while self.stack1.top:
        self.stack2.push(self.stack1.pop())

      removed =  self.stack2.pop()

      while self.stack2.top:
        self.stack1.push(self.stack2.pop())
      
      return removed

if __name__ == "__main__":
    pass