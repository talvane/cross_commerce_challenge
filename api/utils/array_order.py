def quickSort(aArray):
    quickSortHelper(aArray, 0, len(aArray)-1)


def quickSortHelper(aArray, first, last):
    if first < last:

        splitpoint = partition(aArray, first, last)

        quickSortHelper(aArray, first, splitpoint-1)
        quickSortHelper(aArray, splitpoint+1, last)


def partition(aArray, first, last):
    pivotvalue = aArray[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and aArray[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while aArray[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = aArray[leftmark]
            aArray[leftmark] = aArray[rightmark]
            aArray[rightmark] = temp

    temp = aArray[first]
    aArray[first] = aArray[rightmark]
    aArray[rightmark] = temp

    return rightmark
