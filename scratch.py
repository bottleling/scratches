def siftdown(arr, first, last ):
    child = 2*first+1
    #index of the left child whose parent is root at 'first'

    while child <= last:
        sibling = child + 1
        #if the right child is larger than the left, let's move the parent to the right instead
        if (child < last) and (arr[child] < arr[sibling]):
            child += 1 #this is now the right child

        if arr[child] > arr[first]: #if the child is larger than parent
            #swap the child and root
            tmp = arr[child]
            arr[child] = arr[first]
            arr[first] = tmp
            first = child #the root's index was changed!
            child = 2 * first + 1
        else: #it's ok, the children are smaller than the parent.
            return

def heapify(arr):
    lastInd = len(arr) - 1
    parents = lastInd//2 #approximate parents.. we dont have to sift down for leaf nodes on the bottom level
    for i in range(parents, -1, -1):
        siftdown(arr, i, lastInd)
    return arr

def heapSort(arr):
    heapify(arr) # create a max heap

    for i in range(len(arr)-1,0,-1):
        if arr[0] > arr[i]: #the heap has its maximal element at position 0. so this moves it to the back of the array.
            tmp = arr[0]
            arr[0] = arr[i]
            arr[i] = tmp
            siftdown(arr, 0, i-1)
    return arr
import unittest
class DoTests(unittest.TestCase):
    def test_heapify(self):
        a = [5, 3, 2, 1, 4]
        self.assertEqual(heapify(a), [5,4,2,1,3])
    def test_heapsort(self):
        a = [5,3,2,1,4]
        self.assertEqual(heapSort(a), range(1,6))
if __name__ == "__main__":
    unittest.main()

