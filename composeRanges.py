def composeRanges(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [str(nums[0])]
    s = nums[0]
    e = nums[0]
    res = []
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 1:
            if e == s:
                res.append(str(s))
            else:
                res.append("%d->%d" % (s, e))
            s = nums[i]
        e = nums[i]
    if e == s:
        res.append(str(s))
    else:
        res.append("%d->%d" % (s, e))
    return res


import unittest
class DoTests(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(composeRanges([]), [])
    def test_continuous(self):
        self.assertEual(composeRanges([0,1,2]), "0->2")
if __name__ == "__main__":
    unittest.main()

