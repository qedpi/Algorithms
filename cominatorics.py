from math import factorial, floor, ceil

# to add efficient exponentiation


def floorg(x, interval):
    return x // interval * interval


def ceilg(x, interval):
    return ceil(x // interval) * interval


def sum_to_n(n):
    return n * (n + 1) // 2


def seriesa(start, step, steps):
    # finite arthimetic series
    return start + sum_to_n(step) * step


def seriesg(start, ratio, steps):
    # finite geometric series
    return start * ratio ** (steps + 1) // (ratio - 1)


def fact(n):
    def loop(n, acc):  # tail recursive
        if not n:
            return 1
        else:
            return loop(n - 1, n * acc)
    loop(n, 1)




