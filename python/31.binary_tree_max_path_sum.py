# Given a binary tree, find the maximum path sum.
#
# The path may start and end at any node in the tree.
#
# For example:
# Given the below binary tree,
#
#        1
#       / \
#      2   3
# Return 6.
#
# Time:  O(n)
# Space: O(h), h is height of binary tree

import argparse
from helper import get_tree_from_list


class Solution(object):
    max_sum = float("-inf")

    def max_path_sum(self, root):
        self.max_path_sum_helper(root)
        return self.max_sum

    def max_path_sum_helper(self, root):
        if root is None:
            return 0
        left = max(0, self.max_path_sum_helper(root.left))
        right = max(0, self.max_path_sum_helper(root.right))
        self.max_sum = max(self.max_sum, root.val + left + right)
        print(root.val, max(left, right), self.max_sum)
        return root.val + max(left, right)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--tree', dest='tree', required=True, nargs='+',
                        type=int,
                        help='list, represent a breadth first traversal tree')

    args = parser.parse_args()
    root_node = get_tree_from_list(args.tree)
    print(Solution().max_path_sum(root_node))
