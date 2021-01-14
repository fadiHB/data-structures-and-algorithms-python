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
        if not self.rear and not self.front:
            self.front = node
            self.rear = node
        temp = self.rear
        self.rear = node
        temp.next = self.rear
        
    def dequeue (self):

        if self.front:
            temp = self.front.data
            self.front = self.front.next
            return temp
        return 'the queue is alreadt empty'





class Cat():
     def __init__(self,name):
        self.name = name
        self.kind = 'cat'

class Dog():
    def __init__(self,name):
        self.name = name
        self.kind = 'dog'


class AnimalShelter:
    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()


    def enqueue(self,animal):
        if animal.kind == 'cat':
            self.cat_queue.enqueue(animal)
            
        if animal.kind == 'dog':
            self.dog_queue.enqueue(animal)
            
    
    def dequeue (self,kind):

        #Stretch Goal
        if (not self.cat_queue.front) and (not self.dog_queue.front):
            return "the cat's queue and the dog's queue are both empty"

        if kind == 'cat':

            #Stretch Goal
            if (self.cat_queue.front == None) and (self.dog_queue.front):
                dog = self.dog_queue.dequeue()
                msg = f'cat queue is empty, here is a dog : {dog.name}'
                return msg
            cat = self.cat_queue.dequeue()
            return cat.name

        elif kind == 'dog':

            #Stretch Goal
            if (self.dog_queue.front == None) and (self.cat_queue.front):
                cat = self.cat_queue.dequeue()
                msg = f'cat queue is empty, here is a cat : {cat.name}'
                return msg            
            dog = self.dog_queue.dequeue()
            return dog.name

if __name__ == "__main__":
    alex = Dog('alex')
    aln = Dog('Aln')
    sam = Dog('Sam')
    cray = Dog('Cray')
    soso = Cat('Soso')
    sno = Cat('Son')
    animals = AnimalShelter()
    animals.enqueue(alex)
    animals.enqueue(aln)
    animals.enqueue(sam)
    animals.enqueue(cray)
    animals.enqueue(soso)
    animals.enqueue(sno)
    animals.dequeue('cat')
    animals.dequeue('dog')
    animals.dequeue('dog')
    animals.dequeue('dog')