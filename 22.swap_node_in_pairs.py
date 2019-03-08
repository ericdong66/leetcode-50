# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space.
# You may not modify the values in the list, only nodes itself can be changed.
#
# Time:  O(n)
# Space: O(1)

import argparse
from model import ListNode
from helper import get_linked_list_from_list


class Solution:
    @staticmethod
    def swap_pairs(head):
        dummy = ListNode(0)
        current, dummy.next = dummy, head

        while current.next and current.next.next:
            temp = current.next

            current.next = current.next.next
            temp.next = temp.next.next

            current.next.next = temp

            current = current.next.next

        return dummy.next


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', dest='list', required=True, nargs='+',
                        help='list of integer', type=int)

    args = parser.parse_args()
    ll = get_linked_list_from_list(args.list)
    print(Solution().swap_pairs(ll))
