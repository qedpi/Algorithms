
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



