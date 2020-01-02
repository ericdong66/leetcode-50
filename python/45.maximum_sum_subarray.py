# Find the contiguous subarray within an array (containing at least one number)
# which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
#
#
#
# Time:  O(n)
# Space: O(1)


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)
        global_max, local_max = 0, 0
        for x in nums:
            local_max = max(0, local_max + x)
            global_max = max(global_max, local_max)
        return global_max


if __name__ == "__main__":

    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    print(Solution().maxSubArray([-2, 2]))
