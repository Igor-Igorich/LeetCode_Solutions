
def remove_duplicates(nums: list[int]) -> tuple:
    idx_to_insert = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[idx_to_insert - 1]:
            nums[idx_to_insert], nums[i] = nums[i], nums[idx_to_insert]
            idx_to_insert += 1
    return (nums, idx_to_insert)


M = [int(i) for i in input('Enter the array elements separated by a space: ').split()]
print(remove_duplicates(M))
