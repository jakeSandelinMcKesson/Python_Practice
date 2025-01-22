# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal = 0

        def dfs(node):
            if not node: return 0
            left, right = dfs(node.left), dfs(node.right)
            
            if abs(left-right) > 1:
                nonlocal bal
                bal = -1
                return max(left,right) + 1
            else:
                return max(left,right) + 1
        
        dfs(root)

        if bal == -1:
            return False
        else: 
            return True
            
        