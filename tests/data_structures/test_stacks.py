from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues_Class10_2 import Stacks,Node


def test_push_peek_pop_isEmpty():
    my_stacks = Stacks()
    my_stacks.push(10)
    assert my_stacks.peek() == 10 # Can successfully push onto a stack
    my_stacks.push(20)
    my_stacks.push('test')
    my_stacks.push(True)
    assert my_stacks.peek() == True #Can successfully push multiple values onto a stack
                                    #Can successfully peek the next item on the stack

def test_pop():
    my_stacks = Stacks()
    my_stacks.push(10)
    my_stacks.push(20)
    my_stacks.push('test')
    my_stacks.push(True)
    assert my_stacks.pop() == True #Can successfully pop off the stack
    assert my_stacks.peek() == 'test' ##Can successfully pop off the stack

def test_isEmpty():
    my_stacks = Stacks()
    assert my_stacks.isEmpty() == True
    my_stacks.push(10)
    my_stacks.push(20)
    assert my_stacks.isEmpty() == False
    my_stacks.pop()
    my_stacks.pop()
    assert my_stacks.isEmpty() == True #Can successfully empty a stack after multiple pops
    
def test_raises_exception():
    my_stacks = Stacks()
    assert my_stacks.peek() == 'the stack is already empty ..!!' #Calling pop or peek on empty stack raises exception















# def test_pop():


 