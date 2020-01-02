# Time:  O(m * n)
# Space: O(m + n)
#
# A robot is located at the top-left corner of a m x n grid
# (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid
# (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
# Note: m and n will be at most 100.
#


class Solution:
    @staticmethod
    def unique_paths(m, n):
        matrix = [[1] * n] * m
        for r in reversed(range(m-1)):
            for c in reversed(range(n-1)):
                matrix[r][c] = matrix[r + 1][c] + matrix[r][c + 1]
        return matrix[0][0]


if __name__ == "__main__":
    print(Solution().unique_paths(5, 7))
