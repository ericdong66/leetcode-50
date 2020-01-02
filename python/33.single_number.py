# Time:  O(n)
# Space: O(1)
#
# Given an array of integers, every element appears twice except for one.
# Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it
# without using extra memory?
#

import argparse


class Solution:
    @staticmethod
    def single_number(li):
        lookup = dict()
        for n in li:
            if lookup.get(n) is True:
                del lookup[n]
            else:
                lookup[n] = True
        return list(lookup.keys())[0]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', dest='list', required=True, nargs='+',
                        help='list of integer', type=int)

    args = parser.parse_args()
    print(Solution().single_number(args.list))
