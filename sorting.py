

def sort_bubble(xs):
    """ invariant: after nth pass, last n elements sorted """
    for last in reversed(range(len(xs))):
        in_order = True

        for cur in range(last):
            if xs[cur] > xs[cur + 1]:  # out of order, then swap
                xs[cur], xs[cur + 1] = xs[cur + 1], xs[cur]
                in_order = False

        if in_order:
            break

    return xs
# print(sort_bubble([5, 4, 3, 2, 1]))


def sort_selection(xs):
    """ invariant: after nth pass, first n elements sorted """
    n = len(xs)

    for start in range(n):
        # for each position, find minimum in sub-array
        pos_min = start
        for cur in range(start, n):
            if xs[cur] < xs[pos_min]:  # smaller value found
                pos_min = cur

        xs[pos_min], xs[start] = xs[start], xs[pos_min]

    return xs
# print(sort_selection([1, 4, 5, 2, 188, 9]))


def sort_insertion(xs):
    n = len(xs)

    for i in range(1, n):
        j = i - 1
        while xs[i] < xs[j] and j >= 0:
            j -= 1

        if xs[i] < xs[j + 1]:  # out of order
            temp = xs[i]
            k = i
            while k > j:
                xs[k] = xs[k-1]
                k -= 1

            xs[j + 1] = temp
        print(xs)
    return xs
#print(sort_insertion([1, 5, 3, 6, 2]))


def merge(xs, ys):
    INF = float('inf')
    xs.append(INF)
    ys.append(INF)
    i, j = 0, 0
    merged = []
    for k in range(len(xs) + len(ys) - 2):
        # print(merged)
        if xs[i] < ys[j]:
            merged.append(xs[i])
            i += 1
        else:
            merged.append(ys[j])
            j += 1
    return merged


def sort_merge(xs):
    if len(xs) < 2:
        return xs

    mid = len(xs) // 2
    left, right = xs[:mid], xs[mid:]  # second half is bigger if odd
    return merge(sort_merge(left), sort_merge(right))
# print(sort_merge([1, 5, 3, 6, 2]))


def sort_quick(xs):
    # choose pivot to be median of first, middle, and last
    n = len(xs)
    if n <= 1:
        return xs
    else:
        pivot = sorted([xs[0], xs[-1], xs[n // 2]])[1]

        end_left = 0
        start_right = n - 1
        for i in range(n):
            if xs[i] < pivot:
                if i > end_left:  # LLRL -> LLLR
                    xs[i], xs[end_left] = xs[end_left], xs[i]
                end_left += 1
            elif xs[i] > pivot:  # greater than pivot
                if i < start_right:
                    xs[i], xs[start_right] = xs[start_right], xs[i]
                start_right -= 1

        print(xs, pivot)
        return sort_quick(xs[:end_left]) + sort_quick(xs[end_left:])
print(sort_quick([1, 5, 3, 6, 2]))
