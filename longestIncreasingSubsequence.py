def longestIncreasingSubsequence(seq):
    if len(seq) ==0:
        return 0
    lengths = [0 for i in range(len(seq))]
    lengths[0] = 1
    bestSoFar = 1
    for i in range(1,len(seq)):
        bestToI = 0
        for j in range(0, i):
            if seq[i] > seq[j]:
                bestToI = max(bestToI, lengths[j])
        lengths[i] = bestToI + 1
        bestSoFar = max(bestToI, lengths[i])
    return bestSoFar

import unittest
class DoTests(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(longestIncreasingSubsequence([]), 0)
    def test_single(self):
        self.assertEqual(longestIncreasingSubsequence([10, 20, 3, 40, 5, 60, 98]), 5)
    def test_two(self):
        self.assertEqual(longestIncreasingSubsequence([3,2]), 1)
    def test_twenty(self):
        self.assertEqual(longestIncreasingSubsequence([50, 3, 10, 7, 40, 80]), 4)
if __name__ == "__main__":
    unittest.main()

