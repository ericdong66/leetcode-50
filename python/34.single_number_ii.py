# Time:  O(n)
# Space: O(1)
#
# Given an array of integers, every element appears three times except for one.
# Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it
# without using extra memory?

import argparse


class Solution(object):
    @staticmethod
    def single_number(nums):
        return (sum(set(nums)) * 3 - sum(nums)) // 2


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', dest='list', required=True, nargs='+',
                        help='list of integer', type=int)

    args = parser.parse_args()
    print(Solution().single_number(args.list))
