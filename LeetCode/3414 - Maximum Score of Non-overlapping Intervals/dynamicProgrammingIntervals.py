from typing import List


def count_before(sorted_intervals: List[List[int]], target) -> int:
    lo, hi = 0, len(sorted_intervals)
    while lo < hi:
        mid = (lo + hi) // 2
        if sorted_intervals[mid][1] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def better(a, b):
    if a[0] != b[0]:
        return a if a[0] > b[0] else b
    return a if a[1] < b[1] else b


def maximumWeight(intervals: List[List[int]]) -> List[int]:
    sorted_intervals = []
    for i, iv in enumerate(intervals):
        sorted_intervals.append([iv[0], iv[1], iv[2], i])

    sorted_intervals = sorted(sorted_intervals, key=lambda x: x[1])

    n = len(sorted_intervals)

    prev = []
    for i in range(n):
        prev.append(count_before(sorted_intervals, sorted_intervals[i][0]) - 1)

    dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for k in range(1, 5):
            skip = dp[i - 1][k]
            p = dp[prev[i - 1] + 1][k - 1]
            take = (p[0] + sorted_intervals[i - 1][2], sorted(p[1] + [sorted_intervals[i - 1][3]]))
            dp[i][k] = better(take, skip)

    return dp[n][4][1]
