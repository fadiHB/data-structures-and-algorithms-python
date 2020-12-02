from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import binary_search

def test_even_num():
    actual = binary_search([1,2,3,4],4)
    expected = 3
    assert actual == expected


def test_odd_num():
    actual = binary_search([1,2,3,4,5],4)
    expected = 3
    assert actual == expected

def test_not_include_num():
    actual = binary_search([1,2,3,4,5],0)
    expected = -1
    assert actual == expected
