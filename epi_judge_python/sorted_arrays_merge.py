from test_framework import generic_test

from heapq import heappush, heappop 
def merge_sorted_arrays(sorted_arrays):
    res = []
    n = len(sorted_arrays)
    h = []
    it = [iter(arr) for arr in sorted_arrays]
    for i in range(n):
        heappush(h, (next(it[i]), i))
    while h:
        v, i = heappop(h)
        res.append(v)
        x = next(it[i], "#")
        if x != "#":
            heappush(h, (x, i))
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
