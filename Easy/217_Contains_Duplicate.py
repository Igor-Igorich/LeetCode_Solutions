from typing import List

def primitive_contains_duplicate_01(nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return True
    return False
    
def primitive_contains_duplicate_02(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)

def pipeline_execute(func: function) -> str:
    
    nums_1 = [1,2,3,1]    
    nums_2 = [1,2,3,4]
    nums_3 = [1,1,1,3,3,4,3,2,4,2]
    
    return f'{nums_1} -> {func(nums_1)}\n{nums_2} -> {func(nums_2)}\n{nums_3} -> {func(nums_3)}'

def my_contains_duplicate_01_1(nums: List[int]) -> bool:
    hash_table = {}
    for i in nums:
        if i in hash_table:
            return True
        else:
            hash_table[i] = 1
    return False

def my_contains_duplicate_01_2(nums: List[int]) -> bool:
    hash_table = {}
    for i in nums:
        if i in hash_table:
            return True
        hash_table[i] = 1
    return False

def my_contains_duplicate_02(nums: List[int]) -> bool:
    ht = set(nums)
    for i in nums:
        try:
            ht.remove(i)
        except:
            return True
    return False

def my_contains_duplicate_03(nums: List[int]) -> bool:
    ht = set()
    for i in nums:
        if i in ht:
            return True
        ht.add(i)
    return False

print(pipeline_execute(my_contains_duplicate_03))

