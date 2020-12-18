class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def peek(self):
        try:
            return self.front.data
        except AttributeError:
            return "the queue is already empty"

    def enqueue (self,data):
        node = Node(data) 
          
        if self.rear == None: 
            self.front = self.rear = node 
            return
        self.rear.next = node
        self.rear = node 

    def dequeue (self):
  
        if self.isEmpty(): 
            return
        temp = self.front 
        self.front = temp.next
  
        if(self.front == None): 
            self.rear = None

        return temp.data
        

    def isEmpty(self):
        return self.front == None
            
if __name__ == '__main__':
    q = Queue() 
    q.enqueue(10) 
    q.enqueue(20) 
    print('peek ',q.peek())
    q.dequeue()
    print('peek ',q.peek())
    q.dequeue()
    print('peek ',q.peek())
    q.enqueue(30) 
    q.enqueue(40) 
    q.enqueue(50)  
    q.dequeue()
    print("Front " + str(q.front.data)) 
    print("Rear " + str(q.rear.data)) 