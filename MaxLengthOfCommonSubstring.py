import unittest


def returnMaxLengthOfCommonSubstring(a: str, b: str, maxLen: int) -> int:
    if len(a) == 1 or len(b) == 1:
        if len(a) == 1 and len(b) == 1:
            return maxLen+1 if a == b else maxLen
        if len(a) == 1:
            return maxLen+1 if a == b[0] else returnMaxLengthOfCommonSubstring(a, b[1:], 0)
        else:
            return maxLen+1 if a[0] == b else returnMaxLengthOfCommonSubstring(a[1:], b, 0)

    else:
        if a[0] == b[0]:
            return returnMaxLengthOfCommonSubstring(a[1:], b[1:], maxLen+1)
        else:
            return max(max(maxLen, returnMaxLengthOfCommonSubstring(a[1:], b, 0)), max(maxLen, returnMaxLengthOfCommonSubstring(a, b[1:], 0)))


class TestRandomProblem(unittest.TestCase):

    def test_add(self):
        self.assertEqual(returnMaxLengthOfCommonSubstring("abc", "a", 0), 1)
        self.assertEqual(returnMaxLengthOfCommonSubstring("abc", "acb", 0), 1)
        self.assertEqual(returnMaxLengthOfCommonSubstring("aabc", "acac", 0), 1)
        self.assertEqual(returnMaxLengthOfCommonSubstring("aabc", "aacab", 0), 2)
        self.assertEqual(returnMaxLengthOfCommonSubstring("abc", "abc", 0), 3)
        self.assertEqual(returnMaxLengthOfCommonSubstring("abc", "ac", 0), 1)
        self.assertEqual(returnMaxLengthOfCommonSubstring("abcd", "cd", 0), 2)
        self.assertEqual(returnMaxLengthOfCommonSubstring("abcd", "bc", 0), 2)
