
print((1, 0, 3))

def memoize(f):
    """ Memoization decorator for n-airy functions.
        Spec from Python decorator library """
    class MemoDict(dict):
        def __init__(self, func):
            self.func = func

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            result = self[key] = self.func(*key)
            return result

    return MemoDict(f)


def memoizex(f):
    """ Memoization decorator for unary functions.
        Spec of Python decorator library """
    # http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/
    class MemoDict(dict):
        def __missing__(self, key):
            result = self[key] = f(key)
            return result
    return MemoDict().__getitem__


@memoize
def foo(a, b, c=5):
    return a * b * c
