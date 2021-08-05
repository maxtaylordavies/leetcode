import math


def longestCommonPrefix(self, strs):
    if not strs:
        return ""

    return lcp(strs, 0, len(strs) - 1)


def lcp(self, strs, l, r):
    if l == r:
        return strs[l]

    mid = math.floor((l + r) / 2)
    lcpLeft = lcp(strs, l, mid)
    lcpRight = lcp(strs, mid + 1, r)

    return commonPrefix(lcpLeft, lcpRight)


def commonPrefix(self, left, right):
    common = ""
    minLen = min(len(left), len(right))

    for i in range(minLen):
        if left[i] != right[i]:
            return common
        common += left[i]

    return common
