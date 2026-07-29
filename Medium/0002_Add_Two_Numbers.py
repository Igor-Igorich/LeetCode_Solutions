from typing import List, Callable, Optional
import time
from functools import wraps


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def timer_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} выполнена за {elapsed:.6f} сек")
        return result
    return wrapper


def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    """Преобразует список в связный список."""
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Преобразует связный список в список Python."""
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


@timer_decorator
def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Складывает два числа, представленные в виде связных списков.

    Алгоритм:
        1. Создаёт фиктивный узел-голову для результирующего списка.
        2. Проходит по обоим спискам одновременно, пока есть элементы или перенос.
        3. На каждом шаге складывает цифры из обоих списков и перенос с предыдущего шага.
        4. Вычисляет новую цифру (sum % 10) и новый перенос (sum // 10).
        5. Добавляет новую цифру в результирующий список.
        6. Продвигает указатели в обоих списках, если они не закончились.

    Args:
        l1: Голова первого связного списка (число записано в обратном порядке).
        l2: Голова второго связного списка (число записано в обратном порядке).

    Returns:
        Optional[ListNode]: Голова результирующего связного списка,
                            представляющего сумму чисел.

    Time complexity: O(max(m, n)), где m и n — длины списков.
    Space complexity: O(max(m, n)) для хранения результата.

    Note:
        Числа хранятся в обратном порядке (единицы в голове).
        Пример: число 342 представлено как [2, 4, 3].
    """
    answer = ListNode()
    tail = answer
    carry = 0

    while l1 is not None or l2 is not None or carry:
        digit_1 = l1.val if l1 is not None else 0
        digit_2 = l2.val if l2 is not None else 0

        summ = digit_1 + digit_2 + carry
        carry = summ // 10
        cur_digit = summ % 10

        new_node = ListNode(cur_digit)
        tail.next = new_node
        tail = tail.next

        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    return answer.next


def pipeline_check() -> str:
    """
    Тестирует функцию сложения чисел из связных списков.
    """
    test_cases = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8], "342 + 465 = 807"),
        ([0], [0], [0], "0 + 0 = 0"),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1],
         "9999999 + 9999 = 10009998"),
        ([1], [9, 9, 9], [0, 0, 0, 1], "1 + 999 = 1000"),
        ([5], [5], [0, 1], "5 + 5 = 10"),
        ([1, 8], [0], [1, 8], "81 + 0 = 81"),
        ([9, 9], [1], [0, 0, 1], "99 + 1 = 100"),
    ]

    results = []

    for i, (arr1, arr2, expected, description) in enumerate(test_cases, 1):
        l1 = list_to_linked_list(arr1)
        l2 = list_to_linked_list(arr2)

        result_node = add_two_numbers(l1, l2)
        result = linked_list_to_list(result_node)

        status = "PASS" if result == expected else f"FAIL (ожидалось {expected})"
        results.append(
            f"{i}) {description}\n"
            f"   Input: l1={arr1}, l2={arr2}\n"
            f"   Output: {result} {status}"
        )

    return "\n\n".join(results)


def main() -> None:
    print(pipeline_check())


if __name__ == "__main__":
    main()