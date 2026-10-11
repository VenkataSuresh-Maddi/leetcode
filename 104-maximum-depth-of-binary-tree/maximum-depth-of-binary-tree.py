# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def depth(root,count):
            if root is None:
                return count
            else:
                count+=1
            left = depth(root.left,count)
            right = depth(root.right,count)
            return max(left,right)
        return depth(root,0)
        