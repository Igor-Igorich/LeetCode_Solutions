from typing import List

def primitive_top_k_frequent_01(nums: List[int], k: int) -> List[int]:
    ht = {}
    res = []
    for val in set(nums):
        ht[val] = nums.count(val)
    ht = sorted(ht.items(), key=lambda x: x[1], reverse=True)
    for i in range(k):
        res.append(ht[i][0])
    return res

def primitive_top_k_frequent_02(nums: List[int], k: int) -> List[int]:
    ht = {}
    res = []
    for val in nums:
        ht[val] = ht.get(val, 0) + 1
    ht = sorted(ht.items(), key=lambda x: x[1], reverse=True)
    for i in range(k):
        res.append(ht[i][0])
    return res
    
def my_top_k_frequent_01(nums: List[int], k: int) -> List[int]:
    len_nums = (len(nums) + 1)
    res = []
    freqs = [[] for _ in range(len_nums)]
    for val in set(nums):
        freqs[len_nums - nums.count(val)].append(val)
    
    for i in range(len_nums):
        for num in freqs[i]:
            res.append(num)
            if len(res) == k:
                return res

def my_top_k_frequent_02(nums: List[int], k: int) -> List[int]:
    res = []
    freqs = [[] for _ in range(len(nums) + 1)]
    cnts = {}
    for val in nums:
        cnts[val] = cnts.get(val, 0) + 1
        
    for val, cnt in cnts.items():
        freqs[cnt].append(val)
    
    for i in range(len(nums), -1, -1):
        for num in freqs[i]:
            res.append(num)
            if len(res) == k:
                return res

def pipeline_check(func: function) -> str:
    nums_1, k_1 = [1,1,1,2,2,3], 2
    nums_2, k_2 = [1], 1
    nums_3, k_3 = [1,2,1,2,1,2,3,1,3,2], 2
    return f'1) -> {func(nums_1, k_1)}\n2) -> {func(nums_2, k_2)}\n3) -> {func(nums_3, k_3)}'

print(pipeline_check(my_top_k_frequent_02))
