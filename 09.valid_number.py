# Validate if a given string is numeric.
#
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Note: It is intended for the problem statement to be ambiguous.
# You should gather all requirements up front before implementing one.
#
# Time:  O(n)
# Space: O(1)

import argparse


class Solution(object):
    @staticmethod
    def is_number(s):
        # zero or more leading space
        # optional sign
        # number with optional .number
        # option eE and trailing space
        regex_str = "^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$"
        import re
        return bool(re.match(regex_str, s))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--str', dest='str', required=True,
                        help='a string')
    args = parser.parse_args()

    print(Solution.is_number(args.str))
