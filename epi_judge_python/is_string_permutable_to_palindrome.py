from test_framework import generic_test

from collections import Counter
def can_form_palindrome(s):
    # TODO - you fill in here.
    # return sum([v % 2 for _, v in Counter(s).items()]) <= 1
    char_cnt = [0] * 256
    for c in s:
        char_cnt[ord(c)] += 1
    if sum([v % 2 for v in char_cnt]) <= 1:
        return True 
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
