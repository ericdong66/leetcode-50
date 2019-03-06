# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
#
# You may assume no duplicates in the array.
#
# Here are few examples.
# [1,3,5,6], 5 -> 2
# [1,3,5,6], 2 -> 1
# [1,3,5,6], 7 -> 4
# [1,3,5,6], 0 -> 0
#
# Time:  O(log(n))
# Space: O(1)

import argparse


class Solution(object):
    @staticmethod
    def search_insert(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] >= target:
                right = middle - 1
            else:
                left = middle + 1
        return left


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', dest='list', required=True, nargs='+',
                        help='list of integer')
    parser.add_argument('--target', dest='target', required=True,
                        help='target number')

    args = parser.parse_args()
    print(Solution.search_insert(args.list, args.target))
