# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
# Time:  O(n)
# Space: O(n)


import argparse


class Solution(object):
    @staticmethod
    def two_sum(nums, target):
        lookup = dict()
        for idx, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in lookup:
                return lookup[num2], idx
            lookup[num1] = idx


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', dest='list', required=True, nargs='+',
                        type=int, help='list of integer')
    parser.add_argument('--target', dest='target', required=True,
                        type=int, help='target number')

    args = parser.parse_args()
    print(Solution().two_sum(args.list, args.target))
