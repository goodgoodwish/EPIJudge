from test_framework import generic_test


def is_pattern_contained_in_grid(grid, S):
    # TODO - you fill in here.
    def dfs(grid, S, start, row, col, visited):
        if grid[row][col] != S[start]:
            return
        if start == len(S) - 1:
            return True 
        steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for step_r, step_c in steps:
            r1 = row + step_r 
            c1 = col + step_c 
            if r1 < 0 or r1 >= rows or c1 < 0 or c1 >= cols:
                continue
            ans = dfs(grid, S, start + 1, r1, c1, visited)
            if ans:
                return True

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    for r in range(rows):
        for c in range(cols):
            ans = dfs(grid, S, 0, r, c, visited)
            if ans:
                return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
