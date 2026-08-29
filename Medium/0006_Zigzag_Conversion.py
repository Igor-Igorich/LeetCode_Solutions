from math import ceil


def print_zigzag_beauty(s: str, num_rows: int) -> None:

    if num_rows == 1:
        print(s)
        return

    len_array = ceil(len(s) / (num_rows * 2 - 2)) * (num_rows - 1)
    res_array = [[" "] * len_array for _ in range(num_rows)]

    up = False
    i = 0
    j = 0
    idx = 0
    while idx < len(s):
        res_array[i][j] = s[idx]

        if up:
            j += 1
            i -= 1
            if i == 0:
                up = False
        else:
            i += 1
            if i == num_rows - 1:
                up = True

        idx += 1

    for arr in res_array:
        print("    ".join(arr))


def zigzag_convert(s: str, num_rows: int) -> str:

    if num_rows == 1:
        return s

    len_array = ceil(len(s) / (num_rows * 2 - 2)) * (num_rows - 1)
    res_array = [[""] * len_array for _ in range(num_rows)]

    up = False
    i = 0
    j = 0
    idx = 0
    while idx < len(s):
        res_array[i][j] = s[idx]

        if up:
            j += 1
            i -= 1
            if i == 0:
                up = False
        else:
            i += 1
            if i == num_rows - 1:
                up = True

        idx += 1

    ans = ""

    for arr in res_array:
        ans += "".join(arr)

    return ans


def zigzag_convert_easy(s: str, num_rows: int) -> str:

    if num_rows == 1 or num_rows >= len(s):
        return s

    res = ""
    shift = 2 * num_rows - 2
    for i in range(num_rows):
        idx = i

        while idx < len(s):
            res += s[idx]

            if 0 < i < num_rows - 1:
                mid = idx + shift - 2 * i
                if mid < len(s):
                    res += s[mid]

            idx = idx + shift

    return res


s_1 = "".join([chr(x) for x in range(ord("A"), ord("A") + 7)])
s_2 = "PAYPALISHIRING"
n_2 = 2

s = ""
n = 1
while True:

    s = input("Введите строку: ")
    n = int(input("Введите кол-во строк: "))

    if n == 0:
        break

    print_zigzag_beauty(s, n)
    print()
    print("Answer_1:", zigzag_convert(s, n))
    print()
    print("Answer_2:", zigzag_convert_easy(s, n))
    if zigzag_convert(s, n) != zigzag_convert_easy(s, n):
        print("FALSE")
