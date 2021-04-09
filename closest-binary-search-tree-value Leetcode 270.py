"""
https://leetcode.com/problems/closest-binary-search-tree-value/
https://www.lintcode.com/problem/900/


Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        closest=float('inf')
        while root:

            if abs(target-root.val) < abs(target-closest):
                closest= root.val
            
            if root.val > target:
                root=root.left

            else:
                root=root.right
        return closest

    