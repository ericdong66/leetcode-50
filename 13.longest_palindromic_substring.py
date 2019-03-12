# Time:  O(n^2)
# Space: O(n)

# Given a string s, find the longest palindromic subsequence's length in s.
# You may assume that the maximum length of s is 1000.
#
# Example 1:
####
# Input:
# "bbbab"
#
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
#
# Example 2:
####
# Input:
# "cbbd"
#
# Output:
# 2


class Solution(object):
    @staticmethod
    def longest_palindrome_sub_string(s):
        if s == s[::-1]:
            return len(s)

        dp = [[1] * len(s) for _ in range(2)]
        for i in reversed(range(len(s))):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i % 2][j] = 2 + dp[(i+1) % 2][j-1] if i+1 <= j-1 else 2
                else:
                    dp[i % 2][j] = max(dp[(i+1) % 2][j], dp[i % 2][j-1])
        return dp[0][-1]


if __name__ == '__main__':
    print(Solution().longest_palindrome_sub_string("bbbab"))
    print(Solution().longest_palindrome_sub_string("cbbd"))
