import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or not head.next: return head

    last, n = head, 1
    while last.next:
        last = last.next
        n += 1

    if k % n == 0: return head

    middle = head
    for i in range(n - k % n - 1):
        middle = middle.next

    new_head = middle.next
    last.next = head
    middle.next = None
    return new_head


def print_node(node):
    while node:
        print(node.val)
        node = node.next
    print(" ")

node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print_node(rotateRight(copy.deepcopy(node), 1))
print_node(rotateRight(copy.deepcopy(node),5))
print_node(rotateRight(copy.deepcopy(node),4))
print_node(rotateRight(copy.deepcopy(node),6))
