def minCoinChange(coins, amt):
    if amt == 0:
        return 0
    ways = [float('inf') for i in range(amt+1)]
    ways[0] = 0
    for i in range(0, amt+1):
        for coin in coins:
            #if you use the coin, update the amount
            if i + coin <= amt:
                ways[i+coin] = min(ways[i+coin], ways[i]+1)
    if ways[amt] == float('inf'):
        return -1
    return ways[amt]


import unittest
class DoTests(unittest.TestCase):

    # def test_empty(self):
    #     self.assertEqual(minCoinChange([],0), 0)
    # def test_single(self):
    #     self.assertEqual(minCoinChange([1,2],1), 1)
    # def test_two(self):
    #     self.assertEqual(minCoinChange([1,2,3,4], 5), 2)
    #
    # def test_twenty(self):
    #     self.assertEqual(minCoinChange([1, 2, 3], 20), 7)

    def test_thirty(self):
        self.assertEqual(minCoinChange([5,1, 6], 30), 5)
if __name__ == "__main__":
    unittest.main()

