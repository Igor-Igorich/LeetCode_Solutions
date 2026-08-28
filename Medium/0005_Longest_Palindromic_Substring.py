def bad_longest_palindrome(s: str) -> str:

    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s

    last_pal = s[0]

    for center in range(len(s)):

        left = right = center
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > len(last_pal):
                last_pal = s[left : right + 1]
            left -= 1
            right += 1

        left = center
        right = center + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > len(last_pal):
                last_pal = s[left : right + 1]
            left -= 1
            right += 1

    return last_pal


def good_longest_palindrome(s: str) -> str:

    n = len(s)
    # 1. Мгновенная проверка на C-уровне Python
    if n <= 1 or s == s[::-1]:
        return s

    start, max_len = 0, 1
    i = 0

    while i < n:
        # 2. Ранняя остановка (Early Exit)
        # Если оставшийся хвост строки физически не может дать палиндром длиннее max_len
        if (n - i) <= max_len // 2:
            break

        l = r = i

        # 3. Схлопывание дубликатов (серии одинаковых букв "aaaaa")
        while r < n - 1 and s[r] == s[r + 1]:
            r += 1

        # Следующую проверку начинаем СРАЗУ после серии одинаковых букв
        i = r + 1

        # 4. Расширение от единого схлопнутого центра
        while r < n - 1 and l > 0 and s[r + 1] == s[l - 1]:
            r += 1
            l -= 1

        # Запоминаем максимум
        length = r - l + 1
        if length > max_len:
            start = l
            max_len = length

    return s[start : start + max_len]


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


check(good_longest_palindrome)
