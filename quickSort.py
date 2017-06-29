def partition(arr, left, end):
    pivotVal = arr[end]
    right = end
    while left < right:
        while left < right and arr[left] < pivotVal:
            left += 1
        while right > left and arr[right] >= pivotVal:
            right -=1
        tmp = arr[left]
        arr[left] = arr[right]
        arr[right] = tmp
    ## when left and right meet, swap the value at that position with the pivot value
    tmp = arr[left]
    arr[left] = arr[end]
    arr[end] = tmp
    return left

def quickSort(arr, left, right):
    if left < right:
        pivotInd = partition(arr, left, right)
        quickSort(arr, left, pivotInd -1)
        quickSort(arr, pivotInd, right)
    return arr

import unittest
class DoTests(unittest.TestCase):

    def test_quicksort(self):
        a = [10,9,8,4,7,5,2,1,3,6]
        self.assertEqual(quickSort(a, 0, len(a)-1), range(1,11))
if __name__ == "__main__":
    unittest.main()

