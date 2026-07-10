from typing import List

def two_sum(numbers: List[int], target: int) -> List[int]:
    idx_1 = 0
    start_idx_2 = len(numbers) - 1
    idx_2 = start_idx_2
    while True:
        sum = numbers[idx_1] + numbers[idx_2]
        if sum == target:
            return [idx_1 + 1, idx_2 + 1]
        elif sum > target:
            idx_2 -= 1
        else:
            idx_1 += 1

def pipeline_check(func: function) -> str:
    n_1, t_1 = [2,7,11,15], 9
    n_2, t_2 = [2,3,4], 6
    n_3, t_3 = [-1,0], -1
    
    return f'1) {func(n_1, t_1)}\n2) {func(n_2, t_2)}\n3) {func(n_3, t_3)}'

print(pipeline_check(two_sum))