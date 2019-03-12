# There are n coins in a line. Two players take turns to take one or two coins
# from right side until there are no more coins left. The player who take the
# last coin wins.

# Could you please decide the first play will win or lose?


# Example
# n = 1, return true.
# n = 2, return true.
# n = 3, return false.
# n = 4, return true.
# n = 5, return true.

# Challenge
# O(n) time and O(1) memory


"""
class Solution {
public:
    /**
     * @param n: an integer
     * @return: a boolean which equals to true if the first player will win
     */
     bool firstWillWin(int n) {
        if (n <= 0) return false;
        if (n <= 2) return true;
        vector<bool> dp(n + 1, true);
        dp[3] = false;
        for (int i = 4; i <= n; ++i) {
            dp[i] = dp[i - 3];
        }
        return dp.back();
    }
};
"""


class Solution(object):
    @staticmethod
    def first_will_win(n):
        if n <= 0:
            return False
        if n <= 2:
            return True
        dp = [True] * (n + 1)
        dp[3] = False
        for i in range(4, n+1):
            dp[i] = dp[i-3]

        return dp[-1]


if __name__ == '__main__':
    print(Solution().first_will_win(1))
    print(Solution().first_will_win(2))
    print(Solution().first_will_win(3))
    print(Solution().first_will_win(4))
    print(Solution().first_will_win(5))
