from model import TreeNode, ListNode


def get_tree_from_list(li):
    """
    :param li: list, represent a breadth first traversal tree
    :return: root node
    """
    if not li:
        return None

    node_list = list()
    for idx, num in enumerate(li):
        if idx == 0:
            node_list.append(TreeNode(num))
        else:
            parent_idx, right = divmod((idx - 1), 2)
            if not right:
                node_list[parent_idx].left = TreeNode(num)
            else:
                node_list[parent_idx].right = TreeNode(num)
            node_list.append(TreeNode(num))
    return node_list[0]


def get_linked_list_from_list(li):
    """"
    :param li: list of integers
    :return: header node
    """
    curr = dummy = ListNode(0)
    for i in li:
        curr.next = ListNode(i)
        curr = curr.next

    return dummy.next
