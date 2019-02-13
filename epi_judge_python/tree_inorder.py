from test_framework import generic_test


def inorder_traversal_01(tree):
    results = []
    s = []
    node = tree
    while s or node:
        while node:
            s.append(node)
            node = node.left
        if s:
            curt = s.pop()
            results.append(curt.data)
        node = curt.right
    return results

def inorder_traversal(tree):
    results = []
    s = []
    node = tree
    while s or node:
        if node:
            s.append(node)
            node = node.left
        else:
            curt = s.pop()
            results.append(curt.data)
            node = curt.right
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
