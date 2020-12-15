from data_structures_and_algorithms.data_structures.queue_with_stacks.queue_with_stacks import PseudoQueue,Queue,Stacks,Node

def test_dequeue_one():
    queue = PseudoQueue()
    queue.enqueu(1)
    queue.enqueu(2)
    queue.enqueu(3)
    queue.enqueu(4)
    assert queue.dequeue() == 1


def test_dequeue_two():
    queue = PseudoQueue()
    queue.enqueu(1)
    queue.dequeue()
    assert queue.dequeue() == 'Ops .. the Stack is empty man !!'
