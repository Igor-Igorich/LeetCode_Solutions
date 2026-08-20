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


def level_order_01(root: Optional[TreeNode]) -> List[List[int]]:
    res = []

    if root is None:
        return res

    queue = deque([(root, 0)])
    while queue:
        cur_node, cur_level = queue.popleft()

        if len(res) <= cur_level:
            res.append([])

        res[-1].append(cur_node.val)

        if cur_node.left:
            queue.append((cur_node.left, cur_level + 1))
        if cur_node.right:
            queue.append((cur_node.right, cur_level + 1))

    return res


def level_order_02(root: Optional[TreeNode]) -> List[List[int]]:
    res = []

    if root is None:
        return res

    queue = deque([root])
    while queue:

        cur_level = []

        for _ in range(len(queue)):

            cur_node = queue.popleft()
            cur_level.append(cur_node.val)

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

        res.append(cur_level)

    return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(level_order_02(root))
