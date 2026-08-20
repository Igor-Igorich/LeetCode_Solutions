from collections import deque
from typing import List, Optional, Self


class TreeNode:

    def __init__(
        self,
        val: int = 0,
        left: Optional[Self] = None,
        right: Optional[Self] = None,
    ) -> None:
        self.val: int = val
        self.left: Optional[Self] = left
        self.right: Optional[Self] = right


def zigzag_order(root: Optional[TreeNode]) -> List[List[int]]:

    res = []

    if root is None:
        return res

    queue = deque([root])
    reverse = False

    while queue:

        cur_level = []

        for _ in range(len(queue)):

            if not reverse:
                cur_node = queue.popleft()
                cur_level.append(cur_node.val)

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            else:
                cur_node = queue.pop()
                cur_level.append(cur_node.val)

                if cur_node.right:
                    queue.appendleft(cur_node.right)
                if cur_node.left:
                    queue.appendleft(cur_node.left)

        res.append(cur_level)
        reverse = not reverse

    return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(zigzag_order(root))
