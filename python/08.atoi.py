# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases. If you want a challenge,
# please do not see below and ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely
#  (ie, no given input specs).
# You are responsible to gather all the input requirements up front.
#
# spoilers alert... click to show requirements for atoi.
#
# Requirements for atoi:
# The function first discards as many whitespace characters as necessary
# until the first non-whitespace character is found. Then, starting from this
# character, takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that
# form the integral number, which are ignored and have no effect on the behavior
#  of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is empty or
# it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
# If the correct value is out of the range of representable values,
# INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
#
# Time:  O(n)
# Space: O(1)

import argparse


class Solution(object):
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    def my_atoi(self, s):

        result = 0
        if not s:
            return result

        i = 0
        while i < len(s) and s[i].isspace():
            i += 1

        if len(s) == i:
            return result

        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        while i < len(s) and '0' <= s[i] <= '9':
            if result * 10 + int(s[i]) > self.INT_MAX:
                return self.INT_MAX if sign > 0 else self.INT_MIN
            result = result * 10 + int(s[i])
            i += 1

        return sign * result


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--str', dest='str', required=True,
                        help='a string')
    args = parser.parse_args()

    print(Solution().my_atoi(args.str))
