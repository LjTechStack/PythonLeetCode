import unittest

def say(string: str) -> str:
    prev = ""
    count = 1
    result = ""
    for char in string:
        if char == prev:
            count += 1
        else:
            if prev == "":
                prev = char
            else:
                result += str(count) + prev
                count = 1
                prev = char
    result += str(count) + prev
    return result


# %%
def countAndSay(n: int) -> str:
    count = 1
    result = ""
    while (count <= n):
        if count == 1:
            result = "1"
        else:
            result = say(result)
        count += 1

    return result

class TestNotebook(unittest.TestCase):

    def test_add(self):
        self.assertEqual(countAndSay(0), "")
        self.assertEqual(countAndSay(1), "1")
        self.assertEqual(countAndSay(2), "11")
        self.assertEqual(countAndSay(3), "21")
        self.assertEqual(countAndSay(4), "1211")
        self.assertEqual(countAndSay(5), "111221")
        self.assertEqual(countAndSay(6), "312211")
        self.assertEqual(countAndSay(7), "13112221")


unittest.main(argv=[''], verbosity=2, exit=False)