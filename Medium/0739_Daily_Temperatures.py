from typing import List, Callable
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
def daily_temperatures_01(temperatures: List[int]) -> List[int]:
    """
    Находит количество дней до следующего более тёплого дня.

    Алгоритм (с использованием монотонного стека):
        1. Инициализирует массив результатов нулями.
        2. Использует монотонно убывающий стек для хранения пар (температура, индекс).
        3. При обходе массива слева направо:
           - Пока стек не пуст и текущая температура больше температуры на вершине стека,
             извлекаем индекс из стека и вычисляем разницу дней.
           - Помещаем текущую температуру и индекс в стек.
        4. Элементы, оставшиеся в стеке, не имеют более тёплого дня в будущем.

    Args:
        temperatures: Список дневных температур.

    Returns:
        List[int]: Список, где каждый элемент — количество дней до следующего
                   более тёплого дня. Если такого дня нет, значение равно 0.

    Time complexity: O(n), где n — количество дней.
    Space complexity: O(n) в худшем случае.

    Note:
        Монотонный стек хранит элементы в порядке убывания температуры.
    """
    result = [0] * len(temperatures)
    monotonic_stack = []

    for idx in range(len(temperatures)):
        while monotonic_stack and monotonic_stack[-1][0] < temperatures[idx]:
            old_idx = monotonic_stack.pop()[1]
            result[old_idx] = idx - old_idx

        monotonic_stack.append((temperatures[idx], idx))

    return result


@timer_decorator
def daily_temperatures_02(temperatures: List[int]) -> List[int]:
    """
    Находит количество дней до следующего более тёплого дня.

    Алгоритм (с использованием динамического программирования):
        1. Инициализирует массив результатов нулями.
        2. Обходит массив справа налево (с предпоследнего элемента).
        3. Для каждого дня i:
           - Начинаем с next_day = i + 1.
           - Пока температура в next_day <= температуре в i:
             - Если у next_day есть ответ (res[next_day] != 0), 
               переходим к следующему дню, используя этот ответ.
             - Иначе более тёплого дня не существует (выходим из цикла).
           - Вычисляем разницу между i и next_day как результат.

    Args:
        temperatures: Список дневных температур.

    Returns:
        List[int]: Список, где каждый элемент — количество дней до следующего
                   более тёплого дня. Если такого дня нет, значение равно 0.

    Time complexity: O(n), где n — количество дней (средний случай).
    Space complexity: O(1) (не считая памяти для результата).

    Note:
        Использует оптимизацию с прыжками через уже вычисленные дни.
        Более эффективен по памяти, чем версия со стеком.
    """
    n = len(temperatures)
    res = [0] * n

    for i in range(n - 2, -1, -1):
        next_day = i + 1

        while next_day < n and temperatures[next_day] <= temperatures[i]:
            if res[next_day] != 0:
                next_day = res[next_day] + next_day
            else:
                break

        if next_day < n and temperatures[next_day] > temperatures[i]:
            res[i] = next_day - i

    return res


def pipeline_check() -> str:
    """
    Тестирует обе реализации daily_temperatures.
    """
    test_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73],
         [1, 1, 4, 2, 1, 1, 0, 0],
         "Базовый случай: типичные температуры"),
        ([30, 40, 50, 60], [1, 1, 1, 0], "Монотонно возрастающие температуры"),
        ([60, 50, 40, 30], [0, 0, 0, 0], "Монотонно убывающие температуры"),
        ([30, 30, 30, 30], [0, 0, 0, 0], "Все температуры одинаковые"),
        ([89, 62, 70, 58, 47, 47, 46, 76, 100, 70],
         [8, 1, 5, 4, 3, 2, 1, 1, 0, 0],
         "Сложный случай с повторениями"),
        ([1], [0], "Один элемент"),
        ([100, 99, 98, 97, 96, 95, 94, 93, 92, 91],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         "Убывающая последовательность (нет более тёплых дней)"),
    ]

    implementations = [
        ("daily_temperatures_01 (монотонный стек)", daily_temperatures_01),
        ("daily_temperatures_02 (динамическое программирование)", daily_temperatures_02),
    ]

    all_results = []

    for impl_name, impl_func in implementations:
        impl_results = [f"\n{impl_name}:"]

        for i, (temperatures, expected, description) in enumerate(test_cases, 1):
            result = impl_func(temperatures)
            status = "PASS" if result == expected else f"FAIL (ожидалось {expected})"
            impl_results.append(
                f"  {i}) {description}\n"
                f"     Input: {temperatures}\n"
                f"     Output: {result} {status}"
            )

        all_results.append("\n".join(impl_results))

    return "\n\n".join(all_results)


def main() -> None:
    print(pipeline_check())

if __name__ == "__main__":
    main()