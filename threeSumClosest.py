def threeSumClosest( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    nums = sorted(nums)
    diff = float("inf")
    result = 0
    for i in range(len(nums)):
        forward = i + 1
        backward = len(nums) - 1
        while forward < backward:
            s = nums[i] + nums[forward] + nums[backward]
            currdiff = abs(target - s)
            if currdiff == 0:
                return s
            if currdiff < diff:
                diff = currdiff
                result = s
            if s > target:
                backward -= 1
            elif s <= target:
                forward += 1
    return result

import unittest
class DoTests(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(threeSumClosest([],1), 0)
    def test_single(self):
        self.assertEqual(threeSumClosest([10, 20, 3, 40, 5, 60, 98], 35), 35)
    def test_two(self):
        self.assertEqual(threeSumClosest([3,2,7], 4), 12)
    def test_twenty(self):
        self.assertEqual(threeSumClosest([50, 3, 10, 7, 40, 80], 12), 20)
if __name__ == "__main__":
    unittest.main()

