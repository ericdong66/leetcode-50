# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
# click to show clarification.
#
# Clarification:
# What constitutes a word?
# A sequence of non-space characters constitutes a word.
# Could the input string contain leading or trailing spaces?
# Yes. However, your reversed string should not contain leading or trailing
# spaces.
#
# How about multiple spaces between two words?
# Reduce them to a single space in the reversed string.
#
# Time:  O(n)
# Space: O(n)

import argparse


class Solution:
    @staticmethod
    def reverse_words(s):
        return ' '.join(s.split()[::-1])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--str', dest='str', required=True,
                        help='a string')

    args = parser.parse_args()
    print(Solution().reverse_words(args.str))
