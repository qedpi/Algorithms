import sys
sys.setrecursionlimit(30000)

from decorators import memoize


@memoize
def lcs_r(a, b):
    # find the longest common subsequence of a and b

    if not a or not b:
        return 0
    elif a[-1] == b[-1]:
        return 1 + lcs_r(a[:-1], b[:-1])
    else:
        return max(lcs_r(a[:-1], b), lcs_r(a, b[:-1]))


print(lcs_r("hellooaneihnoeatihhoaihnoahitnoaehtinhoaeioeathihnaoeihoeasihoeanihsoahsi",
            "mellowooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"))