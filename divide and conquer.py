from collections import Counter

from math import inf

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


def peaks_all(xs):
    xs = [-inf, *xs, -inf]

    peaks = []
    for i in range(1, len(xs) - 1):
        if xs[i - 1] <= xs[i] >= xs[i + 1]:  # is a local peak
            peaks.append(i)

    print(*(f'peak at {i - 1} with value {xs[i]}\n' for i in peaks))

peaks_all([1, 2, 5, 0, 1, 0])


def peak(xs):
    def search(low, high):
        print(low, high)
        mid = low + (high - low) // 2
        left, right = mid - 1, mid + 1
        if xs[mid] < xs[left]:
            search(low, left)
        elif xs[mid] < xs[right]:
            search(right, high)
        else:
            return mid, xs[mid]

    xs = [-inf, *xs, -inf]
    return search(0, len(xs) - 1)

print(peak([1, 2, 1, 0, 1, 0]))

'''
class UpDownHiking:
    def maxHeight(self, N, A, B):
        pivots = range(N)
        def payoff(i):
            return min(i * A, (N - i) * B)
        payoffs = map(payoff, pivots)

        return max(payoffs)
'''

'''
class LastDigit:
    def findX(self, S):
        S = int(S)

        def truncsum(n):
            powers = range(20)
            tens = map(lambda x: 10 ** x, powers)
            total = sum(map(lambda x: n // x, tens))
            return total

        low = 0
        high = 10 ** 19

        while low <= high:
            mid = (low + high) // 2
            t = truncsum(mid)
            if t < S:
                low = mid + 1
            elif t > S:
                high = mid - 1
            else:
                return mid

        return -1
'''

