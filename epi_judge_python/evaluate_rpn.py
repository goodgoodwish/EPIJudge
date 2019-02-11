from test_framework import generic_test


def evaluate(expression):
    op = {
        "+" : lambda d1, d2 : d1 + d2,
        "-" : lambda d1, d2 : d1 - d2,
        "*" : lambda d1, d2 : d1 * d2,
        "/" : lambda d1, d2 : int(d1 / d2),
    }
    s = []
    for v in expression.split(","):
        if v in op:
            d2 = s.pop()
            d1 = s.pop()
            ans = op[v](d1, d2)
            s.append(ans)
            continue
        s.append(int(v))
    return s[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
