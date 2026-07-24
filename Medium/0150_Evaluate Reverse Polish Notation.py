from typing import List, Callable
import time
from functools import wraps

def timer_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        elapsed = time.perf_counter() - start
        print(f'{func.__name__} выполнена за {elapsed:.6f} сек')
        
        return func(*args, **kwargs)
    return wrapper

@timer_decorator
def eval_rpn(tokens: List[str]) -> int:
    """
    Вычисляет выражение, заданное в обратной польской нотации (ОПН).

    Алгоритм:
        1. Использует стек для хранения операндов.
        2. При встрече числа помещает его в стек.
        3. При встрече оператора извлекает два верхних элемента из стека,
           выполняет операцию и помещает результат обратно в стек.
        4. В конце вычислений в стеке остаётся один элемент — результат.

    Args:
        tokens: Список токенов (числа и операторы) в обратной польской нотации.

    Returns:
        int: Результат вычисления выражения.

    Time complexity: O(n), где n — количество токенов.
    Space complexity: O(n) в худшем случае (только числа в стеке).

    Note:
        Деление целочисленное с округлением к нулю (как в C++/Java).
        Используется int(first / second) для правильного округления
        отрицательных чисел к нулю.
    """
    stack = []

    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            second = stack.pop()
            first = stack.pop()
            stack.append(first - second)
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "/":
            second = stack.pop()
            first = stack.pop()
            stack.append(int(first / second))
        else:
            stack.append(int(token))

    return stack[0]

def pipeline_check(func: Callable) -> str:
    """
    Тестирует функцию вычисления выражений в обратной польской нотации.

    Args:
        func: Функция, принимающая список токенов.

    Returns:
        str: Отформатированные результаты тестирования.

    Raises:
        TypeError: Если переданный аргумент не является вызываемой функцией.
    """
    
    if not callable(func):
        raise TypeError('Аргумент должен быть вызываемой функцией')
    
    test_cases = [
        (["2", "1", "+", "3", "*"], 9, "Простое выражение: (2 + 1) * 3"),
        (["4", "13", "5", "/", "+"], 6, "Средний случай: 4 + (13 / 5)"),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
         22, "Сложное выражение из условия задачи"),
        (["3", "4", "+", "2", "*"], 14, "(3 + 4) * 2"),
        (["4", "2", "/"], 2, "Простое деление: 4 / 2"),
        (["3", "11", "+", "5", "-"], 9, "(3 + 11) - 5"),
        (["4", "3", "-"], 1, "Вычитание: 4 - 3"),
        (["2", "3", "*", "4", "+"], 10, "2 * 3 + 4"),
        (["-3", "-2", "*"], 6, "Умножение отрицательных чисел"),
        (["10", "3", "/"], 3, "Деление с округлением к нулю: 10/3 = 3"),
        (["-10", "3", "/"], -3, "Деление с округлением к нулю: -10/3 = -3"),
    ]
    
    results = []
    for i, (tokens, expected, description) in enumerate(test_cases, 1):
        res = func(tokens)
        status = 'PASS' if res == expected else 'FAIL (ожидалось {expected})'
        
        results.append(
            f"{i}) {description}\n"
            f"   Input: {tokens}\n"
            f"   Output: {res} {status}"
        )
        
    return '\n\n'.join(results)

def main() -> None:
    """Точка входа в программу. Демонстрирует работу алгоритма."""

    print(pipeline_check(eval_rpn))

if __name__ == '__main__':
    main()