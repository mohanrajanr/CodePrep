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
        value1 = tree.pop(0)
        value2 = tree.pop(0)

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


def print_tree(head):
    print("PreOrder")
    nodes = [head]
    while len(nodes):
        node = nodes.pop(0)
        if node:
            print("Node:{}".format(node.val))
            nodes.append(node.left)
            nodes.append(node.right)
        else:
            print("None")

head = populate_tree([1,2,3,4,5,6,7])
print_tree(head)


def verticalTraversal(root: Node) -> list:
    res = collections.defaultdict(list)

    nodes = collections.deque([(root, 0, 0)])
    while len(nodes):
        (node, h, v) = nodes.popleft()
        # print(node.val, h)
        res[h].append((v, node.val))
        if node.left:
            nodes.append((node.left, h-1, v+1))
        if node.right:
            nodes.append((node.right, h+1, v+1))

    _out = []
    for i in range(min(res.keys()), max(res.keys())+1):
        _out.append([val for v, val in sorted(res[i])])
    return _out

print(verticalTraversal(head))