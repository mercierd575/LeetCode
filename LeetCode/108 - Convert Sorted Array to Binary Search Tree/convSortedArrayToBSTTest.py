import unittest
from convSortedArrayToBST import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        input_1 = [-10, -3, 0, 5, 9]
        output_1: TreeNode = TreeNode(0,
                                      TreeNode(-3, -10, None),
                                      TreeNode(9, 5))

        self.assertEqual(output_1, Solution.sortedArrayToBST(input_1))


if __name__ == '__main__':
    unittest.main()
