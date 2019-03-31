from test_framework import generic_test


def find_nearest_repetition(paragraph):
    # TODO - you fill in here.
    result = float("inf")
    last_pos = {}
    for i, el in enumerate(paragraph):
        if el in last_pos:
            result = min(result, i - last_pos[el])
        last_pos[el] = i
    return result if result != float("inf") else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
