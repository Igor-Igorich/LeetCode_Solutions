from typing import List

def trap(height: List[int]) -> int:
	cur_max = 0
	left = 0
	right = len(height) - 1
	res = 0
	while left < right:
		cur_l = height[left]
		cur_r = height[right]
		
		if cur_l == cur_r:
			cur_max = cur_l
			left += 1
		elif cur_l < cur_r:
			cur_max = max(cur_max, cur_l)
			res += cur_max - cur_l
			left += 1
		else:
			cur_max = max(cur_max, cur_r)
			res += cur_max - cur_r
			right -= 1
			
	return res
			
			

def pipeline_check(func) -> str:
	h_1 = [0,1,0,2,1,0,1,3,2,1,2,1]
	h_2 = [4,2,0,3,2,5]
	return f'1) {func(h_1)}\n2) {func(h_2)}'

print(pipeline_check(trap))