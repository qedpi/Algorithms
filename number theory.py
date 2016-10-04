# number theory
from functools import reduce


def gcd(a, b):
    # invariant: d | a and d | b -> d | a % b
    if not b:
        return a
    else:
        return gcd(b, a % b)


def gcdb(a, b):  # binary gcd
    if not b or a == b:
        return a
    else:
        aeven, beven = not a % 2, not b % 2

        if aeven and beven:  # extract a factor of 2
            return 2 * gcdb(a // 2, b // 2)
        elif aeven:
            return gcdb(a // 2, b)
        elif beven:
            return gcdb(a, b // 2)
        else:  # both odd
            b, a = sorted([a, b])
            return gcdb((a - b) // 2, b)


def gcdn(xs):
    return reduce(gcd, xs)


def lcm(a, b):
    return a // gcd(a, b) * b


def lcmn(xs):
    return reduce(lcm, xs)


