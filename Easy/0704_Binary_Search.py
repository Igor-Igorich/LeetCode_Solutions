from typing import List, Callable, Optional, Union
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


def binary_search(nums: List[int], target: int) -> int:
    """
    Выполняет классический бинарный поиск в отсортированном массиве.

    Алгоритм:
        1. Устанавливаем левую (left) и правую (right) границы поиска
        2. На каждой итерации находим средний элемент по формуле:
        	mid = left + (right - left) // 2
        3. Сравниваем с целевым значением (target) и сужаем интервал

    Args:
        nums: Отсортированный по возрастанию список целых чисел
        target: Искомое значение

    Returns:
        int: Индекс целевого элемента или -1, если элемент не найден

    Raises:
        ValueError: Если входной список пуст

    Time complexity: O(log n) - логарифмическая сложность
    Space complexity: O(1) - константная память
    """
    if not nums:
        raise ValueError("Массив не может быть пустым")

    left, right = 0, len(nums) - 1

    while left <= right:
        # Вычисление mid с защитой от переполнения
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(nums: List[int], target: int, left: int = 0, right: Optional[int] = None) -> int:
    """
    Рекурсивная реализация бинарного поиска.

    Args:
        nums: Отсортированный список целых чисел
        target: Искомое значение
        left: Левая граница поиска
        right: Правая граница поиска

    Returns:
        int: Индекс целевого элемента или -1, если элемент не найден

    Time complexity: O(log n)
    Space complexity: O(log n) - из-за рекурсивных вызовов
    """
    if right is None:
        right = len(nums) - 1

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)


@timer_decorator
def test_search_algorithm(search_func: Callable[[List[int], int], int]) -> str:
    """
    Тестирует функцию поиска на предопределенных данных.

    Args:
        search_func: Функция поиска, принимающая список и целевое значение

    Returns:
        str: Отформатированные результаты тестирования

    Raises:
        TypeError: Если переданная функция не вызываема
    """
    if not callable(search_func):
        raise TypeError("Аргумент должен быть вызываемой функцией")

    test_data = {
        "массив": [-1, 0, 3, 5, 9, 12],
        "тесты": [
            {"target": 9, "ожидаемый": 4, "описание": "существующий элемент"},
            {"target": 2, "ожидаемый": -1, "описание": "отсутствующий элемент"},
            {"target": -1, "ожидаемый": 0, "описание": "первый элемент"},
            {"target": 12, "ожидаемый": 5, "описание": "последний элемент"},
            {"target": 0, "ожидаемый": 1, "описание": "элемент в середине"}
        ]
    }

    results = [
        f"{'=' * 50}",
        f"Тестирование: {search_func.__name__}",
        f"{'=' * 50}",
        f"Входной массив: {test_data['массив']}"
    ]

    for test in test_data["тесты"]:
        target = test["target"]
        expected = test["ожидаемый"]
        description = test["описание"]

        result = search_func(test_data["массив"], target)
        status = "good" if result == expected else "bad"

        results.append(
            f"{status} Поиск {target} ({description}): "
            f"получено {result}, ожидалось {expected}"
        )

    return "\n".join(results)


def main() -> None:
    """
    Точка входа в программу.
    Демонстрирует работу бинарного поиска с различными сценариями.
    """
    print(test_search_algorithm(binary_search))

    print("\n" + "~" * 50 + "\n")

    print(test_search_algorithm(binary_search_recursive))


if __name__ == "__main__":
    main()