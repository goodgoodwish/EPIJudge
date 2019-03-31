import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    # TODO - you fill in here.
    m = len(items)
    f = [[0] * (capacity + 1) for _ in range(2)]
    for i in range(m):
        for j in reversed(range(1, capacity + 1)):
            with_item_value = 0 if j < items[i].weight else items[i].value + f[(i - 1)%2][j - items[i].weight]
            no_item_value = f[(i - 1)%2][j]
            f[i%2][j] = max(with_item_value, no_item_value)

    return f[(m-1)%2][capacity]


@enable_executor_hook


def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
