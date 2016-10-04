

def fibonacci(n):
    def loop(n, a, b):
        if not n:
            return a
        else:
            return loop(n - 1, b, a + b)

    return loop(n, 0, 1)


