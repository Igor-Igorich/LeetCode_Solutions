from typing import Callable
import time
from functools import wraps


def timer_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} выполнена за {elapsed:.6f} сек")
        return result
    return wrapper


@timer_decorator
def is_valid(s: str) -> bool:
    """
    Проверяет, является ли строка скобок правильной скобочной последовательностью.

    Алгоритм:
        1. Использует стек для отслеживания открывающих скобок.
        2. При встрече закрывающей скобки проверяет соответствие последней
           открывающей скобке в стеке.
        3. Если соответствие нарушено или стек пуст — возвращает False.
        4. В конце проверяет, что стек пуст (все скобки закрыты).

    Args:
        s: Строка, содержащая скобки '(', ')', '{', '}', '[', ']'.

    Returns:
        bool: True, если строка является правильной скобочной последовательностью,
              иначе False.

    Time complexity: O(n), где n — длина строки.
    Space complexity: O(n) в худшем случае (только открывающие скобки).
    """
    stack = []

    bracket_pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in bracket_pairs:
            if not stack:
                return False

            last = stack.pop()
            if last != bracket_pairs[char]:
                return False
        else:
            stack.append(char)

    return len(stack) == 0


def pipeline_check(func: Callable) -> str:
    """
    Тестирует функцию проверки правильной скобочной последовательности.

    Args:
        func: Функция, принимающая строку скобок.

    Returns:
        str: Отформатированные результаты тестирования.

    Raises:
        TypeError: Если переданный аргумент не является вызываемой функцией.
    """
    if not callable(func):
        raise TypeError("Аргумент должен быть вызываемой функцией")

    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("((((", False),
        ("))))", False),
        ("({[}])", False),
        ("{[()]}", True),
        ("()" * 10000 + "{}" * 10000 + "[]" * 10000, True),
    ]

    results = []
    for i, (s, expected) in enumerate(test_cases, 1):
        result = func(s)
        status = "good" if result == expected else f"bad (ожидалось {expected})"

        display_s = s if len(s) <= 50 else f"{s[:47]}..."
        results.append(
            f"{i}) Input: \"{display_s}\"\n"
            f"   Output: {result} {status}"
        )

    return "\n\n".join(results)


def main() -> None:
    """Точка входа в программу. Демонстрирует работу алгоритма."""
    print(pipeline_check(is_valid))
    print()


if __name__ == "__main__":
    main()
