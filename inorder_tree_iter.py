import collections


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def populate_tree(tree):
    head = Node(tree.pop(0))

    nodes = [head]
    while len(tree):
        value1 = tree.pop(0) if tree else None
        value2 = tree.pop(0) if tree else None

        helper = nodes.pop(0)

        if value1:
            node = Node(value1)
            helper.left = node
            nodes.append(node)

        if value2:
            node = Node(value2)
            helper.right = node
            nodes.append(node)

    return head

head = populate_tree([1,2, None, 4, 5, None, None, None, 7])


def do_inorder(root):
    stack = collections.deque([])
    res = []
    node = root
    while node or len(stack):
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        res.append(node.val)

        node = node.right

    return res

print(do_inorder(head))
