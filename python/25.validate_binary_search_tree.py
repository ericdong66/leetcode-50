# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's
# key. The right subtree of a node contains only nodes with keys greater than
# the node's key. Both the left and right subtrees must also be binary search
# trees.
#
# Time:  O(n)
# Space: O(1)

import argparse
from helper import get_tree_from_list


class Solution(object):

    def is_valid_bst(self, root):
        return self.is_valid_bst_recursive(root, float("-inf"), float("inf"))

    def is_valid_bst_recursive(self, node, low, high):
        if node is None:
            return True

        return low < node.val < high \
            and self.is_valid_bst_recursive(node.left, low, node.val) \
            and self.is_valid_bst_recursive(node.right, node.val, high)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--tree', dest='tree', required=True, nargs='+',
                        help='list, represent a breadth first traversal tree')

    args = parser.parse_args()
    root_node = get_tree_from_list([int(i) for i in args.tree])

    print(Solution().is_valid_bst(root_node))
