# Given a non-negative integer represented as a non-empty array of digits,
# plus one to the integer. You may assume the integer do not contain any leading
# zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of
# the list.
#
# Time:  O(n)
# Space: O(1)

import argparse


class Solution(object):
    @staticmethod
    def plus_one(digits):
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', dest='list', required=True, nargs='+',
                        type=int, help='list of integer')

    args = parser.parse_args()
    print(Solution().plus_one(args.list))
