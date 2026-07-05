

def is_valid(s):
    stack = [1]  
    for i in s:
        match i:
            case ')':
                last = stack.pop()
                if last != '(':
                    return False
            case '}':
                last = stack.pop()
                if last != '{':
                    return False
            case ']':
                last = stack.pop()
                if last != '[':
                    return False
            case _:
                stack.append(i)
    if stack == [1]:
        return True
    else:
        return False
    

# s = input('Enter the sequence of parentheses: ')
print(is_valid('()' * 10_000 + '{}' * 10_000 + '[]' * 10_000))
