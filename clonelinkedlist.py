class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head: 'Node') -> 'Node':

    main = head
    clone_copy = Node(-1)

    curr = main
    while curr:
        curr.next = Node(curr.val, curr.next)
        curr = curr.next.next

    curr = main
    while curr:
        node = curr.next
        random = curr.random
        if random:
            node.random = random.next
        curr = curr.next.next

    curr = main
    clone_curr = clone_copy
    while curr and curr.next:
        clone_curr.next = curr.next
        clone_curr = clone_curr.next

        curr.next = curr.next.next
        curr = curr.next

    return clone_copy.next


def print_list(head):

    while head:
        rand_val = head.random.val if head.random else None
        print(head.val, rand_val)
        head = head.next

head = Node(7, Node(13, Node(11, Node(10, Node(1)))))
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head

copyRandomList(head)
print_list(head)
