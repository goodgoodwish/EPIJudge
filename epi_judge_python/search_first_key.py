from test_framework import generic_test


def search_first_of_k(A, k):
    if not A:
        return -1
    start = 0
    end = len(A)
    while start < end:
        mid = start + (end - start)//2
        if A[mid] < k:
            start = mid + 1
        elif A[mid] > k:
            end = mid
        else:
            end = mid

    if end < len(A) and A[end] == k:
        return end # start
    return -1

# 1, 3,3,3, 5

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
