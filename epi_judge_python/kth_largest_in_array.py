from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    def quick_select(A, start, end, k):
        if start > end:
            return
        if start == end == k:
            return A[k]
        left = start 
        right = end
        pivot = A[(left + right)//2]
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        if k <= right:
            return quick_select(A, start, right, k)
        if k >= left:
            return quick_select(A, left, end, k)
        return A[k]

    n = len(A)
    k = n - k
    result = quick_select(A, 0, n - 1, k)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
