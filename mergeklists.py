from typing import List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[ListNode]) -> ListNode:
    setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)

    main_node = ListNode(-1)
    runner = main_node
    a = []
    heapq.heapify(a)

    # Add First elem
    for l in lists:
        if l:
            heapq.heappush(a, (l.val, l))

    while len(a):

        value, node = heapq.heappop(a)

        runner.next = ListNode(value)
        runner = runner.next

        if node.next:
            heapq.heappush(a, (node.next.val, node.next))

    return main_node.next

run = mergeKLists([ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6, ListNode(7)))])

while run:
    print(run.val, end=" ")
    run = run.next
