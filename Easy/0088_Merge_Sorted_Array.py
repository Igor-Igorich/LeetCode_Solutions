from typing import Self


def merge_bad(
        nums1: list[int],
        m: int,
        nums2: list[int], 
        n: int
        ) -> None:
    first = 0
    second = 0
    res = []
    for _ in range(n + m):
        if first >= m:
            res.append(nums2[second])
            second += 1
        elif second >= n:
            res.append(nums1[first])
            first += 1
        elif nums1[first] <= nums2[second]:
            res.append(nums1[first])
            first += 1
        else:
            res.append(nums2[second])
            second += 1
    nums1[:] = list(res)

def merge(
        nums1: list[int],
        m: int,
        nums2: list[int], 
        n: int
        ) -> None:
    
    first_idx = m - 1
    second_idx = n - 1
    cur_idx = m + n - 1
    
    while second_idx >= 0:
        
        if first_idx >= 0 and nums1[first_idx] > nums2[second_idx]:
            nums1[cur_idx] = nums1[first_idx]
            first_idx -= 1
        else:
            nums1[cur_idx] = nums2[second_idx]
            second_idx -= 1
        
        cur_idx -= 1


nums1 = [1,2,3,0,0,0]
merge(nums1, m=3, nums2=[2,5,6], n=3)
print(nums1)