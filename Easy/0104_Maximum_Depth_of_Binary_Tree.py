from typing import Optional, Self


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


def max_depth_recursive(root: Optional[TreeNode]) -> int:

    if root is None:
        return 0

    return (
        max(max_depth_recursive(root.left), max_depth_recursive(root.right)) + 1
    )


def max_depth_iterative(root: Optional[TreeNode]) -> int:

    if root is None:
        return 0

    stack = [(root, 1)]
    res = 0

    while stack:

        cur_node, cur_depth = stack.pop()
        res = max(res, cur_depth)

        if cur_node.left:
            stack.append((cur_node.left, cur_depth + 1))
        if cur_node.right:
            stack.append((cur_node.right, cur_depth + 1))

    return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(max_depth_iterative(root))
