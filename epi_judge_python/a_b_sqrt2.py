from test_framework import generic_test

from sortedcontainers import SortedSet 
import math
def generate_first_k_a_b_sqrt2(k):
    # TODO - you fill in here.
    def ab_sqt2(a, b):
        return a + b * math.sqrt(2)
    a, b = 0, 0
    val = ab_sqt2(a, b)
    bst = SortedSet([(val, a, b)])
    res = []
    while len(res) < k:
        val, a, b = bst.pop(0)
        res.append(val)
        bst.add((ab_sqt2(a + 1, b), a + 1, b))
        bst.add((ab_sqt2(a, b + 1), a, b + 1))
    return res 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("a_b_sqrt2.py", 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))






