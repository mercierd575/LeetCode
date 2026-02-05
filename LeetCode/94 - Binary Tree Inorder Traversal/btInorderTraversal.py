from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """Performs an inorder traversal of a binary tree."""
        res = []

        def traverse(node):
            if not node: return
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)
            return res

        traverse(root)
        return res

