from typing import List, Callable
import time
from functools import wraps


def timer_decorator(func: Callable) -> Callable:
    """Декоратор для измерения времени выполнения функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start

        print(f"{func.__name__} выполнена за {elapsed:.6f} сек")

        return result
    return wrapper


@timer_decorator
def three_sum_closest(nums: List[int], target: int) -> int:
    """
    Находит сумму трёх различных элементов массива, ближайшую к целевому значению.

    Алгоритм:
        1. Сортирует массив для применения техники двух указателей.
        2. Фиксирует первый элемент тройки (индекс i).
        3. Для оставшейся части массива запускает два указателя (left, right),
           сходящихся к центру, вычисляя сумму тройки на каждом шаге.
        4. Отслеживает сумму, минимально отличающуюся от target.
        5. При обнаружении точного совпадения — мгновенный возврат.
        6. Использует ранние прерывания (pruning) для отсечения заведомо
           неоптимальных ветвей перебора.

    Args:
        nums: Массив целых чисел длиной n >= 3.
        target: Целевое значение, к которому необходимо приблизиться.

    Returns:
        int: Сумма трёх элементов, ближайшая к target.
             Гарантируется, что решение единственно.

    Time complexity:  O(n²) — внешний цикл O(n), внутренний O(n).
                      Сортировка O(n log n) поглощается квадратичной составляющей.
    Space complexity: O(1) — константная дополнительная память
                      (не считая O(n) на сортировку в худшем случае).
    """
    n = len(nums)
    nums.sort()

    closest_sum = float('inf')

    for i in range(n - 2):
        
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        min_sum = nums[i] + nums[i + 1] + nums[i + 2]
        if min_sum > target:
            if abs(min_sum - target) < abs(closest_sum - target):
                closest_sum = min_sum
            break
        
        max_sum = nums[i] + nums[n - 1] + nums[n - 2]
        if max_sum < target:
            if abs(max_sum - target) < abs(closest_sum - target):
                closest_sum = max_sum
            continue

        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                return target

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum < target:
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            else:
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return closest_sum


def pipeline_check(func: Callable) -> str:
    """
    Тестирует функцию поиска ближайшей суммы трёх элементов.

    Args:
        func: Функция, принимающая массив nums и целевое значение target.

    Returns:
        str: Отформатированные результаты тестирования.

    Raises:
        TypeError: Если переданный аргумент не является вызываемой функцией.
    """
    if not callable(func):
        raise TypeError("Аргумент должен быть вызываемой функцией")

    test_cases = [
        ([-1, 2, 1, -4], 1, 2, "Базовый случай: смешанные положительные и отрицательные"),
        ([0, 0, 0], 1, 0, "Все элементы одинаковые, цель отлична"),
        ([1, 1, 1, 1], 3, 3, "Точное совпадение с дубликатами"),
        ([4, 0, 5, -5, 3, 3, 0, -4, -5], -2, -2, "Сложный случай с повторениями"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 20, 20, "Точное совпадение, цель больше"),
        ([-10, -5, -3, -1, 2, 4, 7, 9], 0, 0, "Цель — ноль, массив отсортирован")
    ]

    results = []
    for i, (nums, target, expected, description) in enumerate(test_cases, 1):
        result = func(nums, target)
        status = "good" if result == expected else f"bad (ожидалось {expected})"
        results.append(f"{i}) {description}\n   Input: target={target}\n   Output: {result} {status}")

    return "\n\n".join(results)


def main() -> None:
    """Точка входа в программу. Демонстрирует работу поиска ближайшей суммы трёх элементов."""
    print("=== Тестирование 3Sum Closest ===\n")
    print(pipeline_check(three_sum_closest))


if __name__ == "__main__":
    main()