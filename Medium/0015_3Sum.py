from collections import Counter

def slower_three_sum(nums: list[int]) -> list[list[int]]:
    s_nums = sorted(nums)
    result = []
    n = len(s_nums)
    
    for i in range(n - 2):

        if i > 0 and s_nums[i] == s_nums[i - 1]:
            continue
        
        left = i + 1
        right = n - 1
        target = -s_nums[i]
        
        while left < right:
            cur_sum = s_nums[left] + s_nums[right]
            
            if cur_sum == target:
                result.append([s_nums[i], s_nums[left], s_nums[right]])
                
                while left < right and s_nums[left] == s_nums[left + 1]:
                    left += 1
                while left < right and s_nums[right] == s_nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
                
            elif cur_sum < target:
                
                while left < right and s_nums[left] == s_nums[left + 1]:
                    left += 1
                
                left += 1
            else:
                
                while left < right and s_nums[right] == s_nums[right - 1]:
                    right -= 1
                
                right -= 1
    
    return result

# 1) Duplicates do not create problems with the result
# 2) Redundant optimization that complicates the code

def three_sum(nums: list[int]) -> list[list[int]]:
    s_nums = sorted(nums)
    result = []
    n = len(s_nums)
    
    for i in range(n - 2):

        if i > 0 and s_nums[i] == s_nums[i - 1]:
            continue
        
        left = i + 1
        right = n - 1
        target = -s_nums[i]
        
        while left < right:
            cur_sum = s_nums[left] + s_nums[right]
            
            if cur_sum == target:
                result.append([s_nums[i], s_nums[left], s_nums[right]])
                
                while left < right and s_nums[left] == s_nums[left + 1]:
                    left += 1
                while left < right and s_nums[right] == s_nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
                
            elif cur_sum < target:
                left += 1
            else:
                right -= 1
    return result


def faster_three_sum(nums: list[int]) -> list[list[int]]:
    cnts = Counter(nums)
    uniques = list(cnts.keys())
    uniques.sort()
    result = []

    for i, a in enumerate(uniques):
        
        if a > 0:
            break

        if a == 0:
            if cnts[0] >= 3:
                result.append([0, 0, 0])
            break
            
        # a == b < c
        if cnts[a] >= 2:
            c = -2 * a
            if c in cnts:
                result.append([a, a, c])

        # a < b <= c
        for j in range(i + 1, len(uniques)):
            b = uniques[j]
            c = -(a + b)

            if c < b:
                break
            
            if c == b:
                if cnts[b] >= 2:
                    result.append([a, b, b])
                    
            else:
                if c in cnts:
                    result.append([a, b, c])

    return result

def pipeline(func: function) -> str:
    nums_1 = [-1,0,1,2,-1,-4]
    nums_2 = [0,1,1]
    nums_3 = [0,0,0]
    return f'1) {func(nums_1)}\n2) {func(nums_2)}\n3) {func(nums_3)}'

print(pipeline(faster_three_sum))