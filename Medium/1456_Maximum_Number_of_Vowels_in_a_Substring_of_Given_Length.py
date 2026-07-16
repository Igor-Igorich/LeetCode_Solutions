
def primitive_max_vowels(s: str, k: int) -> int:
	cur_sum = 0
	vows = list('aeiou')
	if s[0] in vows:
		cur_sum = 1
	left = 0
	right = 0
	while right < k-1:
		right += 1
		if s[right] in vows:
			cur_sum += 1
	
	if len(s) == k:
		return cur_sum
	
	cur_max = cur_sum
	
	right += 1
	if s[right] in vows:
		cur_sum += 1
	if s[left] in vows:
		cur_sum -=1
	cur_max = max(cur_max, cur_sum)
	
	while right < len(s) - 1:
		right += 1
		left += 1
		
		if s[right] in vows:
			cur_sum += 1
		if s[left] in vows:
			cur_sum -= 1
		cur_max = max(cur_sum, cur_max)
	
	return cur_max

def max_vowels(s: str, k: int) -> int:
    vowels = set('aeiou')
    
    cur_sum = sum(1 for ch in s[:k] if ch in vowels)
    cur_max = cur_sum
    
    for i in range(k, len(s)):
        
        if s[i] in vowels:
            cur_sum += 1

        if s[i - k] in vowels:
            cur_sum -= 1
        cur_max = max(cur_max, cur_sum)
    
    return cur_max


def pipeline_check(func):
	
	s_1, k_1 = "abciiidef", 3
	s_2, k_2 = "aeiou", 2
	s_3, k_3 = "leetcode", 3
	
	return f'1) {func(s_1, k_1)}\n2) {func(s_2, k_2)}\n3) {func(s_3, k_3)}'

print(pipeline_check(max_vowels))