def dp(n, result):
    if result[n] > 0:
        return result[n]
    result[n] = dp(n - 1, result) + dp(n - 2, result)
    # all the ways you could have done n-1 step (and add one step to those),
    # plus all the ways you could have done n-2 steps (and add two steps to those)
    return result[n]


def climbingStairs(n):
    if n < 3:
        return n
    result = [0 for i in range(n + 1)]
    result[1] = 1
    result[2] = 2
    return dp(n, result)


import unittest
class DoTests(unittest.TestCase):

   def test_threeorless(self):
       for i in range(4):
           self.assertEqual(climbingStairs(i), i, msg="problem with %d"%i)
if __name__ == "__main__":
    unittest.main()

