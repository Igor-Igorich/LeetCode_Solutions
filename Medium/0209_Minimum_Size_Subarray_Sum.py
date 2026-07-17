
def min_subarray_len_01(target: int, nums: list[int]) -> int:
	cur_sum = 0
    cur_len = 0
    res = len(nums) + 1
    for i in range(len(nums)):
        cur_len += 1
        cur_sum += nums[i]
        while cur_sum - nums[i - cur_len + 1] >= target:
            cur_sum -= nums[i - cur_len + 1]
            cur_len -= 1
            
        if cur_sum >= target:
            res = min(res, cur_len)
    if res == len(nums) + 1:
        res = 0
    
    return res

def min_subsrray_len_02(target: int, nums: List[int]) -> int:
        min_len = float("inf")
        left = 0
        cur_sum = 0
        
        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                cur_sum -= nums[left]
                left += 1
                
        if min_len == float("inf"):
            min_len = 0
        
        return min_len

def pipeline(func):
	t_1, n_1 = 7, [2, 3, 1, 2, 4, 3]
	t_2, n_2 = 4, [1, 4, 4]
	t_3, n_3 = 11, [1,1,1,1,1,1,1,1]
	
	return f'1) {func(t_1, n_1)}\n2) {func(t_2, n_2)}\n 3) {func(t_3, n_3)}'

print(pipeline(min_subarray_len_01))