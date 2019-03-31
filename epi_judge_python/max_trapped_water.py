from test_framework import generic_test


def get_max_trapped_water(heights):
    # TODO - you fill in here.
    l, r = 0, len(heights) - 1
    res = 0
    while l < r:
        h = min(heights[l], heights[r])
        res = max(res, h * (r - l))
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return res 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_trapped_water.py",
                                       "max_trapped_water.tsv",
                                       get_max_trapped_water))
