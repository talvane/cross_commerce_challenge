from api.utils.array_order import quickSort


aArray = [54, 26, 93, 17, 77, 31, 44, 55, 20]
aOrderArray = [17, 20, 26, 31, 44, 54, 55, 77, 93]


def test_quicksort():
    quickSort(aArray=aArray)
    assert aOrderArray == aArray
