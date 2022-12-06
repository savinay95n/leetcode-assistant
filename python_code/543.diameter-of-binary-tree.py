# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # considering height of a tree with single node as 0
        # considering height of a null tree to be -1
        res = [0]
        def dfs(root):
            if not root:
                return -1
            # calculate left_height
            left = dfs(root.left)
            # calculate right_height
            right = dfs(root.right)
            # calculate diameter (dia = left_height + right_height + 2)
            res[0] = max(res[0], left + right + 2)
            # return max_height = 1 + max(left_height, right_height)
            return 1 + max(left, right)
        dfs(root)
        return res[0]