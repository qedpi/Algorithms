
print((1, 0, 3))

def memoize(f):
    """ Memoization decorator for n-airy functions.
        Spec from Python decorator library """
    class MemoDict(dict):
        def __init__(self, f):
            super()
            self.f = f

        def __call__(self, *args, **kwargs):
            return self[args]

        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret

    return MemoDict(f)


def memoizex(f):
    """ Memoization decorator for unary functions.
        Spec of Python decorator library """
    # http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/
    class MemoDict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return MemoDict().__getitem__


