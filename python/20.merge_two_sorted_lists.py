# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two
# lists.
#
# Time:  O(n)
# Space: O(1)

import argparse
from model import ListNode
from helper import get_linked_list_from_list


class Solution(object):
    @staticmethod
    def merge_two_lists(l1, l2):
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--first', dest='first', required=True, nargs='+',
                        help='list of integer')
    parser.add_argument('--second', dest='second', required=True, nargs='+',
                        help='list of integer')
    args = parser.parse_args()
    first = get_linked_list_from_list(args.first)
    second = get_linked_list_from_list(args.second)
    print(Solution().merge_two_lists(first, second))
