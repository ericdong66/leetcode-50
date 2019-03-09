# Given a binary tree where all the right nodes are
# either leaf nodes with a sibling
# (a left node that shares the same parent node) or empty,
# flip it upside down and turn it into a tree
# where the original right nodes turned into left leaf nodes.
# Return the new root.
#
# For example:
# Given a binary tree {1,2,3,4,5},
#
#     1
#    / \
#   2   3
#  / \
# 4   5
#
# return the root of the binary tree [4,5,2,#,#,3,1].
#
#    4
#   / \
#  5   2
#     / \
#    3   1
#
# Time:  O(n)
# Space: O(1)

import argparse
from helper import get_tree_from_list, breadth_first_traversal


class Solution(object):
    @staticmethod
    def upside_down_binary_tree(root):
        current, parent, right_sibling = root, None, None

        while current:
            left = current.left
            current.left = right_sibling
            right_sibling = current.right
            current.right = parent
            parent = current
            current = left

        return parent


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--tree', dest='tree', required=True, nargs='+',
                        type=int,
                        help='list, represent a breadth first traversal tree')

    args = parser.parse_args()
    root_node = get_tree_from_list(args.tree)

    result = Solution().upside_down_binary_tree(root_node)
    print(breadth_first_traversal(result))
