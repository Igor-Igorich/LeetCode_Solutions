from typing import Optional, Self

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_same_tree(
            self: Self,
            p: Optional[TreeNode],
            q: Optional[TreeNode]
            ) -> bool:

        stack = [(p, q)]
        
        while stack:
            r_1, r_2 = stack.pop()
            
            if not r_1 and not r_2:
                continue
            elif not r_1 or not r_2 or r_1.val != r_2.val:
                return False
            
            stack.append((r_1.right, r_2.right))
            stack.append((r_1.left, r_2.left))
        
        return True

