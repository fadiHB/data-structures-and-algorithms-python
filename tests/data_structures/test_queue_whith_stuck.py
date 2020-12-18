from data_structures_and_algorithms.data_structures.queue_with_stacks.queue_with_stacks import PseudoQueue,Stacks,Node

def test_dequeue_one():
    stack = PseudoQueue()
    stack.enqueu(1)
    stack.enqueu(2)
    stack.enqueu(3)
    stack.enqueu(4)
    assert stack.dequeue() == 1


def test_dequeue_two():
    stack = PseudoQueue()
    stack.enqueu(1)
    stack.dequeue()
    assert stack.dequeue() == 'Ops .. the Stack is empty man !!'
