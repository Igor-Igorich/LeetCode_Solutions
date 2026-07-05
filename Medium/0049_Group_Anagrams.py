
from typing import List
from collections import defaultdict

def primitive_group_anagram(strs: List[str]) -> List[List[str]]:
    ht = {}
    for val in strs:
        key = str(sorted(val))
        if key in ht:
            ht[key].append(val)
        else:
            ht[key] = [val]
    return list(ht.values())

def my_group_anagram_01(strs: List[str]) -> List[List[str]]:
    ht = defaultdict(list)
    for val in strs:
        key = tuple(sorted(val))
        ht[key].append(val)

    return list(ht.values())

def my_group_anagram_02(strs: List[str]) -> List[List[str]]:
    ht = defaultdict(list)
    for val in strs:
        key = "".join(sorted(val))
        ht[key].append(val)

    return list(ht.values())

def my_group_anagram_03(strs: List[str]) -> List[List[str]]:
    ht = defaultdict(list)
    for s in strs:
        char_freq = [0]*26
        for char in s:
            char_freq[ord(char) - ord('a')] += 1
        ht[tuple(char_freq)].append(s)
    
    return list(ht.values())

def pipeline_check(func: function) -> str:
    strs_1 = ["eat","tea","tan","ate","nat","bat"]
    strs_2 = [""]
    strs_3 = ["a"]
    return f'1) -> {func(strs_1)}\n2) -> {func(strs_2)}\n3) -> {func(strs_3)}'


print(pipeline_check(my_group_anagram_03))