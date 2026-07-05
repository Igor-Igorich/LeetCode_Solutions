
def is_palindrome(x):
    if x < 0:
        return False
    elif 0 >= x < 10:
        return True
    temp_x = x
    reverse_x = 0
    while temp_x > 0:
        reverse_x = reverse_x * 10 + temp_x % 10
        temp_x //= 10
    return reverse_x == x

def is_palindrome_with_str(x):
    if x < 0:
        return False
    elif 0 >= x < 10:
        return True
    str_x = str(x)
    lo = 0
    hi = len(str_x) - 1
    while lo < hi:
        if not(str_x[lo] == str_x[hi]):
            return False
        lo += 1
        hi -= 1
    return True
'''
import time

for i in range(1000):
    start_time = time.time()
    res_1 = is_palindrome(i)
    end_time = time.time()
    if res_1:
        print(f'Result for {i} without str: {res_1}; time = {end_time - start_time}')
    start_time = time.time()
    res_2 = is_palindrome_with_str(i)
    end_time = time.time()
    if res_2:
        print(f'Result for {i} with str: {res_2}; time = {end_time - start_time}')
    if res_2 != res_1:
        print('ERROR')
        break
'''

def prim_sol(x: int) -> bool:
    st = str(x)
    return st == st[::-1]

print (prim_sol(-121))

