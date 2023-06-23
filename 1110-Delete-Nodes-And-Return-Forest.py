# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# Return the roots of the trees in the remaining forest. You may return the result in any order.

# Example 1:

# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]

# Example 2:

# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]

from ast import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans=[]
        ds=set(to_delete)

        def process(n):
            if not n: return None

            n.left, n.right = process(n.left), process(n.right)

            if n.val in ds: return None
            if n.left: ans.append(n.left)
            if n.right: ans.append(n.right)

            return None
        
        root = process(root)
        if root: ans.append(root)

        return ans