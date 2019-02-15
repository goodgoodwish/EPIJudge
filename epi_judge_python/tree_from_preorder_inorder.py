from test_framework import generic_test

from binary_tree_node import BinaryTreeNode
def binary_tree_from_preorder_inorder(preorder, inorder):
    n = len(preorder)
    val_idx = {v: i for i, v in enumerate(inorder)}

    def build_tree(pre_start, pre_end, in_start, in_end):
        if pre_start >= pre_end:
            return
        root_val = preorder[pre_start]
        root_idx = val_idx[root_val]
        left_size = root_idx - in_start

        root = BinaryTreeNode(data = root_val)
        root.left = build_tree(pre_start + 1, pre_start + left_size + 1, in_start, root_idx)
        root.right = build_tree(pre_start + left_size + 1, pre_end, root_idx + 1, in_end)
        return root

    # main
    root = build_tree(0, n, 0, n)
    return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
