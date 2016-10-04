

def search_linear(target, xs):
    # also: target in xs
    for x in xs:
        if x == target:
            return True
    else:
        return False


def search_binary(target, xs):
    low, high = 0, len(xs)

    while low <= high:
        mid = low + (high - low) // 2
        cur = xs[mid]
        if cur < target:
            low = mid + 1
        elif cur > target:
            high = mid - 1
        else:
            return mid

    return -1

