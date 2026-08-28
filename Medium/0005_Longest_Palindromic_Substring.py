def longest_palindrome_01(s: str) -> str:

    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s

    last_pal = s[0]
    left = right = 0

    while right < (len(s) - 1):

        right += 1
        if s[left] != s[right]:
            if right < (len(s) - 1):
                right += 1
                if s[left] != s[right]:
                    left += 1
                    if s[left] != s[right]:
                        right = left
                        continue
            else:
                continue

        i = 0
        while (
            ((left - i) > 0)
            and ((right + i) < (len(s) - 1))
            and (s[left - i - 1] == s[right + i + 1])
        ):

            i += 1

        if (right - left + 1) > len(last_pal):
            last_pal = s[left - i : right + i + 1]

        left += 1
        right = left

    return last_pal


def check(func):
    s_1 = "babad"
    s_2 = "cbbd"
    s_3 = "cbbbd"
    s_4 = "caba"
    s_5 = "aacabdkacaa"
    print(f"{s_1}: {func(s_1)}")
    print(f"{s_2}: {func(s_2)}")
    print(f"{s_3}: {func(s_3)}")
    print(f"{s_4}: {func(s_4)}")
    print(f"{s_5}: {func(s_5)}")


check(longest_palindrome_01)
