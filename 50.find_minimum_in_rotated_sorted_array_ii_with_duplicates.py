# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# The array may contain duplicates.
#
# Time:  O(logn) ~ O(n)
# Space: O(1)


class Solution(object):
    @staticmethod
    def find_min(nums):
        left, right = 0, len(nums) - 1
        while left < right and nums[left] >= nums[right]:

            mid = (right + left) // 2

            if nums[mid] == nums[left]:
                left += 1
            elif nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1

        return nums[left]


if __name__ == "__main__":
    print(Solution().find_min([3, 1, 1, 2, 2, 3]))
