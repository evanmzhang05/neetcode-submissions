# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        counter = 0
        finalList = [[]]

        def dfs(root, counter) -> List[List[int]]:
            if not root:
                return []
            
            if len(finalList) - 1 < counter:
                finalList.append([root.val])
            else:
                finalList[counter].append(root.val)

            left = dfs(root.left, counter + 1)
            right = dfs(root.right, counter + 1)
            return finalList
        
        return dfs(root, counter)


