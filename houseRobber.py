def houseRobber(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]

    amt = [0 for i in range(len(nums) + 1)]
    amt[0] = 0
    amt[1] = nums[0]

    for i in range(2, len(nums) + 1):
        amt[i] = max(amt[i - 1], amt[i - 2] + nums[i - 1])

    return amt[len(nums)]

def houseRobber2(nums):
    newVal = 0
    oldVal = 0
    for val in nums:
        tmp_newval = oldVal + val
        oldVal = max(tmp_newval, oldVal)
        newVal = tmp_newval
    return max(newVal, oldVal)
import unittest
class DoTests(unittest.TestCase):

   def test_this(self):
       input = [[2], [1,1,1], [1,5,1], [20,30,30,2]]
       output = [2,2,5,50]
       for i in range(len(input)):
           self.assertEqual(houseRobber2(input[i]), output[i], msg="Input %s didn't give output %d" % (str(input[i]), output[i]) )
if __name__ == "__main__":
    unittest.main()

