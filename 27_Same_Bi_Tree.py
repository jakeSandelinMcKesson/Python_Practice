# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []

        def dfs(node):
            if not node: return None

            left, right = dfs(node.left), dfs(node.right)
            return [node.val,left,right] 

        tree1, tree2  = dfs(p), dfs(q)
        
        if tree1 == tree2:
            return True
        else:
            return False
            