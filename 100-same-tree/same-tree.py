class Solution(object):

  def isSameTree(self, p, q):
    """:type p: Optional[TreeNode]

    :type q: Optional[TreeNode]
    :rtype: bool
    """

    def same(p, q):
      # If both are None, they match
      if not p and not q:
        return True
      # If one is None or values don't match, they are different
      if not p or not q or p.val != q.val:
        return False

      # Recursively check both left and right children properly
      left = same(p.left, q.left)
      right = same(p.right, q.right)
      return left and right

    return same(p, q)