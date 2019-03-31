import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain, dictionary):
    # TODO - you fill in here.
    res = []
    s, dic = domain, dictionary 
    w = max([len(v) for v in dic or [""]])
    n = len(s)
    f = [-1] * n 
    for r in range(n):
        if r <= w and s[:r+1] in dic:
            f[r] = r + 1 
            continue 
        start = max(0, r - w)
        for l in range(start, r + 1):
            if f[l] > 0 and s[l+1: r+1] in dic:
                f[r] = r - l 
    if f[-1] == -1:
        return res
    r = n - 1
    while r >= 0:
        res.append(s[r - f[r] + 1: r + 1])
        r -= f[r]
    res.reverse()
    return res


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_decomposable_into_words.py",
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
