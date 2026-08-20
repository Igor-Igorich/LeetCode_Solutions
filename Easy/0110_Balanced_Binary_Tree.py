from typing import Optional, Self, Tuple


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


def is_balanced_recursive_01(root: Optional[TreeNode]) -> bool:

    def balance_and_height(root: Optional[TreeNode]) -> Tuple[bool, int]:
        if root is None:
            return (True, -1)

        left_balanced, left_height = balance_and_height(root.left)
        right_balanced, right_height = balance_and_height(root.right)

        height = 1 + max(left_height, right_height)
        balanced = (
            abs(right_height - left_height) <= 1
            and left_balanced
            and right_balanced
        )

        return (balanced, height)

    return balance_and_height(root)[0]


def is_balanced_recursive_02(root: Optional[TreeNode]) -> bool:

    def check_height(node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left_height = check_height(node.left)
        if left_height == -1:
            return -1

        right_height = check_height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return check_height(root) != -1


def is_balanced_iterative(root: Optional[TreeNode]) -> bool:

    if root is None:
        return True

    stack = [(root, False)]
    heights = {None: -1}

    while stack:

        cur_node, visited = stack.pop()

        if cur_node is None:
            continue

        if visited:

            left_height = heights[cur_node.left]
            right_height = heights[cur_node.right]

            if abs(right_height - left_height) > 1:
                return False

            heights[cur_node] = max(left_height, right_height) + 1

        else:

            stack.append((cur_node, True))

            stack.append((cur_node.right, False))
            stack.append((cur_node.left, False))

    return True


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(is_balanced_iterative(root))
