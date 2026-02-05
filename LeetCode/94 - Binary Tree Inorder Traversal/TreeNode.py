from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def list_to_tree_node(values) -> Optional['TreeNode']:
        """Helper function to convert a list into a tree node"""
        if not values: return None

        # Creating the root
        iterator_val = iter(values)
        root = TreeNode(next(iterator_val))

        queue = [root]

        while queue:
            current = queue.pop(0)

            # Trying to add Left Child
            try:
                val = next(iterator_val)
                if val is not None:
                    current.left = TreeNode(val)
                    queue.append(current.left)
            except StopIteration:
                break

            # Trying to add Right Child
            try:
                val = next(iterator_val)
                if val is not None:
                    current.right = TreeNode(val)
                    queue.append(current.right)
            except StopIteration:
                break
        return root