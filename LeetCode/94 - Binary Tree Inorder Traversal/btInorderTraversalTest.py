import unittest
from btInorderTraversal import Solution, TreeNode


class InorderTraversalTest(unittest.TestCase):
    """Testing example cases from LeetCode 94 - Binary Tree Inorder Traversal"""
    def test_ex1(self):
        root = TreeNode().list_to_tree_node([1,None,2,3])
        expected = [1,3,2]
        actual = Solution().inorder_traversal(root)
        self.assertEqual(actual, expected)

    def test_ex2(self):
        root = TreeNode().list_to_tree_node([1,2,3,4,5,None,8,None,None,6,7,9])
        expected = [4,2,6,5,7,1,3,9,8]
        actual = Solution().inorder_traversal(root)
        self.assertEqual(actual, expected)

    def test_ex3(self):
        root = TreeNode().list_to_tree_node([])
        expected = []
        actual = Solution().inorder_traversal(root)
        self.assertEqual(actual, expected)

    def test_ex4(self):
        root = TreeNode().list_to_tree_node([1])
        expected = [1]
        actual = Solution().inorder_traversal(root)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
