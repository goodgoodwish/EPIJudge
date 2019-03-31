from test_framework import generic_test


def find_kth_in_two_sorted_arrays(A, B, k):
    # TODO - you fill in here.
    # if len(A) > len(B):
    #     A, B = B, A
    n1, n2 = len(A), len(B)
    print(f" k {k} vs total {n1 + n2}, n1 {n1}, n2 {n2}")
    # if k > (n1 + n2):
    #     return
    start = max(0, k - n2)
    end = min(k, n1)
    MIN, MAX = -float("inf"), float("inf")
    while start < end:
        m1 = (start + end)//2
        m2 = k - m1
        print(f" m1 {m1} m2 {m2}, start {start} end {end} ")
        # R1 = MAX if m1 == n1 else A[m1]
        # L2 = MIN if m2 == 0 else B[m2 - 1]
        # if R1 < L2:
        if A[m1] < B[m2 - 1]:
            start = m1 + 1
        else:
            end = m1

    m1 = end
    m2 = k - m1
    L1 = MIN if m1 == 0 else A[m1 - 1]
    L2 = MIN if m2 == 0 else B[m2 - 1]
    return max(L1, L2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "kth_largest_element_in_two_sorted_arrays.py",
            'kth_largest_element_in_two_sorted_arrays.tsv',
            find_kth_in_two_sorted_arrays))
