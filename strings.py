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
# print(lcs_r("hellooaneihnoeatihhoaihnoahitnoaehtinhoaeioeathihnaoeihoeasihoeanihsoahsi", "mellowooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"))


def pattern_match_exact_naive(text, pattern):
    segments = len(text) - len(pattern) + 1
    matches = []

    for i in range(segments):
        if text[i:i + len(pattern)] == pattern:
            matches.append(i)

    return matches
# print(pattern_match_exact_naive('bananas', 'an'))


def pattern_match_multi_exact_naive(text, patterns):
    matches = {}
    for p in patterns:
        matches[p] = pattern_match_exact_naive(text, p)
    return matches
# print(pattern_match_multi_exact_naive('bananas', ['an', 'na']))


def prefix_trie_of_pattern(patterns):
    # build a trie from the patterns:
    trie = {}

    for p in patterns:
        pos = trie
        for c in p:
            if c not in pos:
                pos[c] = {}
            pos = pos[c]

    return trie


def trie_match(prefix, trie):
    for c in prefix:
        if trie:
            if c in trie:
                trie = trie[c]
            else:
                return False
        else:
            return True
    return True


def trie_match_multi(text, patterns):  # exact
    trie = prefix_trie_of_pattern(patterns)
    match = []
    # run each prefix of text through the trie
    for start in range(len(text)):
        match.append(trie_match(text[start:], trie))
        #print(text[start], sep=' ')

    return match
# print(trie_match_multi('panamabananas', ['banana', 'pan', 'and', 'nab', 'antenna', 'bandana', 'ananas', 'nana']))


def suffix_trie_text(text):
    from collections import deque
    text = deque(text)
    trie = {}
    start_pos = 0
    while text:
        pos = trie
        for i, c in enumerate(text):
            if c not in pos:
                pos[c] = {}

            if i == len(text) - 1:  # last character
                pos[c]['.'] = start_pos

            pos = pos[c]
        text.popleft()
        start_pos += 1

    return trie
# print(suffix_trie_text('abc'))


def num_leaves(tree):
    if type(tree) is not dict:
        return 1
    else:
        return sum(map(num_leaves, tree.values()))


def flatten(xs):
    return [item for sublist in xs for item in sublist]


def leaf_values(tree):
    if type(tree) is not dict:
        return [tree]
    else:
        return flatten([leaf_values(x) for x in tree.values()])


def suffix_trie_match(trie, pattern):
    for c in pattern:
        if c in trie:
            trie = trie[c]
        else:
            return []

    return leaf_values(trie)


def suffix_trie_match_patterns(text, patterns):
    trie = suffix_trie_text(text)
    matches = {}
    for p in patterns:
        matches[p] = suffix_trie_match(trie, p)
    print(trie)
    return matches


print(suffix_trie_match_patterns('banana', ['a']))


# Naive Burrows-Wheeler Transform
def bwt_naive(s):
    s += '$'

    rotations = []
    for i in range(len(s)):
        rotations.append(s[i:] + s[:i])

    rotations.sort()
    s_bwt = ''.join([s[-1] for s in rotations])
    return s_bwt
print(bwt_naive('banana'))


def bwt_inverse_naive(s):
    c_first, c_last = sorted(s), s
    pass




