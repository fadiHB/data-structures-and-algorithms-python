from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray
 
def test_insertShiftArray_1():
    actual = insertShiftArray([1,1,1,1],0)
    expected = [1,1,0,1,1]
    assert actual == expected

def test_insertShiftArray_2():
    actual = insertShiftArray([1,1,1],0)
    expected = [1,1,0,1]
    assert actual == expected

def test_insertShiftArray_3():
    actual = insertShiftArray([],0)
    expected = [0]
    assert actual == expected
