
import timeit

def add_binary_primal(
        a, b: str,
        ) -> str:
    res = ''
    sum_digits = ''
    carry = '0'
    i = 1
    while (i <= max(len(a), len(b))) or (carry != '0'):
        
        sum_digits = ''
        
        if i <= len(a):
            sum_digits += a[-i]
        if i <= len(b):
            sum_digits += b[-i]
        
        match sum_digits:
            case '01' | '10' | '1':
                if carry == '1':
                    res = '0' + res
                else:
                    res = '1' + res
            case '11':
                if carry == '1':
                    res = '1' + res
                else:
                    res = '0' + res
                    carry = '1'
            case '00' | '0' | '':
                if carry == '1':
                    res = '1' + res
                    carry = '0'
                else:
                    res = '0' + res
        i += 1
        
    return res

def add_binary_too_simple(
        a, b: str,
        ) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]


def add_binary(
        a, b: str,
        ) -> str:
    res = ''
    carry = 0
    idx = 1
    len_a = len(a)
    len_b = len(b)
    
    while idx <= len_a or idx <= len_b or carry:
        if idx <= len_a:
            carry += int(a[-idx])
        if idx <= len_b:
            carry += int(b[-idx])
        
        res = str(carry % 2) + res
        carry //= 2
        
        idx += 1
    
    return res
    
def add_binary_good(
        a, b: str,
        ) -> str:
    res = []
    carry = 0
    idx = 1
    len_a = len(a)
    len_b = len(b)
    
    while idx <= len_a or idx <= len_b or carry:
        if idx <= len_a:
            carry += int(a[-idx])
        if idx <= len_b:
            carry += int(b[-idx])
        
        res.append(str(carry % 2))
        carry //= 2
        
        idx += 1
    
    return ''.join(res[::-1])


a = input('Enter a:')
b = input('Enter b:')
print(add_binary(a, b))
