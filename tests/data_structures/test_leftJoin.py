from data_structures_and_algorithms.data_structures.leftJoin.leftJoin import Hashtable, left_join
import pytest


def test_left_join_normal():
    h1 = Hashtable(1024)
    h1.add('fond','enamored')        
    h1.add('wrath', 'anger')          
    h1.add('diligent', 'employed')    
    h1.add('outfit', 'garb')           
    h1.add('guide', 'usher')

    h2 = Hashtable(1024)
    h2.add('fond', 'averse')
    h2.add('wrath', 'delight')
    h2.add('diligent', 'idle')
    h2.add('guide', 'follow')
    h2.add('flow', 'jam')

    assert  left_join(h1,h2) == [ ['fond', 'enamored', 'averse'], ['outfit', 'garb', None], ['diligent', 'employed', 'idle'], ['wrath', 'anger', 'delight'], ['guide', 'usher', 'follow']]

def test_left_join_1st_empty():
    h1 = Hashtable(1024)
    h2 = Hashtable(1024)
    h2.add('fond', 'averse')
    h2.add('wrath', 'delight')
    h2.add('diligent', 'idle')
    h2.add('guide', 'follow')
    h2.add('flow', 'jam')

    assert left_join(h1,h2) == []

def test_left_join_no_matches():
    one = Hashtable(1024)
    one.add('pond','enamored')        
    one.add('rath', 'anger')          
    one.add('adiligent', 'employed')    
    one.add('poutfit', 'garb')           
    one.add('hangguide', 'usher')           

    two = Hashtable(1024)
    two.add('fond', 'averse')
    two.add('wrath', 'delight')
    two.add('diligent', 'idle')
    two.add('guide', 'follow')
    two.add('flow', 'jam')

    assert left_join(one,two) == [['rath', 'anger', None], ['pond', 'enamored', None], ['hangguide', 'usher', None], ['adiligent', 'employed', None], ['poutfit', 'garb', None]] 


