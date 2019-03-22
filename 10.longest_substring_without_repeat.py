# Given a string, find the length of the longest substring without repeating
# characters.
#
# For example, the longest substring without repeating letters for
# "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.
#
# Time:  O(n)
# Space: O(1)

import argparse
from collections import defaultdict


class Solution:
    @staticmethod
    def length_of_longest_substring(s):
        longest, start, visited = 0, 0, [False for _ in range(256)]
        for i, char in enumerate(s):
            while visited[ord(char)]:
                visited[ord(char)] = False
                start += 1
            visited[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest

    @staticmethod
    def length_of_longest_substring2(s):
        lookup, start, longest = defaultdict(lambda: -1), 0, 0
        for idx, char in enumerate(s):
            if lookup[char] >= start:
                start = lookup[char] + 1
            lookup[char] = idx
            longest = max(longest, idx - start + 1)
        return longest


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--str', dest='str', required=True,
                        help='a string')
    args = parser.parse_args()
    print(Solution().length_of_longest_substring2(args.str))
