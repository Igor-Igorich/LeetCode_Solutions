'''
input_nums = input()
target = int(input())
input_nums = input_nums.replace('[', '').replace(']', '')
nums_orig = list(map(int, input_nums.split(',')))
nums_dupl = sorted([(x, idx) for idx, x in enumerate(nums_orig)])
answer = []

was_found = False
for i in range(len(nums_dupl) - 1):
    desired = target - nums_dupl[i][0]
    for j in range((i + 1), len(nums_dupl)):
        if nums_dupl[j][0] == desired:
            answer.append(nums_dupl[i][1])
            answer.append(nums_dupl[j][1])
            was_found = True
            break
        elif nums_dupl[j][0] > desired:
            break
    if was_found:
        break

print(answer)
'''

def find_sum(nums, target):
    hash_table = {}

    for idx, val in enumerate(nums):
        complement = target - val
        if complement in hash_table:
            return [hash_table[complement], idx]
        else:
            hash_table[val] = idx

print(find_sum([2, 7, 11, 15], 9))

