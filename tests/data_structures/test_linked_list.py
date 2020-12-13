from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,Node,zip_lists
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

def test_zip_lists():
    ll1 = LinkedList()
    ll1.append(3)
    ll1.append(2)
    ll1.append(1)
    ll2 = LinkedList()
    ll2.append(3)
    ll2.append(2)
    ll2.append(1)
    assert zip_lists(ll1,ll2).__str__() == "{ 3 } -> { 3 } -> { 2 } -> { 2 } -> { 1 } -> { 1 } -> NULL"
    