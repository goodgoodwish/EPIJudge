from test_framework import generic_test

import collections 
def binary_tree_depth_order(tree):
    results = []
    q = collections.deque([tree])
    while q:
        n = len(q)
        level_nodes = []
        for _ in range(n):
            node = q.popleft()
            if not node:
                continue 
            level_nodes.append(node.data)
            q.append(node.left)
            q.append(node.right)
        if level_nodes:
            results.append(level_nodes)

    return results 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
