# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root
# node down to the nearest leaf node.
#
# Time:  O(n)
# Space: O(h), h is height of binary tree


import argparse
from helper import get_tree_from_list


class Solution:
    @staticmethod
    def min_depth(root):
        if root is None:
            return 0

        queue = list()
        queue.append(root)
        right_most, depth = root, 1

        while queue:
            node = queue.pop(0)
            if node.left is None and node.right is None:
                break
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if node is right_most:
                depth += 1
                right_most = node.right or node.left

        return depth


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--tree', dest='tree', required=True, nargs='+',
                        type=int,
                        help='list, represent a breadth first traversal tree')

    args = parser.parse_args()
    root_node = get_tree_from_list(args.tree)

    print(Solution().min_depth(root_node))
