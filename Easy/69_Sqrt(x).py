
def my_sqrt_very_bad(
        x: int
        ) -> int:
    res = 0
    while (res + 1) * (res + 1) <= x:
        res += 1
    return res

def my_sqrt_with_binary_search(
        x: int
        ) -> int:
    if x < 2:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

def my_sqrt_with_binary_operations(
        x: int
        ) -> int:
    if x < 2:
        return x
    
    cnt = 0
    temp = x
    while temp > 0: # подсчет кол-ва битов числа (для 8 = 1000 cnt = 4, для 7 = 111 cnt = 3)
        cnt += 1
        temp >>= 1
    
    res = 0
    for i in range( (cnt + 1) // 2, -1, -1):
        res |= (1 << i) # побитовое "или" для 0000 -> 1000 -> 1100 -> 1110 -> 1111
        if res * res > x:
            res ^= (1 << i) # отменяем последнее увеличение с помощью xor
    
    return res

print(my_sqrt_with_binary_operations(int(input('Enter number: '))))