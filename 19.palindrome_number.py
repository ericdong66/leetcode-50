# Determine whether an integer is a palindrome. Do this without extra space.
#
# Some hints:
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction
# of using extra space.
#
# You could also try reversing an integer. However, if you have solved the
# problem "Reverse Integer", you know that the reversed integer might overflow.
# How would you handle such case?
#
# There is a more generic way of solving this problem.
#
# Time:  O(1)
# Space: O(1)

import argparse


class Solution:
    @staticmethod
    def is_palindrome(x):

        if x < 0:
            return False

        div = 1
        while x // div > 10:
            div *= 10

        while x != 0:
            print(x, div)
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x % div) // 10
            div //= 100

        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--number', dest='number', required=True, type=int,
                        help='a number')

    args = parser.parse_args()
    print(Solution().is_palindrome(args.number))
