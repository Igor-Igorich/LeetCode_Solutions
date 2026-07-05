
def roman_to_int(s):
    result = 0
    alphabet = dict(zip(['I', 'V', 'X', 'L', 'C', 'D', 'M'], [1, 5, 10, 50, 100, 500, 1000]))
    for i in range(len(s)):
        if (i < len(s) - 1) and (alphabet[s[i]] < alphabet[s[i + 1]]):
            result -= alphabet[s[i]]
        else:
            result += alphabet[s[i]]
    return result


s = input('Enter a Roman number: ')
print(roman_to_int(s))
