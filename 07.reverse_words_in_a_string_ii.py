# Time: O(n)
# Space:O(1)
#
# Given an input string, reverse the string word by word.
# A word is defined as a sequence of non-space characters.
#
# The input string does not contain leading or trailing spaces
# and the words are always separated by a single space.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
# Could you do it in-place without allocating extra space?
#

import argparse


class Solution(object):
    def reverse_words(self, s):
        self.reverse(s, 0, len(s) - 1)
        i = 0
        for j in range(len(s) + 1):
            if j == len(s) or s[j] == ' ':
                self.reverse(s, i, j - 1)
                i = j + 1

    @staticmethod
    def reverse(s, begin, end):
        for i in range((end - begin) // 2):
            s[begin + i], s[end - i] = s[end - i], s[begin + i]


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--str', dest='str', required=True,
                        help='a string')
    args = parser.parse_args()

    s = [c for c in args.str]
    Solution().reverse_words(s)
    print(''.join(s))
