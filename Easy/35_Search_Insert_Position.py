
def binary_search_primary(
        lst: list[int],
        target: int
        ) -> int:
    lo = 0
    hi = len(lst)
    mid = lo + (hi - lo) // 2
    while lst[mid] != target:
        if lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid
        mid = lo + (hi - lo) // 2
    return mid


def binary_search(
        arr: list[int],
        target: int
        ) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        
        # print(f'mid = {mid}; low, high = {low, high}')

    return -1

def search_insert(
        arr: list[int],
        target: int
        ) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return low


arr = list(map(int, input('Enter array: ').split()))
target = int(input('Enter target: '))
print(f'Binary searche result: {binary_search(arr, target)}')
print(f'Correct result: {arr.index(target) if target in arr else -1}')
print(f'Search Insert result: {search_insert(arr, target)}')
