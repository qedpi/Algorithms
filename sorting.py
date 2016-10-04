

def sort_bubble(xs):
    n = len(xs)
    in_order = False
    for i in range(n - 1):
        if in_order:
            break
        else:
            in_order = True

        for j in range(n - 1 - i):
            if xs[j] > xs[j + 1]:
                in_order = False
                xs[j], xs[j + 1] = xs[j + 1], xs[j]
    return xs


def sort_selection(xs):
    n = len(xs)

    for i in range(n - 1):
        for j in range(i + 1, n):
            x, y = xs[i], xs[j]
            if x > y:
                xs[i], xs[j] = y, x

    return xs


def sort_insertion(xs):
    n = len(xs)

    for i in range(1, n):
        j = i - 1
        while xs[i] < xs[j] and j:
            j -= 1

        if xs[i] < xs[j]:
            xs[i], xs[j] = xs[j], xs[i]

    return xs


print(sort_insertion([1, 5, 3, 6, 2]))

#print(sort_selection([1, 4, 5, 2, 188, 9]))

#print(sort_bubble([5, 4, 3, 2, 1]))