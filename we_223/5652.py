class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapNodes(head: ListNode, k: int) -> ListNode:
    main_head = ListNode(-1, head)
    temp_k = k
    node = main_head

    while node and temp_k:
        node = node.next
        temp_k -= 1

    if temp_k != 0:
        return head

    kth_node = node
    # print("Found Kth Node:{}".format(kth_node.val))

    temp_k_node = node
    node = main_head
    while temp_k_node:
        # print(temp_k_node, node)
        temp_k_node = temp_k_node.next
        node = node.next

    last_kth_node = node
    # print("Found Last Kth Node:{}".format(last_kth_node.val))

    last_kth_node.val, kth_node.val = kth_node.val, last_kth_node.val

    return main_head.next


def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print(" ")

node1 = ListNode(1, ListNode(2))
node2 = ListNode(1, ListNode(2, ListNode(3)))
node3 = ListNode(1)
node4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print_list(swapNodes(node1, 1))
print_list(swapNodes(node2, 2))
print_list(swapNodes(node3, 1))
print_list(swapNodes(node4, 2))
