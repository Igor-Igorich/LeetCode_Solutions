from typing import List

def max_area_01(height: List[int]) -> int:
    result = -1
    cur_l = len(height) - 1
    left = 0
    right = cur_l
    cur_left = height[left]
    cur_right = height[right]
    cur_h = min(cur_left, cur_right)
    
    while left < right:
        result = max(result, cur_h * cur_l)
        if cur_left < cur_right:
            left += 1
            cur_left = height[left]
        else:
            right -= 1
            cur_right = height[right]
        cur_l -= 1
        cur_h = min(cur_left, cur_right)
    
    return result

def max_area_02(height: List[int]) -> int:
    result = -1
    cur_l = len(height) - 1
    left = 0
    right = cur_l
    cur_left = height[left]
    cur_right = height[right]
    cur_h = min(cur_left, cur_right)
    
    while left < right:
        result = max(result, cur_h * cur_l)
        if cur_left < cur_right:
            while (left < right) and (cur_left >= height[left + 1]):
                left += 1
                cur_l -= 1
            left += 1
            cur_left = height[left]
        else:
            while (left < right) and (cur_right >= height[right - 1]):
                right -= 1
                cur_l -= 1
            right -= 1
            cur_right = height[right]
        cur_l -= 1
        cur_h = min(cur_left, cur_right)
    
    return result

def pipeline_check(func: function) -> str:
    height_1 = [1,8,6,2,5,4,8,3,7]
    height_2 = [1,1]
    return f'1) {func(height_1)}\n2) {func(height_2)}'

print(pipeline_check(max_area_02))
