

def search_linear(target, xs):
    # also: target in xs
    for x in xs:
        if x == target:
            return True
    else:
        return False
# print(search_linear(5, [0, -5, 3]))


def search_linear_pos(target, xs):
    for i, x in enumerate(xs):
        if x == target:
            return i
    else:
        return False
# print(search_linear_pos(5, [0, 5, 3]))


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

