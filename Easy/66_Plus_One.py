
def plus_one(digits: list[int]) -> list[int]:
    for i in range(len(digits) - 1, -1, -1):
        digits[i] = (digits[i] + 1) % 10
        if digits[i] != 0:
            return digits
    digits.insert(0, 1)
    return digits

digits = [int(i) for i in input('Enter number: ')]
print(plus_one(digits))