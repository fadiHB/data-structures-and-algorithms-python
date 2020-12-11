from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues_Class10_1 import Queue

def test_enqueue():
    my_queue = Queue()
    my_queue.enqueue(0)
    assert my_queue.peek() == 0
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    assert my_queue.peek() == 0

def test_dequeue():
    my_queue = Queue()
    my_queue.enqueue(0)
    my_queue.enqueue(1)
    assert my_queue.dequeue() == 0
    assert my_queue.peek() == 1

def test_isEmpty():
    my_queue = Queue()
    assert my_queue.isEmpty() == True
    my_queue.enqueue(0)
    my_queue.enqueue(1)
    assert my_queue.isEmpty() == False
    my_queue.dequeue()
    assert my_queue.peek() == 1
    my_queue.dequeue()
    assert my_queue.isEmpty() == True

def test_raises_exception():
    my_queue = Queue()
    assert my_queue.peek() == 'the queue is already empty'