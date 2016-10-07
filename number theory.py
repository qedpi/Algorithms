# number theory
from functools import reduce


# also from math import gcd, tail recursive
def gcd(a, b):
    # invariant: d | a and d | b -> d | a % b
    if not b:
        return a
    else:
        return gcd(b, a % b)


def odd(x):
    return x % 2


def even(x):
    return not x % 2


def gcd_b(a, b, acc=1):  # binary gcd
    if a < b:  # swap to make a geq b
        a, b = b, a

    if not b:  # base case
        return a * acc

    if even(a):
        a //= 2
        if even(b):
            b //= 2
            acc <<= 1
    else:
        if even(b):
            b //= 2
        else:
            a = (a - b) // 2

    return gcd_b(a, b, acc)
# print(gcd_b(12, 30))


def gcd_b_it(a, b, acc=1):  # binary gcd
    while b:  # base case not reached
        if a < b:  # swap to make a geq b
            a, b = b, a

        if even(a):
            a //= 2
            if even(b):
                b //= 2
                acc <<= 1
        else:
            if even(b):
                b //= 2
            else:
                a = (a - b) // 2
    return a * acc
# print(gcd_b_it(12, 30))


def gcd_it(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_n(xs):
    return reduce(gcd, xs)


def lcm(a, b):
    return a // gcd(a, b) * b


def lcm_n(xs):
    return reduce(lcm, xs)


def prime_sieve_range(n):
    # find primes up to n
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False

    primes = []
    for p in range(2, n + 1):
        if is_prime[p]:
            target = p ** 2
            primes.append(p)

            while target < n + 1:
                is_prime[target] = False
                target += p

    return primes


