from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import deque
class QueueWithMax:
    def __init__(self,):
        self.desc_q = deque()
        self.q = deque()

    def enqueue(self, x):
        self.q.append(x)
        while self.desc_q and x > self.desc_q[-1]:
            self.desc_q.pop()
        self.desc_q.append(x)

    def dequeue(self):
        x = self.q.popleft()
        if x >= self.desc_q[0]:
            self.desc_q.popleft()
        return x

    def max(self):
        if self.desc_q:
            return self.desc_q[0]
        return 


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_with_max.py",
                                       'queue_with_max.tsv', queue_tester))
