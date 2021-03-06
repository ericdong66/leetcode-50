from model import TreeNode, ListNode, RandomListNode
from random import randint


def get_tree_from_list(li):
    """
    :param li: list, represent a breadth first traversal tree
    :return: root node
    """
    if not li:
        return None

    node_list = list()
    for idx, num in enumerate(li):
        new_node = TreeNode(num)
        if idx == 0:
            node_list.append(new_node)
        else:
            parent_idx, right = divmod((idx - 1), 2)
            if not right:
                node_list[parent_idx].left = new_node
            else:
                node_list[parent_idx].right = new_node
            node_list.append(new_node)
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


def get_random_linked_list_from_list(li):
    """"
    :param li: list of integers
    :return: header node
    """
    lookup = list()
    curr = dummy = RandomListNode(0)
    for i in li:
        new = RandomListNode(i)
        lookup.append(new)
        curr.next = new
        curr = curr.next

    for node in lookup:
        random_idx = randint(0, len(lookup) - 1)
        node.random = lookup[random_idx]

    return dummy.next


def in_order_depth_first_traversal(root):
    """
    :param root: root of a tree node
    :return: result of in order dfs
    """
    result, stack = [], [(root, False)]

    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if visited:
            result.append(node.val)
        else:
            stack.append((node.right, False))
            stack.append((node, True))
            stack.append((node.left, False))
    return result


def breadth_first_traversal(root):
    """
    :param root: root of a tree node
    :return: result of in order dfs
    """
    result, queue = [], [root]

    while queue:
        node = queue.pop(0)
        if node is None:
            continue
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        result.append(node.val)

    return result
