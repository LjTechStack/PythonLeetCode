import unittest
from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_list = s.rstrip(' ').split(' ')

        return len(str_list[-1])


class TestNotebook(unittest.TestCase):

    def test_add(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLastWord("this is a string"), 6)
        self.assertEqual(solution.lengthOfLastWord("this is a  "), 1)
        self.assertEqual(solution.lengthOfLastWord("this is a ab"), 2)
        self.assertEqual(solution.lengthOfLastWord(" "), 0)

