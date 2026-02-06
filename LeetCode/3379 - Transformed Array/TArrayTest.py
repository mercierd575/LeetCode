import unittest
from typing import List
from TransformedArray import constructTransformedArray

class TArrayTest(unittest.TestCase):
    def test_1(self):
        nums = [3,-2,1,1]
        actual = constructTransformedArray(nums)
        expected = [1,1,1,3]
        self.assertEqual(actual, expected)

    def test_2(self):
        nums = [-10]
        actual = constructTransformedArray(nums)
        expected = [-10]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
