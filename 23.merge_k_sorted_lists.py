# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.
# Divide and Conquer solution.
#
# Time:  O(nlogk)
# Space: O(logk)

import argparse
from model import ListNode
from helper import get_linked_list_from_list


class Solution:
    @staticmethod
    def merge_k_lists(lists):
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

        def merge_k_lists_helper(li, begin, end):
            if begin > end:
                return None
            if begin == end:
                return li[begin]
            return merge_two_lists(
                merge_k_lists_helper(li, begin, (begin + end) // 2),
                merge_k_lists_helper(li, (begin + end) // 2 + 1, end)
            )

        return merge_k_lists_helper(lists, 0, len(lists) - 1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list1', dest='list1', required=True, nargs='+',
                        type=int, help='list of integer')
    parser.add_argument('--list2', dest='list2', required=True, nargs='+',
                        type=int, help='list of integer')
    parser.add_argument('--list3', dest='list3', required=True, nargs='+',
                        type=int, help='list of integer')
    args = parser.parse_args()

    list1 = get_linked_list_from_list(args.list1)
    list2 = get_linked_list_from_list(args.list2)
    list3 = get_linked_list_from_list(args.list3)

    print(Solution().merge_k_lists([list1, list2, list3]))
