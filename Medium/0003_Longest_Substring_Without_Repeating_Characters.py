
def len_of_longest_substr_01(s: str) -> int:
	
	if not s:
        return 0
    
    left = 0
    right = 1
    cur_len = 1
    cur_max = 1
    
    while right < len(s):
        
        while right < len(s) and s[right] not in s[left:right]:
            right += 1
            cur_len += 1
        
        cur_max = max(cur_len, cur_max)
        
        
        if right >= len(s):
            break
        
        
        while left < right and s[right] in s[left:right]:
            left += 1
            cur_len -= 1
    
    return cur_max

def len_of_longest_substr_02(s: str) -> int:
    left = 0
    max_len = 0
    seen = set()
    
    for right in range(len(s)):
        
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

def pipeline_check(func) -> str:
	s_1 = 'abcabcbb'
	s_2 = 'bbbbb'
	s_3 = 'pwwkew'
	
	return f'1) {func(s_1)}\n2) {func(s_2)}\n3) {func(s_3)}'

print(pipeline_check(len_of_longest_substr))
