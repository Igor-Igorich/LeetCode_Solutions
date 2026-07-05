
def remove_element(nums: list[int], val: int) -> tuple:
    start_idx = 0
    while start_idx < len(nums) and nums[start_idx] != val:
        start_idx += 1
    idx_to_insert = start_idx
    for i in range(start_idx + 1, len(nums)):
        if nums[i] != val:
            nums[idx_to_insert], nums[i] = nums[i], nums[idx_to_insert]
            idx_to_insert += 1
    return (nums, idx_to_insert)

M = [int(i) for i in input('Enter the array elements separated by a space: ').split()]
print(remove_element(M, int(input('Enter value: '))))
