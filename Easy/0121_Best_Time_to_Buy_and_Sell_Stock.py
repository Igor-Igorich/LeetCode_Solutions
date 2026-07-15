from typing import List


# Invented by me
def my_max_profit(prices: List[int]) -> int:
    ma = mi = prices[0]
    cur_profit = 0
    
    for i in prices:
        if i < mi:
            cur_profit = max(cur_profit, ma - mi)
            mi = ma = i
        elif i > ma:
            ma = i
            cur_profit = max(cur_profit, ma - mi)
    
    return cur_profit

# From solutions
def mmax_profit(prices: List[int]) -> int:
    buy = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] - buy > profit:
            profit = prices[i] - buy
    return profit

prices = [7,6,4,3,1]
print(my_max_profit(prices))

def max_profit_sliding_window(prices: List[int]) -> int:
	left = 0
	right = 1
	cur_l = prices[left]
	res = 0
	len_prices = len(prices)
	while right < len_prices:
		cur_r = prices[right]
		if cur_r > cur_l:
			res = max(res, cur_r - cur_l)
		elif cur_r < cur_l:
			left = right
			cur_l = prices[left]
		right += 1
	return res

def pipeline_check(func) -> str:
	p_1 = [7, 1, 5, 3, 6, 4]
	p_2 = [7,6, 4, 3, 1]
	return f'1) {func(p_1)}\n2) {func(p_2)}'

print(pipeline_check(max_profit))
            
            
