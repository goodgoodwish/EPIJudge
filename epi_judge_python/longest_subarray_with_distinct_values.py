from test_framework import generic_test


def longest_subarray_with_distinct_entries(A):
    # TODO - you fill in here.
    last_pos = {}
    sub_len = -float("inf")
    start_idx = 0
    for i, el in enumerate(A):
        if el in last_pos and last_pos[el] >= start_idx:
            start_idx = last_pos[el] + 1
        last_pos[el] = i
        sub_len = max(sub_len, i - start_idx + 1)
    return sub_len


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
