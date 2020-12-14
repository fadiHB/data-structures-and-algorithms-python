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


class AnimalShelter:
    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()


    def enqueue(self):
        pass


class Animal:
    pass


class Cat(AnimalShelter):
    pass


class Dog(AnimalShelter):
    pass



if __name__ == "__main__":
    pass