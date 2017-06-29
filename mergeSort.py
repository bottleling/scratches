def merge(a,b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        elif b[j] < a[i]:
            result.append(b[j])
            j += 1
    if i < len(a):
        result.extend(a[i:])
    elif j < len(b):
        result.extend(b[j:])
    return result



def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr) // 2
    a = mergeSort(arr[:mid])
    b = mergeSort(arr[mid:])
    return merge(a,b)

import unittest
class DoTests(unittest.TestCase):

    def test_quicksort(self):
        a = [5,3,2,1,4]
        self.assertEqual(mergeSort(a), range(1,6))
if __name__ == "__main__":
    unittest.main()

