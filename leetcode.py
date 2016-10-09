# Singly-Linked List
class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None


# Doubly-Linked List
class DLLNode:
    def __init__(self, v):
        self.val = v
        self.next = None
        self.prev = None


# Binary-Tree Node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pair_sum(nums, target):  # 1: Array & Hash
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # partial sums, compare with target - n
    partials = {}

    for i, n in enumerate(nums):
        if n in partials:  # found soul mate
            return [partials[n], i]  # indices
        else:  # post profile  # describe soul mate
            partials[target - n] = i
    else:
        return None


def add_lists_reversed(*xs):  # 2: LL
    """
    :type xs: List[ListNode]
    :rtype: ListNode
    """
    total, carry = 0, 0
    head = ListNode(0)
    cur = head
    ns = [*xs]

    while any(ns):
        total = carry
        for i, xs in enumerate(ns):
            if xs:
                total += xs.val
                ns[i] = xs.next

        carry = total // 10
        total -= carry * 10
        cur.next = ListNode(total)
        cur = cur.next
    if carry:  # extra digit at the end
        cur.next = ListNode(carry)

    return head.next


def len_longest_distinct_substr(s):  # 3: sliding window
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    start = 0
    max_len = 0
    pos = {}

    for i, c in enumerate(s + s[-1]):
        if c in pos and pos[c] >= start:  # must remove previous occurrence of c
            max_len = max(max_len, i - start)
            start = pos[c] + 1
        pos[c] = i

    return max_len
