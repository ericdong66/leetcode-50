# Given an integer, convert it to a roman numeral.
#
# Input is guaranteed to be within the range from 1 to 3999.
#
# Time:  O(n)
# Space: O(1)

import argparse


class Solution(object):
    @staticmethod
    def int_to_roman(num):
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", \
                       10: "X", 40: "XL", 50: "L", 90: "XC", \
                       100: "C", 400: "CD", 500: "D", 900: "CM", \
                       1000: "M"}
        key_set, result = sorted(numeral_map.keys()), []
        while num > 0:
            for key in reversed(key_set):
                while num // key > 0:
                    num -= key
                    result.append(numeral_map[key])

        return "".join(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--number', dest='number', required=True, type=int,
                        help='a number')
    args = parser.parse_args()
    print(Solution().int_to_roman(args.number))
