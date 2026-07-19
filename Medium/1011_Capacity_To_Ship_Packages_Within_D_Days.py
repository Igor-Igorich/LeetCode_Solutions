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
def ship_within_days(weights: List[int], days: int) -> int:
    
    answer = sum(weights)
    
    if days == 1:
        return answer

    def check(capacity: int) -> bool:
        total_days = 0
        current_weight = 0

        for weight in weights:
            if current_weight + weight <= capacity:
                current_weight += weight
            else:
                total_days += 1
                current_weight = weight

        if current_weight > 0:
            total_days += 1

        return total_days <= days

    left = max(weights)
    right = answer

    while left <= right:
        mid = left + (right - left) // 2

        if check(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


def pipeline_check(func: Callable) -> str:
    if not callable(func):
        raise TypeError("Аргумент должен быть вызываемой функцией")

    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15),
        ([3, 2, 2, 4, 1, 4], 3, 6),
        ([1, 2, 3, 1, 1], 4, 3),
        ([10, 20, 30, 40, 50, 60], 3, 90),
        ([100, 200, 300, 400, 500], 5, 500),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10, 1),
        ([5, 5, 5, 5, 5], 2, 15),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 55),
    ]

    results = []
    for i, (weights, days, expected) in enumerate(test_cases, 1):
        result = func(weights, days)
        status = "good" if result == expected else f"bad (ожидалось {expected})"
        results.append(
            f"{i}) Input: weights={weights}, days={days}\n"
            f"   Output: {result} {status}"
        )

    return "\n\n".join(results)


def main() -> None:
    print(pipeline_check(ship_within_days))


if __name__ == "__main__":
    main()