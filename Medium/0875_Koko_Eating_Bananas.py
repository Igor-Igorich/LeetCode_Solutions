from typing import List, Callable
import math
from functools import wraps
import time


def timer_decorator(func: Callable) -> Callable:
    """
    Декоратор для измерения времени выполнения функции.

    Args:
        func: Декорируемая функция.

    Returns:
        Callable: Обёрнутая функция с логированием времени выполнения.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start

        print(f"{func.__name__} выполнена за {elapsed:.6f} сек")

        return result
    return wrapper


@timer_decorator
def min_eating_speed(piles: List[int], h: int) -> int:
    """
    Находит минимальную скорость поедания бананов (бананов в час),
    чтобы съесть все бананы за h часов.

    Алгоритм:
        1. Если количество куч равно h, скорость должна быть равна 
           максимальному размеру кучи (съедаем по одной куче в час).
        2. Если куча одна, скорость вычисляется как ceil(piles[0] / h).
        3. В противном случае применяется бинарный поиск по скорости 
           в диапазоне [1, max(piles)].
        4. Для проверки скорости используется вспомогательная функция check,
           которая вычисляет общее время, необходимое для поедания всех бананов
           с заданной скоростью, и сравнивает его с h.

    Args:
        piles: Список размеров куч бананов (целые положительные числа).
        h: Количество часов, за которое необходимо съесть все бананы.

    Returns:
        int: Минимальная скорость поедания (бананов в час).

    Time complexity: O(n log m), где n — количество куч, 
                     m — максимальный размер кучи.
    Space complexity: O(1) — константная дополнительная память.
    """
    ans = max(piles)

    if h == len(piles):
        return ans

    if len(piles) == 1:
        return math.ceil(piles[0] / h)

    def check(speed: int) -> bool:
        """
        Проверяет, можно ли съесть все бананы за h часов 
        с заданной скоростью.

        Args:
            speed: Скорость поедания (бананов в час).

        Returns:
            bool: True, если все бананы можно съесть за h часов или меньше,
                  иначе False.
        """
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / speed)
        return total_hours <= h

    left = 1
    right = ans

    while left <= right:
        mid = left + (right - left) // 2

        if check(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


def pipeline_check(func: Callable) -> str:
    """
    Тестирует функцию поиска минимальной скорости поедания бананов.

    Args:
        func: Функция, принимающая список куч piles и количество часов h.

    Returns:
        str: Отформатированные результаты тестирования.

    Raises:
        TypeError: Если переданный аргумент не является вызываемой функцией.
    """
    if not callable(func):
        raise TypeError("Аргумент должен быть вызываемой функцией")

    test_cases = [
        ([3, 6, 7, 11], 8, 4, "Базовый случай: классический пример с несколькими кучами"),
        ([30, 11, 23, 4, 20], 5, 30, "Меньше часов, чем куч — высокая скорость"),
        ([30, 11, 23, 4, 20], 6, 23, "Промежуточный случай"),
        ([312884470], 312884470, 1, "Одна куча, много часов — минимальная скорость"),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10, 1, "Все кучи одного размера, ровно по часу"),
        ([1000000000, 1000000000, 1000000000], 3, 1000000000, "Большие числа, точное совпадение"),
        ([1000000000], 2, 500000000, "Одна куча — деление пополам"),
    ]

    results = []
    for i, (piles, h, expected, description) in enumerate(test_cases, 1):
        result = func(piles, h)
        status = "PASS" if result == expected else f"FAIL (ожидалось {expected})"
        results.append(
            f"{i}) {description}\n"
            f"   Input: piles={piles}, h={h}\n"
            f"   Output: {result} {status}"
        )

    return "\n\n".join(results)


def main() -> None:
    """Точка входа в программу. Демонстрирует работу алгоритма."""

    print(pipeline_check(min_eating_speed))


if __name__ == "__main__":
    main()