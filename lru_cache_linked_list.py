class ListNode:

    def __init__(self, key, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class Cache:

    def __init__(self, max_size=5):
        self.max_size = max_size
        self.head = None
        self.tail = None
        self.cache = {}

    def add(self, key: str, val):
        node = ListNode(key, val, None, self.head)
        if self.tail is None:
            self.tail = node
        if self.head is not None:
            self.head.prev = node
        self.head = node
        self.cache[key] = node
        if len(self.cache.keys()) > self.max_size:
            if self.tail.prev is not None:
                self.tail.prev.next = None
            del self.cache[self.tail.key]
            self.tail = self.tail.prev

    def get(self, key):
        if key in self.cache:
            node: ListNode = self.cache[key]
            if node.next is None:
                self.tail = node.prev
            if node.prev is not None:
                node.prev.next = node.next
                node.prev = None
            self.head.prev = node
            node.next = self.head
            self.head = node
            return node.val

    def remove(self, key):
        if key in self.cache:
            node: ListNode = self.cache[key]
            if node.prev is not None:
                node.prev.next = node.next
            elif node.next is not None:
                self.head = node.next
            del self.cache[key]




c = Cache()
print(c.add("a", 1))
print(c.add("b", 2))
print(c.add("c", 3))
print(c.add("d", 4))
print(c.add("e", 5))
print(c.get("a"))
print(c.add("f", 6))
print(c.get("b"))
