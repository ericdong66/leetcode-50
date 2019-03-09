# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary
# tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
#
# Time:  O(n^2)
# Space: O(h), h is height of binary tree

import argparse
from helper import get_tree_from_list


class Solution(object):
    def is_balanced(self, root):
        if root is None:
            return True
        return abs(self.max_depth(root.left) - self.max_depth(root.right)) <= 1\
            and self.is_balanced(root.left) \
            and self.is_balanced(root.right)

    def max_depth(self, root):
        if root is None:
            return 0
        return max(self.max_depth(root.left),
                   self.max_depth(root.right)) + 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--tree', dest='tree', required=True, nargs='+',
                        type=int,
                        help='list, represent a breadth first traversal tree')

    args = parser.parse_args()
    root_node = get_tree_from_list(args.tree)
    print(Solution().is_balanced(root_node))
