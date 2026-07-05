
def bad_longest_common_prefix(strs):
    strs_sort = sorted(strs, key=lambda x: len(x))
    prefix = strs_sort[0]
    for i in range(1, len(strs)):
        while prefix[len(prefix) - 1] != strs[i][len(prefix) - 1]:
            prefix = prefix[:-1]
            if prefix == "":
                return prefix
    return prefix

def longest_common_prefix(strs):
    strs_sort = sorted(strs)
    prefix = ""
    first = strs_sort[0]
    last = strs_sort[-1]
    i = 0
    while (i < len(first)) and (first[i] == last[i]):
        prefix += first[i]
        i += 1
    return prefix

print(longest_common_prefix(["flower","flow","flower"]))