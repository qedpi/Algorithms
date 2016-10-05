
def fibonacci_r(n):
    if n <= 2:
        return 1
    else:
        return fibonacci_r(n - 1) + fibonacci_r(n - 1)


def fibonacci_tr(n):
    def loop(n, a, b):
        if not n:
            return a
        else:
            return loop(n - 1, b, a + b)

    return loop(n, 0, 1)


def fibonacci_it(n):
    a, b = 0, 1

    while n:
        n -= 1
        a, b = b, a + b

    return a


def sum_to_n(n):
    return n * (n + 1) // 2


def seriesa(start, step, steps):
    # finite arthimetic series
    return start + sum_to_n(step) * step


def seriesg(start, ratio, steps):
    # finite geometric series
    return start * ratio ** (steps + 1) // (ratio - 1)