class Node:
    def __init__(self, key: int, val: int, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1, self.head)
        self.head.next = self.tail

        self.table = dict()

        self.length = 0
        self.capacity = capacity

    def get(self, key: int) -> int:

        if key in self.table:
            node = self.table[key]

            self.remove_node(node)
            self.add_first(node)

            return node.val

        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.table:
            # No Cap increase
            node = self.table[key]
            node.val = value
            self.remove_node(node)
            self.add_first(node)

        else:
            # Cap increase
            node = Node(key, value, self.head, self.head.next)

            if self.length + 1 > self.capacity:

                del self.table[self.tail.prev.key]
                self.length -= 1
                self.remove_node(self.tail.prev)

            self.add_first(node)
            self.table[key] = node
            self.length += 1

    def remove_node(self, node):

        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def add_first(self, node):

        next = self.head.next

        node.next = next
        node.prev = self.head

        self.head.next = node
        next.prev = node

    def __repr__(self):
        out_string = []

        node = self.head.next
        while node != self.tail:
            out_string.append(str((node.key, node.val)))
            node = node.next

        return " ".join(out_string)

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
print(obj.put(2, 1))
print(obj.put(2, 2))
print(obj.get(2))
print(obj.put(3, 3))
print(obj.get(2))
print(obj.put(4, 4))
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
print(obj)