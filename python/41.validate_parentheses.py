# Time:  O(n)
# Space: O(n)
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}"
# are all valid but "(]" and "([)]" are not.
#
import argparse


class Solution:
    @staticmethod
    def is_valid(s):
        stack = list()
        lookup = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for c in s:
            if c in lookup:
                stack.append(c)
            elif len(stack) == 0 or lookup[stack.pop()] != c:
                return False
        return len(stack) == 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--str', dest='str', required=True,
                        help='a statement to be validated')

    args = parser.parse_args()
    print(Solution.is_valid(args.str))
