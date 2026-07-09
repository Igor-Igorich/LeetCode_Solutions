
import string

def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    s = s.lower()
    while left < right:
        while not(s[left].isalnum()) and left < right:
            left += 1
        while not(s[right].isalnum()) and left < right:
            right -= 1
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def primitive_is_palindrome(s: str) -> bool:
    transform = str.maketrans("", "", string.punctuation)
    s = "".join(s.translate(transform).lower().split())

    return s == s[::-1]

def bad_is_palindrome(s: str) -> bool:
    s = ''.join(c.lower() for c in s if c.isalnum())
    left = 0 
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

def pipeline_check(func: function) -> str:
    s_1 = "A man, a plan, a canal: Panama"
    s_2 = "race a car"
    s_3 = " "
    return f'1) -> {func(s_1)}\n2) -> {func(s_2)}\n3) -> {func(s_3)}'

print(pipeline_check(primitive_is_palindrome))
