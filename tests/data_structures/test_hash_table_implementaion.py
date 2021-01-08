from data_structures_and_algorithms.data_structures.hash_table_implementaion.hashmap import Node, Hashmap
import pytest

def test_add(prep):
    actual = prep.add('name', 'Ahmad')
    assert prep.contains('name') == True   

def test_get(prep):
    assert prep.get('colud') == 100

def test_contain(prep):
    assert prep.contains('test') == False

def test_hash(prep):
    assert prep.get_hash('could') == 903

@pytest.fixture
def prep():
    things = Hashmap(1024)
    things.add('could', 67)
    things.add('colud', 100)
    return things