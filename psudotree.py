import collections


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def populate_tree(tree):
    head = Node(tree.pop(0))

    nodes = [head]
    helper = nodes.pop()
    while len(tree):
        value = tree.pop(0)

        if value:
            node = Node(value)
        else:
            node = None

        if helper.left and helper.right:
            helper = nodes.pop(0)

        if helper.left:
            helper.right = node
            nodes.append(helper.right)
        else:
            helper.left = node
            nodes.append(helper.left)

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


def dfs(node, str_list):
    if not node.left and not node.right:
        print("end", node.val)
        yield ''.join(str_list + [str(node.val)])
        return

    if node.left:
        for s in dfs(node.left, str_list + [str(node.val)]):
            print("inl", s)
            yield s

    if node.right:
        for s in dfs(node.right, str_list + [str(node.val)]):
            print("inr", s)
            yield s
    return

head = populate_tree([2,1,1,1,3,None,None,None,None,None,1])
print_tree(head)

count = 0
for path in dfs(head, []):
    print(path)

    pc = collections.Counter(path)
    ones = 0
    twos = 0
    isValid = True
    for value in pc.values():
        if value == 1:
            ones += 1
        elif value == 2:
            twos += 1
        else:
            isValid = False
            break

    if not isValid:
        continue

    if len(path) % 2 == 0:
        if len(pc.values()) == twos:
            count +=1
            print(path, count)
    else:
        if ones == 1 and len(pc.values()) - 1 == twos:
            count +=1
            print(path, count)
