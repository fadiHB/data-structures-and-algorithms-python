from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList, Node
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

def test_append():
    ll = LinkedList()
    ll.append(5)
    assert ll.head.value == 5
    ll.append(10)
    assert ll.head.next.value == 10
    ll.append('f')
    assert ll.head.next.next.value == 'f'

def test_insertBefore():
    ll = LinkedList()
    ll.append(0)
    ll.append(3)
    ll.insertBefore(3,5)
    assert ll.__str__() == "{ 0 } -> { 5 } -> { 3 } -> NULL"

def test_insertAfter():
    ll = LinkedList()
    ll.append(0)
    ll.append(3)
    ll.insertAfter(3,5)
    assert ll.__str__() == "{ 0 } -> { 3 } -> { 5 } -> NULL"





