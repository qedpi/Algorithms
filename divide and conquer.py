from collections import Counter


def majority_naive(xs):
    # O(n squared)
    unique_elements = [x for x in Counter(xs)]
    for x in unique_elements:
        if xs.count(x) > len(xs) // 2:
            return x
    else:
        return 'no majority element found'
# print(majority_naive([2, 4, 2, 3]))


def majority_divconq(xs):
    # O(n log n)
    # key idea: majority for the array will be majority for one half, thus, get candidates from there.

    #if len(xs) <
    pass