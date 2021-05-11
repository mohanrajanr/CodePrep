
class Node:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next


a = [1, 2, 3, 4, 5]
head = None
for i in range(len(a)):
    head = Node(a[i], head)

h = head
for i in range(len(a)):
    print(h.val, end=" ")
    h = h.next

# print("\nRecursion")
# def recursion(node, prev=None):
#     if not node:
#         return prev
#     main_node = recursion(node.next, node)
#     # print("Recursion: Setting Next for Node:{} as {}".format(node.val, prev))
#     node.next = prev
#     return main_node
#
# new = recursion(head)
# h = new
# for i in range(len(a)):
#     print(h.val, end=" ")
#     h = h.next

print("\nIteration")
def iteration(node):
    prev = None

    while node:
        next = node.next
        node.next = prev
        prev = node
        print("Iteration Pointing:{} to {}".format(node.val, prev))
        node = next
    return prev

new2 = iteration(head)
h = new2
for i in range(len(a)):
    print(h.val, end=" ")
    h = h.next
