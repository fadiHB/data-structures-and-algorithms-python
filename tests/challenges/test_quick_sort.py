from data_structures_and_algorithms.challenges.Quick_Sort.Quick_Sort import quickSort, partition

def test_quick_sort():
    arr = [10, 7, 8, 9, 1, 5] 
    n = len(arr)
    actual = quickSort(arr,0,n-1) 
    expected = [1, 5, 7, 8, 9, 10]
    assert actual == expected