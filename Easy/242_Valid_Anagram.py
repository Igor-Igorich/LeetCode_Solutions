
def primitive_is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

def my_is_anagram_01(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counter = {}

    for char in s:
        counter[char] = counter.get(char, 0) + 1

    for char in t:
        if char not in counter or counter[char] == 0:
            return False
        counter[char] -= 1

    return True

def my_is_anagram_02(s: str, t: str) -> bool:
    if len(s)!=len(t):
        return False
    char=set(s)

    for i in char:
        if s.count(i)!=t.count(i):
            return False
    return True   

def pipeline_check(func: function) -> str:
    set_1 = ("anagram", "nagaram")
    set_2 = ("rat", "car")
    return f'set_1 -> {func(*set_1)}\nset_2 -> {func(*set_2)}'

print(pipeline_check(my_is_anagram_01))