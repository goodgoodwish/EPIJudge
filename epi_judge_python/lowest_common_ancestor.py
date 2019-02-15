import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree, node0, node1):
    def dfs(root, A, B):
        if not root:
            return
        if root is A or root is B:
            return root
        left_node = dfs(root.left, A, B)
        right_node = dfs(root.right, A, B)
        if left_node and right_node:
            return root
        if left_node:
            return left_node
        if right_node:
            return right_node
    return dfs(tree, node0, node1)


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
