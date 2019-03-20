# Given a sorted integer array where the range of elements are [lower, upper]
# inclusive, return its missing ranges.
#
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# return ["2", "4->49", "51->74", "76->99"].
#
# Time:  O(n)
# Space: O(1)

import argparse


class Solution(object):

    def get_range(self, lower, upper):
        if lower == upper:
            return "{}".format(lower)
        else:
            return "{}->{}".format(lower, upper)

    def find_missing_ranges(self, nums, lower, upper):
        ranges = []
        pre = lower - 1

        for i in range(len(nums) + 1):
            if i == len(nums):
                cur = upper + 1
            else:
                cur = nums[i]
            if cur - pre >= 2:
                ranges.append(self.get_range(pre + 1, cur - 1))

            pre = cur

        return ranges

    def missing(self, nums):
        result = list()
        if not nums:
            return result

        pre = nums[0]
        for cur in nums[1:]:
            if cur - pre >= 2:
                result.append(self.get_range(pre+1, cur-1))
            pre = cur
        return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', dest='list', required=True, nargs='+',
                        type=int, help='list of integer')
    parser.add_argument('--lower', dest='lower', required=True, type=int,
                        help='lower boundary')
    parser.add_argument('--upper', dest='upper', required=True, type=int,
                        help='upper boundary')

    args = parser.parse_args()
    # print(Solution().find_missing_ranges(args.list, args.lower, args.upper))
    print(Solution().missing(args.list))
