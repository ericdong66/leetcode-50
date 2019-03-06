# Time:  O(n + k)
# Space: O(k)
#
# Implement str_str().
#
# Returns a pointer to the first occurrence of needle in haystack,
#  or null if needle is not part of haystack.
#

# Time:  O(n * k)
# Space: O(k)

import argparse


class Solution(object):
    @staticmethod
    def str_str(haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--haystack', dest='haystack', required=True,
                        help='haystack string')
    parser.add_argument('--needle', dest='needle', required=True,
                        help='needle string')

    args = parser.parse_args()

    print(Solution().str_str(args.haystack, args.needle))
