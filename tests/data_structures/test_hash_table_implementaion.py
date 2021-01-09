from data_structures_and_algorithms.data_structures.hash_table_implementaion.hashmap import Node, Hashmap
import pytest

def test_add(prep):
    actual = prep.add('name', 'Ahmad')
    assert prep.contains('name') == True   

def test_hash(prep):
    assert prep.get_hash('could') == 903
    assert prep.get_hash('colud') == 903

def test_get(prep):
    prep.add('could', 67)
    prep.add('colud', 100)
    assert prep.get('could') == 67
    assert prep.get('colud') == 100
    assert prep.get('test') == 'the key is not valid'

def test_contain(prep):
    assert prep.contains('test') == False



@pytest.fixture
def prep():
    things = Hashmap(1024)
    return things