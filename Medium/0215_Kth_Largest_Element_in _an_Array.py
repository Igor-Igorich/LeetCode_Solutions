from typing import List
from random import randint
import heapq

def partition(nums: List[int], left: int, right: int, pivot_index: int) -> int:
    
    pivot = nums[pivot_index]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    stored_index = left
    
    for i in range(left, right):
        if nums[i] < pivot:
            nums[i], nums[stored_index] = nums[stored_index], nums[i]
            stored_index += 1
            
    nums[right], nums[stored_index] = nums[stored_index], nums[right]
    return stored_index

def find_kth_largest_02(nums: List[int], k: int) -> int:
    
    left, right = 0, len(nums) - 1
    
    while True:
        pivot_index = randint(left, right)
        new_pivot_index = partition(nums, left, right, pivot_index)
        if new_pivot_index == len(nums) - k:
            return nums[new_pivot_index]
        elif new_pivot_index > len(nums) - k:
            right = new_pivot_index - 1
        else:
            left = new_pivot_index + 1

def pipeline_check(func: function) -> str:
    nums_1, k_1 = [3,2,1,5,6,4], 2
    nums_2, k_2 = [3,2,3,1,2,4,5,5,6], 4
    return f'1) -> {func(nums_1, k_1)}\n2) -> {func(nums_2, k_2)}'

def find_kth_largest_01(nums: List[int], k: int) -> int:
    heap = nums[:k]
    heapq.heapify(heap)
    
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    
    return heap[0]

def primitive_find_kth_largest(nums: List[int], k: int) -> int:
    return sorted(nums, reverse=True)[k-1]


class SpecialList:
    def __init__(self):
        self.data = []

    def insert_sorted(self, x):
        lo, hi = 0, len(self.data)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.data[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        self.data.insert(lo, x)

    def pop_first(self):
        if not self.data:
            raise IndexError("pop from empty list")
        return self.data.pop(0)

    def __len__(self):
        return len(self.data)

    def first(self):
        return self.data[0] if self.data else None

def findKthLargest_with_special(nums, k):
    sl = SpecialList()
    for x in nums:
        sl.insert_sorted(x)
        if len(sl) > k:
            sl.pop_first()
    return sl.first()

print(pipeline_check(findKthLargest_with_special))