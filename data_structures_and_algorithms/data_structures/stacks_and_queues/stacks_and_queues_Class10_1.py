class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

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

    def isEmpty(self):
        if self.rear:
            return False
        return True
            
if __name__ == '__main__':
    my_queue = Queue()
    my_queue.enqueue(0)
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    print(my_queue.peek())
    print(my_queue.dequeue())
    print(my_queue.peek())
    print(my_queue.isEmpty())
    my_queue.dequeue()
    print(my_queue.peek())
    print(my_queue.dequeue())
    print(my_queue.isEmpty())