# Design and implement a TwoSum class. It should support the following
# operations: add and find.
#
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the
# value.
#
# For example,
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
# Time:  O(n)
# Space: O(n)


import argparse
from collections import defaultdict


class TwoSum(object):

    def __init__(self):
        self.data = defaultdict(int)

    def add(self, number):
        self.data[number] += 1

    def find(self, target):
        for key in self.data:
            num = target - key
            if num in self.data and (num != key or self.data[key] > 1):
                return True
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', dest='list', required=True, nargs='+',
                        type=int, help='list of integer')
    parser.add_argument('--target', dest='target', required=True,
                        type=int, help='target number')

    args = parser.parse_args()

    s = TwoSum()
    for i in args.list:
        s.add(i)

    print(s.find(args.target))
