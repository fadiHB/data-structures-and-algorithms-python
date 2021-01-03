from data_structures_and_algorithms.challenges.Insertion_Sort.Insertion_Sort import insertion_sort

def test_insertion_sort():
    actual = insertion_sort([9,8,7,6,5,4,3,2,1])
    exptected = [1,2,3,4,5,6,7,8,9]
    assert actual == exptected