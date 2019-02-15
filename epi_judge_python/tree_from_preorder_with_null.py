import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from binary_tree_node import BinaryTreeNode
def reconstruct_preorder(preorder):
    def build_tree(node_iter):
        curt_data = next(node_iter)
        if curt_data is None:
            return
        left_tree = build_tree(node_iter)
        right_tree = build_tree(node_iter)
        return BinaryTreeNode(data=curt_data, left = left_tree, right = right_tree)
    tree = build_tree(iter(preorder))
    return tree


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_with_null.py",
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
