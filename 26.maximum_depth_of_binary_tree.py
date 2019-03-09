# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
#

import argparse
from helper import get_tree_from_list


class Solution:
    def max_depth(self, root):
        if root is None:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--tree', dest='tree', required=True, nargs='+',
                        type=int,
                        help='list, represent a breadth first traversal tree')

    args = parser.parse_args()
    root_node = get_tree_from_list(args.tree)
    print(Solution().max_depth(root_node))
