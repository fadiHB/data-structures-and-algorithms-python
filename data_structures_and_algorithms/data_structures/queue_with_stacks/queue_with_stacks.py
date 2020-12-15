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


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def peek(self):
        try:
            return self.front.data
        except AttributeError:
            return "the queue is already empty"

    def enqueue (self,data):
        node = Node(data)
        if self.rear:
            node.next = self.rear
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue (self):
        '''
        to remove data from the queue
        there are three status for that
        1- the queue is empty
        2- the queue have one value
        3 -the queue have mor thae one value
        '''
        if not self.rear:
            return('the queue is alreadt empty')
        if not self.rear.next:
            removed = self.rear.data
            self.rear = None
            return removed
        if self.rear.next:
            current = self.rear
            while current.next != self.front :
                current = current.next
            removed =  current.next.data
            current.next = None
            self.front = current
            return removed


class PseudoQueue :
    def __init__(self):
      self.stack1 = Stacks()
      self.stack2 = Stacks()


    def enqueu(self,data):
      self.stack1.push(data)

    def dequeue(self):

      if not self.stack1.top:
        return 'Ops .. the Stack is empty man !!'

      while self.stack1.top:
        self.stack2.push(self.stack1.pop())

      removed =  self.stack2.pop()

      while self.stack2.top:
        self.stack1.push(self.stack2.pop())
      
      return removed


if __name__ == "__main__":
  queue = PseudoQueue()

  queue.enqueu(1)
  queue.enqueu(2)
  queue.enqueu(3)
  queue.enqueu(4)

  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.dequeue())