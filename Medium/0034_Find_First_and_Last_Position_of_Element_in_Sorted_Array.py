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
        
        print(result)
        print(f"{func.__name__} выполнена за {elapsed:.6f} сек")
        
        return result
    return wrapper


@timer_decorator
def search_range(nums: List[int], target: int) -> List[int]:
    """
    Находит диапазон индексов целевого элемента в отсортированном массиве.

    Алгоритм:
        1. Выполняет бинарный поиск для нахождения любого вхождения target
        2. Расширяет границы влево и вправо, пока соседние элементы равны target
        3. Возвращает [left, right] - первый и последний индекс target

    Args:
        nums: Отсортированный по возрастанию список целых чисел
        target: Искомое значение

    Returns:
        List[int]: Список из двух элементов [левый_индекс, правый_индекс].
                   Если элемент не найден, возвращает [-1, -1]

    Time complexity: O(log n + k), где k - количество повторений target
    Space complexity: O(1) - константная память
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            left = right = mid
            while left > 0 and nums[left - 1] == target:
                left -= 1
            while right < len(nums) - 1 and nums[right + 1] == target:
                right += 1
            return [left, right]
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return [-1, -1]


def pipeline_check(func: Callable) -> str:
    """
    Тестирует функцию поиска диапазона на предопределенных данных.

    Args:
        func: Функция поиска, принимающая список и целевое значение

    Returns:
        str: Отформатированные результаты тестирования

    Raises:
        TypeError: Если переданная функция не вызываема
    """
    if not callable(func):
        raise TypeError("Аргумент должен быть вызываемой функцией")

    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8),
        ([5, 7, 7, 8, 8, 10], 6),
        ([], 0),
    ]

    results = []
    for i, (nums, target) in enumerate(test_cases, 1):
        result = func(nums, target)
        results.append(f"{i}) {result}")

    return "\n".join(results)


def main() -> None:
    """Точка входа в программу. Демонстрирует работу поиска диапазона."""
    print(pipeline_check(search_range))


if __name__ == "__main__":
    main()