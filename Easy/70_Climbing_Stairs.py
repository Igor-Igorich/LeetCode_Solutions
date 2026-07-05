
def climb_stairs_tribute_to_Mozgunov(
        n: int,
        cur: int = 0
        ) -> int:
    if cur == n:
        return 1
    elif cur > n:
        return 0
    else:
        return climb_stairs_tribute_to_Mozgunov(n, cur + 1)\
                    + climb_stairs_tribute_to_Mozgunov(n, cur + 2)


def climb_stairs_iterative(
        n: int
        ) -> int:
    
    prev_1 = 1
    prev_2 = 0
    cur = 0
    
    for _ in range(1, n + 1):
        cur = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = cur
    
    return cur

print(climb_stairs_iterative(44))