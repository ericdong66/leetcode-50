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


class TwoSum(object):

    def __init__(self):
        self.data = set()

    def add(self, number):
        self.data.add(number)

    def find(self, target):
        lookup = dict()
        for idx, n in enumerate(self.data):
            if target - n in lookup:
                return True
            lookup[n] = idx
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', dest='list', required=True, nargs='+',
                        help='list of integer')
    parser.add_argument('--target', dest='target', required=True,
                        help='target number')

    args = parser.parse_args()

    s = TwoSum()
    for i in [int(i) for i in args.list]:
        s.add(i)

    print(s.find(int(args.target)))
