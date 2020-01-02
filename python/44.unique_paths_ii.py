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
    def unique_paths(m, n, obstacle_grid):
        matrix = [[1] * n] * m
        for r in reversed(range(m-1)):
            for c in reversed(range(n-1)):
                if obstacle_grid[r][c] == 1:
                    matrix[r][c] = 0
                else:
                    matrix[r][c] = matrix[r + 1][c] + matrix[r][c + 1]
        return matrix[0][0]


if __name__ == "__main__":
    obstacle_grid = [
                      [0, 0, 0],
                      [0, 1, 0],
                      [0, 0, 0]
                   ]
    print(Solution().unique_paths(len(obstacle_grid), len(obstacle_grid[0]),
                                  obstacle_grid))
