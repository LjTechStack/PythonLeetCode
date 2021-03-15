import unittest
from typing import List


def maxSubArray(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    current_list = greatest_list = nums[0]

    for current in nums[1:]:
        if current > 0:
            if current_list <= 0:
                current_list = current
            else:
                current_list += current
            greatest_list = max(current_list, greatest_list)
        else:
            if current_list <= current:
                current_list = current
            else:
                current_list += current
            greatest_list = max(current_list, greatest_list)
    return max(current_list, greatest_list)


class TestNotebook(unittest.TestCase):

    def test_add(self):
        self.assertEqual(maxSubArray([-2]), -2)
        self.assertEqual(maxSubArray([-2, 1]), 1)
        self.assertEqual(maxSubArray([1]), 1)
        self.assertEqual(maxSubArray([-2, 1, -3]), 1)
        self.assertEqual(maxSubArray([1, 2]), 3)
        self.assertEqual(maxSubArray([-2, -1]), -1)
        self.assertEqual(maxSubArray([-2, -1, -3]), -1)
        self.assertEqual(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(maxSubArray([8, -19, 5, -4, 20]), 21)
        self.assertEqual(maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4]), 6)

