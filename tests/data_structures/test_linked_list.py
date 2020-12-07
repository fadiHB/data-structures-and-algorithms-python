from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,Node
)



def test_instance():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


def test_insert():
    ll = LinkedList()
    ll.insert(5)
    assert ll.head.value == 5
    ll.insert(10)
    assert ll.head.value == 10

def test_includes():
    ll = LinkedList()
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    ll.insert(0)
    assert ll.includes(3) == True
    assert ll.includes(5) == False

def test__str__():
    ll = LinkedList()
    ll.insert('c')
    ll.insert('b')
    ll.insert('a')
    assert ll.__str__() == "{ a } -> { b } -> { c } -> NULL"

# def test_ll_kth():
#     ll = LinkedList()
#     ll.insert(2)
#     ll.insert(8)
#     ll.insert(3)
#     ll.insert(1)
#     ll.kthFromEnd(0)
#     assert ll.kthFromEnd(0) is 1
#     assert ll.__st
#     pass

def test_k_isgreater_than_the_length():
    ll = LinkedList()
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    assert ll.kthFromEnd(4) == 'the k is grater than list length'

def test_k_and_the_length_of_the_list_are_the_same():
    ll = LinkedList()
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    ll.insert(1)
    assert ll.kthFromEnd(3) == 1

def test_k_is_not_a_positive_intege():
    ll = LinkedList()
    ll.insert(8)
    ll.insert(3)
    assert ll.kthFromEnd(-1) == 'cant be negative number'

def test_linked_list_is_of_a_size_1():
    ll = LinkedList()
    ll.insert(8)
    assert ll.kthFromEnd(0) == 8


