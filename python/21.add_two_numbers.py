# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain
# a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
# Definition for singly-linked list.
# Time:  O(n)
# Space: O(1)

import argparse
from model import ListNode
from helper import get_linked_list_from_list


class Solution(object):
    @staticmethod
    def add_two_numbers(l1, l2):
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return dummy.next


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--first', dest='first', required=True, nargs='+',
                        help='list of integer', type=int)
    parser.add_argument('--second', dest='second', required=True, nargs='+',
                        help='list of integer', type=int)
    args = parser.parse_args()

    first = get_linked_list_from_list(args.first)
    second = get_linked_list_from_list(args.second)
    print(Solution().add_two_numbers(first, second))
