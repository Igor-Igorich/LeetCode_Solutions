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


class MyCodec_01:

    def serialize_recursive(self, root: Optional[TreeNode]) -> str:

        if root is None:
            return "None"

        left = self.serialize_recursive(root.left)
        right = self.serialize_recursive(root.right)

        return str(root.val) + "_" + left + "_" + right

    def deserialize_recursive(self, data: str) -> Optional[TreeNode]:

        def recursive_create(queue: deque) -> Optional[TreeNode]:

            if not queue:
                return None

            val = queue.popleft()
            if val == "None":
                return None

            new_node = TreeNode(int(val))
            new_node.left = recursive_create(queue)
            new_node.right = recursive_create(queue)

            return new_node

        data_queue = deque(data.split("_"))

        return recursive_create(data_queue)


class MyCodec_02:

    def serialize(self, root: Optional[TreeNode]) -> str:

        if root is None:
            return "None"

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("None")

        while result and result[-1] == "None":
            result.pop()

        return "_".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:

        arr = data.split("_")

        if not arr or arr[0] == "None":
            return None

        root = TreeNode(int(arr[0]))
        queue = deque([root])
        idx = 1

        while queue and idx < len(arr):

            cur_node = queue.popleft()

            # Левый потомок
            if idx < len(arr) and arr[idx] != "None":
                cur_node.left = TreeNode(int(arr[idx]))
                queue.append(cur_node.left)
            idx += 1

            # Правый потомок
            if idx < len(arr) and arr[idx] != "None":
                cur_node.right = TreeNode(int(arr[idx]))
                queue.append(cur_node.right)
            idx += 1

        return root


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(MyCodec_02().serialize(root=root))
