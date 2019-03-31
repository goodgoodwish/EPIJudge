import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

import collections
def find_smallest_subarray_covering_set(paragraph, keywords):
    # TODO - you fill in here.
    result = Subarray(-1, -1)
    t_el_cnt = dict(collections.Counter(keywords))
    win_el_cnt = {}
    required = len(t_el_cnt)
    formed = 0
    left = 0
    min_len = float("inf")

    for right, el in enumerate(paragraph):
        if el not in t_el_cnt:
            continue
        win_el_cnt[el] = win_el_cnt.get(el, 0) + 1
        if win_el_cnt[el] == t_el_cnt[el]:
            formed += 1
        while formed == required:
            if right - left < min_len:
                result = Subarray(left, right)
            el = paragraph[left]
            if el in t_el_cnt:
                if win_el_cnt[el] == t_el_cnt[el]:
                    formed -= 1
                win_el_cnt[el] -= 1
            left += 1
    return result


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))
