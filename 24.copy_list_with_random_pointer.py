# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
#
# Time:  O(n)
# Space: O(n)

import argparse
from model import RandomListNode
from helper import get_random_linked_list_from_list


class Solution:
    @staticmethod
    def copy_random_list(head):
        dummy = RandomListNode(0)

        current, pre, copied = head, dummy, dict()

        while current:
            new = RandomListNode(current.label)
            copied[current] = new
            pre.next = new
            pre = pre.next
            current = current.next

        current = head
        while current:
            if current.random:
                copied[current].random = copied[current.random]
            current = current.next

        return dummy.next


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', dest='list', required=True, nargs='+',
                        help='list of integer', type=int)

    args = parser.parse_args()
    ll = get_random_linked_list_from_list(args.list)
    print(ll)
    print(Solution().copy_random_list(ll))
