from typing import List, Callable, Optional
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


class MinStack_01:
    """
    Реализация стека с поддержкой получения минимального элемента за O(1).
    
    Алгоритм:
        1. Использует два стека: основной и стек для хранения текущих минимумов.
        2. При push добавляет элемент в основной стек и обновляет минимум в min_stack.
        3. При pop удаляет элементы из обоих стеков.
        4. getMin возвращает последний элемент из min_stack (текущий минимум).

    Time complexity: O(1) для всех операций.
    Space complexity: O(n) для хранения двух стеков.
    """
    def __init__(self):
        self.general_stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.general_stack.append(value)
        
        cur_min = self.getMin()
        if cur_min is None or cur_min > value:
            cur_min = value
        self.min_stack.append(cur_min)

    def pop(self) -> None:
        self.general_stack.pop()
        self.min_stack.pop()

    def top(self) -> Optional[int]:
        if self.general_stack:
            return self.general_stack[-1]
        return None

    def getMin(self) -> Optional[int]:
        if self.min_stack:
            return self.min_stack[-1]
        return None


class MinStack_02:
    """
    Реализация стека с поддержкой получения минимального элемента за O(1).
    
    Алгоритм:
        1. Использует один стек для хранения кортежей (значение, текущий_минимум).
        2. При push вычисляет новый минимум и сохраняет пару.
        3. При pop удаляет верхний элемент.
        4. getMin возвращает сохранённый минимум из верхнего элемента.

    Time complexity: O(1) для всех операций.
    Space complexity: O(n) для хранения стека с кортежами.
    """
    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        cur_min = self.getMin()
        if cur_min is None or cur_min > value:
            cur_min = value
        self.stack.append((value, cur_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> Optional[int]:
        if self.stack:
            return self.stack[-1][0]
        return None

    def getMin(self) -> Optional[int]:
        if self.stack:
            return self.stack[-1][1]
        return None


class MinStack_03:
    """
    Реализация стека с поддержкой получения минимального элемента за O(1).
    
    Алгоритм:
        1. Использует один стек для хранения списков [значение, текущий_минимум].
        2. При push вычисляет новый минимум и сохраняет список.
        3. При pop удаляет верхний элемент.
        4. getMin возвращает сохранённый минимум из верхнего элемента.

    Time complexity: O(1) для всех операций.
    Space complexity: O(n) для хранения стека со списками.
    """
    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val is None or min_val > val:
            min_val = val
        self.st.append([val, min_val])

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> Optional[int]:
        return self.st[-1][0] if self.st else None

    def getMin(self) -> Optional[int]:
        return self.st[-1][1] if self.st else None


def test_min_stack(MinStackClass: Callable, operations: List[str], values: List) -> List[Optional[int]]:
    """
    Тестирует реализацию стека с поддержкой минимума.

    Args:
        MinStackClass: Класс стека для тестирования.
        operations: Список операций ('push', 'pop', 'top', 'getMin').
        values: Список значений для операций push.

    Returns:
        List[Optional[int]]: Результаты операций top и getMin.
    """
    stack = MinStackClass()
    results = []
    value_index = 0

    for op in operations:
        if op == 'push':
            stack.push(values[value_index])
            value_index += 1
            results.append(None)
        elif op == 'pop':
            stack.pop()
            results.append(None)
        elif op == 'top':
            results.append(stack.top())
        elif op == 'getMin':
            results.append(stack.getMin())

    return results


def pipeline_check() -> str:
    """
    Тестирует все три реализации MinStack на различных наборах операций.
    """
    test_cases = [
        (
            ["push", "push", "push", "getMin", "pop", "top", "getMin"],
            [-2, 0, -3],
            [None, None, None, -3, None, 0, -2],
            "Базовый случай: push, pop, top, getMin"
        ),
        (
            ["push", "push", "push", "getMin", "push", "getMin", "pop", "getMin"],
            [1, 2, 3, 4],
            [None, None, None, 1, None, 1, None, 1],
            "Минимум не меняется"
        ),
        (
            ["push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin"],
            [5, 7, 3],
            [None, None, None, 3, None, 5, None, 5],
            "Удаление минимального элемента"
        ),
        (
            ["push", "getMin", "push", "getMin", "push", "getMin", "push", "getMin"],
            [10, 5, 3, 1],
            [None, 10, None, 5, None, 3, None, 1],
            "Монотонно убывающие значения"
        ),
        (
            ["push", "getMin", "push", "getMin", "push", "getMin", "pop", "getMin", "pop", "getMin"],
            [1, 2, 3],
            [None, 1, None, 1, None, 1, None, 1, None, 1],
            "Удаление элементов"
        ),
    ]

    classes = [
        ("MinStack_01 (два стека)", MinStack_01),
        ("MinStack_02 (кортежи)", MinStack_02),
        ("MinStack_03 (списки)", MinStack_03),
    ]

    all_results = []

    for class_name, min_stack_class in classes:
        class_results = [f"\n{class_name}:"]
        
        for i, (ops, vals, expected, description) in enumerate(test_cases, 1):
            result = test_min_stack(min_stack_class, ops, vals)
            status = "PASS" if result == expected else f"FAIL (ожидалось {expected})"
            class_results.append(
                f"  {i}) {description}\n"
                f"     Операции: {ops}\n"
                f"     Результат: {result} {status}"
            )
        
        all_results.append("\n".join(class_results))

    return "\n\n".join(all_results)


def main() -> None:
    """Точка входа в программу. Демонстрирует работу трёх реализаций MinStack."""
    print(pipeline_check())


if __name__ == "__main__":
    main()