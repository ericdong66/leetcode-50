# Find the contiguous subarray within an array (containing at least one number)
# which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
#
# Time:  O(n)
# Space: O(1)


class Solution:
    @staticmethod
    def max_product_subarray(li):
        global_max, local_max, local_min = float("-inf"), 1, 1
        for x in li:
            local_max = max(x, local_max * x, local_min * x)
            local_min = min(x, local_max * x, local_min * x)
            global_max = max(global_max, local_max)
        return global_max


if __name__ == "__main__":
    print(Solution().max_product_subarray([2, 3, -2, 4]))
    print(Solution().max_product_subarray([-4, -3]))
