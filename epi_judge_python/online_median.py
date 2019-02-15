from test_framework import generic_test

from heapq import heappush, heappop, heappushpop

def online_median(sequence):
    big_min_h = []
    small_max_h = [] # negative -,
    res = []
    for v in sequence:
        x = heappushpop(big_min_h, v)
        heappush(small_max_h, -x)
        if len(big_min_h) < len(small_max_h):
            x = -heappop(small_max_h)
            heappush(big_min_h, x)
        res.append(big_min_h[0] 
            if len(big_min_h) > len(small_max_h) 
            else (big_min_h[0] - small_max_h[0]) * 0.5)

    return res


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
