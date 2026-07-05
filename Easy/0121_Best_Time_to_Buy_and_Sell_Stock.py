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
            
            
