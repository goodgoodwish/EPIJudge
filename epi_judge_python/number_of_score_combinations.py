from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    # TODO - you fill in here.
    n = final_score
    nums = individual_play_scores
    m = len(nums)
    f = [1] + [0] * n
    for i in range(m):
        for j in range(1, n + 1):
            no_num = f[j] if i >= 1 else 0
            with_num = f[j - nums[i]] if j >= nums[i] else 0
            f[j] = no_num + with_num
    return f[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
