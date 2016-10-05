from math import factorial, floor, ceil

# to add efficient exponentiation


def floorg(x, interval):
    return x // interval * interval


def ceilg(x, interval):
    return ceil(x // interval) * interval


def fact(n):
    def loop(n, acc):  # tail recursive
        if not n:
            return 1
        else:
            return loop(n - 1, n * acc)
    loop(n, 1)




