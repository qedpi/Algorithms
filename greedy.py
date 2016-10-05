

def greedy_coin_change(n, denoms=(1, 5, 10)):
    denoms = sorted(denoms, reverse=True)
    try_denom = 0
    coins_used = 0

    while n:
        while denoms[try_denom] <= n:
            n -= denoms[try_denom]
            coins_used += 1

        while denoms[try_denom] > n:
            try_denom += 1
            if try_denom == len(denoms):
                return -1 if n else coins_used
print(greedy_coin_change(19))


def knapsack_fractional(cap, ws, vs):
    val_densities = sorted([(v / w, w, v) for w, v in zip(ws, vs)])
    total_val = 0
    print(val_densities)
    while cap:
        best = val_densities.pop()
        take = min(cap, best[1])
        msg = f'take {take} from {best}'
        print(msg)

        cap -= take
        total_val += take * best[0]

    return total_val
# print(knapsack_fractional(10, [6, 7], [9, 11]))


# aka max revenue on ad placement
def max_prod_sum(xs, ys): # positive val only
    xs, ys = sorted(xs), sorted(ys)

    prod_sum = 0

    while xs and ys:
        prod_sum += xs.pop() * ys.pop()

    return prod_sum
# print(max_prod_sum([1, 6, 4], [7, 5, 3]))


# aka collecting signatures
def point_interval_coverage(intervals):
    from operator import itemgetter
    intervals.sort(key=itemgetter(1), reverse=True)
    visits = 0

    while intervals:
        last_visit = intervals.pop()[1]
        visits += 1
        while intervals and intervals[-1][0] <= last_visit:
            intervals.pop()

    return visits
# print(point_interval_coverage([(4, 5), (0, 2), (1, 3)]))


# aka grouping by interests
def interval_point_coverage(width, points):
    intervals = 0
    points.sort(reverse=True)
    while points:
        intervals += 1
        cover_until = points.pop() + width
        while points and points[-1] <= cover_until:
            points.pop()

    return intervals
# print(interval_point_coverage(2, [1, 5, 2]))


# aka max prize places for competition
def max_distinct_sum(n):
    # sum 1 to n is n (n + 1) / 2
    from math import floor
    best = floor((2 * n) ** .5 - .5)
    return best
# print(max_distinct_sum(8))


# aka maximize salary
def max_num_from_digits(n):
    s = "".join(sorted(str(n), reverse=True))
    return s
# print(max_num_from_digits(94619))


def max_num_from_nums(xs):
    from operator import itemgetter
    xs = sorted(['.'.join(str(x)) + '~' for x in xs])
    xs = [''.join(x[:-1].split('.')) for x in xs]
    return ''.join(reversed(xs))

print(max_num_from_nums([90, 9, 4, 42, 99]))