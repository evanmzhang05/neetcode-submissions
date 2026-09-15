# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.isSameTree(root, subRoot) == False:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left or right
        else:
            return True
        

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q == None:
            return True
        elif p == None and q != None:
            return False
        elif p != None and q == None:
            return False

        if p.val != q.val:
            return False
        else:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return left and right