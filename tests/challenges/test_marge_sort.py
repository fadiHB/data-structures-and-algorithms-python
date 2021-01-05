from data_structures_and_algorithms.challenges.marge_sort import marge_sort

def test_marge_sort():
    actual = marge_sort([9, 7, 8, 3, 2, 1])
    expected = [1, 2, 3, 7, 8, 9 ]
    if actual == expected:
        print('-------- Happy Path --------')
    assert actual == expected