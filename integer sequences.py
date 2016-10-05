import sys
sys.setrecursionlimit(999999999)

from functools import reduce
from operator import add

from decorators import memoizex


@memoizex
def fibonacci_r(n):
    if n <= 2:
        return 1
    else:
        return fibonacci_r(n - 1) + fibonacci_r(n - 2)


def fibonacci_tr(n, *, a=0, b=1):
    if not n:
        return a
    else:
        return fibonacci_tr(n - 1, a=b, b=a + b)


def fibonacci_it(n):
    a, b = 0, 1

    while n:
        n -= 1
        a, b = b, a + b

    return a


def sum_to_n_it(n):
    return sum(range(n + 1))


def sum_to_n_r(n):
    if not n:
        return 0
    else:
        return n + sum_to_n_r(n - 1)


def sum_to_n_tr(n, *, acc=0):
    if not n:
        return acc
    else:
        return sum_to_n_tr(n - 1, acc=acc + n)


def sum_to_n_e(n):
    return n * (n + 1) // 2


def sum_to_n_f(n):
    return reduce(add, range(n + 1))


def sum_to_n_b(n):
    return sum(range(n + 1))


def series_arith(start, step, steps):
    # finite arthimetic series
    return start + sum_to_n_e(step) * step


def series_geomet(start, ratio, steps):
    # finite geometric series
    return start * ratio ** (steps + 1) // (ratio - 1)


# variant examples

def fibo_mod_m_tr(n, a=0, b=1, m=10):
    if not n:
        return a
    else:
        return fibo_mod_m_tr(n - 1, a=b, b=(a + b) % m)


# use a general periodic detector decorator
def fibo_mod_m_it(n, m=10):
    a, b = 0, 1

    while n:
        n -= 1
        a, b = b, (a + b) % m

    return a
print(fibo_mod_m_it(327305))


# note that sum of Fn is F_n+2 - 1, instead we present the iterative method
def fibo_sum_tr(n, *, a=0, b=1, acc=0):
    if not n:
        return acc
    else:
        return fibo_sum_tr(n - 1, a=b, b=a + b, acc=acc + b)
print(fibo_sum_tr(18))


def fibo_partial_sum_tr(start, end):
    # both inclusive
    return fibo_sum_tr(end) - fibo_sum_tr(start - 1)

