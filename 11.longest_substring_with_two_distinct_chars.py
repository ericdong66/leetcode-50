# Given a string, find the length of the longest substring T
# that contains at most 2 distinct characters.
#
# For example, Given s = "eceba",
#
# T is "ece" which its length is 3.
#
# Time:  O(n)
# Space: O(1)

import argparse


class Solution:
    @staticmethod
    def length_of_longest_substring(s):
        longest, start, pre = 0, 0, -1
        for cur in range(1, len(s)):
            if s[cur] == s[cur - 1]:
                continue
            if pre >= 0 and s[cur] != s[pre]:
                longest = max(longest, cur - start)
                start = pre + 1
            pre = cur - 1
        longest = max(longest, len(s) - start)
        return longest


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--str', dest='str', required=True,
                        help='a string')
    args = parser.parse_args()
    print(Solution().length_of_longest_substring(args.str))
