from data_structures_and_algorithms.challenges.marge_sort.marge_sort import mergeSort

def test_marge_sort():
    actual = mergeSort([9, 7, 8, 3, 2, 1])
    expected = [1, 2, 3, 7, 8, 9 ]
    assert actual == expected

        