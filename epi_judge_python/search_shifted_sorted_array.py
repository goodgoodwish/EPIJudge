from test_framework import generic_test


def search_smallest(A):
    start = 0
    end = len(A)
    small_end = A[end - 1]
    while start < end:
        mid = start + (end - start)//2
        if A[mid] > small_end:
            start = mid + 1
        elif A[mid] <= small_end:
            end = mid

    return start # end



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
