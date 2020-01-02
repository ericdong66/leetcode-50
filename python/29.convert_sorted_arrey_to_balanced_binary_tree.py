# Given an array where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# Time:  O(n)
# Space: O(logn)

from model import TreeNode


class Solution(object):
    def sorted_array_to_bst(self, nums):
        return self.sorted_array_to_bst_recu(nums, 0, len(nums)-1)

    def sorted_array_to_bst_recu(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = TreeNode(nums[mid])
        node.left = self.sorted_array_to_bst_recu(nums, start, mid - 1)
        node.right = self.sorted_array_to_bst_recu(nums, mid + 1, end)
        return node


if __name__ == "__main__":
    num = [1, 2, 3]
    result = Solution().sorted_array_to_bst(num)
    print(result.val)
    print(result.left.val)
    print(result.right.val)
