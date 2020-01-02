# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that
# they add up to the target, where index1 must be less than index2.
# Please note that your returned answers (both index1 and index2) are not
# zero-based.
#
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
#

# Time:  O(n)
# Space: O(1)


import argparse


class Solution(object):
    @staticmethod
    def two_sum(nums, target):
        idx1, idx2 = 0, len(nums) - 1
        while idx1 < idx2:
            sum_ = nums[idx1] + nums[idx2]
            if sum_ > target:
                idx2 -= 1
            elif sum_ < target:
                idx1 += 1
            else:
                return idx1 + 1, idx2 + 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', dest='list', required=True, nargs='+',
                        type=int, help='list of integer')
    parser.add_argument('--target', dest='target', required=True,
                        type=int, help='target number')

    args = parser.parse_args()
    print(Solution().two_sum(args.list, args.target))
