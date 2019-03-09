# Time:  O(n)
# Space: O(logn)
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# Definition for a  binary tree node

import argparse
from model import TreeNode
from helper import get_linked_list_from_list, in_order_depth_first_traversal


class Solution:
    current = None

    def sorted_list_to_bst(self, head):
        current, length = head, 0
        while current is not None:
            current = current.next
            length += 1
        self.current = head
        return self.sorted_list_to_bst_helper(0, length - 1)

    def sorted_list_to_bst_helper(self, start, end):
        if start > end:
            return None
        mid = start + (end - start) // 2
        left = self.sorted_list_to_bst_helper(start, mid - 1)
        parent = TreeNode(self.current.val)
        parent.left = left
        self.current = self.current.next
        right = self.sorted_list_to_bst_helper(mid + 1, end)
        parent.right = right
        return parent


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', dest='list', required=True, nargs='+',
                        type=int, help='list of integer')

    args = parser.parse_args()
    ll = get_linked_list_from_list(args.list)

    result = Solution().sorted_list_to_bst(ll)
    print(in_order_depth_first_traversal(result))
