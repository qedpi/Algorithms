import sys
sys.setrecursionlimit(999999999)

from decorators import memoize


coins = [2, 3, 5, 7]

@memoize
def coin_change_memo(total, num_used=len(coins)):
    if not total:
        return 0
    elif not num_used:
        return float('inf')  # impossible

    # choose to use first coin or not
    dont = coin_change_memo(total, num_used - 1)
    if total < coins[num_used - 1]:
        return dont
    else:
        used = coin_change_memo(total - coins[num_used - 1], num_used) + 1
        return min(used, dont)

# print(coin_change_memo(1000))


@memoize
def min_ops_to(target):
    # ops are inverse functions
    # currently fixed to: double, triple, or increment
    if target == 1:
        return 0
    elif target <= 0:
        return float('inf')
    else:
        choices = []
        fs = (lambda x: not x % 3, lambda y: not y % 2, lambda z: True)
        gs = (lambda x: x // 3, lambda y: y // 2, lambda z: z - 1)
        map(lambda f, g: choices.append(g(target)) if True else None, fs, gs)
        # print(*map(lambda f: choices.append(f(target)), fs))
        print(choices)

min_ops_to(5)