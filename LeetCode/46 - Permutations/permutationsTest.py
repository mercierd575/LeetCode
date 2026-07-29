import unittest
from typing import List

from permutations import permute


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        i: List[int] = [1, 2, 3]
        perm: List[List[int]] = permute(i)
        expected: List[List[int]] = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(expected, perm)

    def test_case_2(self):
        i: List[int] = [0,1]
        perm: List[List[int]] = permute(i)
        expected: List[List[int]] = [[0, 1], [1, 0]]
        self.assertEqual(expected, perm)

    def test_case_3(self):
        i: List[int] = [1]
        perm: List[List[int]] = permute(i)
        expected: List[List[int]] = [[1]]
        self.assertEqual(expected, perm)


if __name__ == '__main__':
    unittest.main()
