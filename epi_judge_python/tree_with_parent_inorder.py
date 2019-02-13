from test_framework import generic_test


def inorder_traversal(tree):
    node = tree 
    results, prev = [], None 
    while node:
        if prev is node.parent:
            while node.left:
                node = node.left
            results.append(node.data)
            next = node.right or node.parent
        elif prev is node.left:
            results.append(node.data)
            next = node.right or node.parent
        else:
            next = node.parent
        prev = node 
        node = next
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
