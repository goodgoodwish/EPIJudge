from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A):
    # TODO - you fill in here.
    n = len(A)
    f = [1] * n
    for r in range(n):
        for l in range(r):
            if A[l] <= A[r]:
                f[r] = max(f[l] + 1, f[r])
    return max(f)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_nondecreasing_subsequence.py",
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
