from data_structures_and_algorithms.data_structures.repeated_word.repeated_word import max_occurred_world

def test_repated():
    actual = max_occurred_world('Once upon a time, there was a brave princess who..')
    expected = 'a'
    assert actual == expected