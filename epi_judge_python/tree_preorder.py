from test_framework import generic_test


def preorder_traversal(tree):
    results, s = [], []
    node = tree
    s = [node]
    while s:
        node = s.pop()
        if node:
            results.append(node.data)
            s += [node.right, node.left]
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))
