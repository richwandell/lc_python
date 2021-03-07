from collections import deque

class LRUCache:
    """
    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise,
add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
evict the least recently used key.

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
    """

    def __init__(self, capacity: int):
        self.cache = {}
        self.queue = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.queue.remove(key)
            self.queue.appendleft(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.queue.remove(key)
            self.queue.appendleft(key)
            self.cache[key] = value
            return

        if len(self.queue) < self.capacity:
            self.queue.appendleft(key)
            self.cache[key] = value
        else:
            remove_key = self.queue.pop()
            del self.cache[remove_key]
            self.cache[key] = value
            self.queue.appendleft(key)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# c = LRUCache(2)
# c.put(1, 1) # cache is {1=1}
# c.put(2, 2) # cache is {1=1, 2=2}
# print(c.get(1))    # return 1
# c.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print(c.get(2))    # returns -1 (not found)
# c.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# print(c.get(1))    # return -1 (not found)
# print(c.get(3))    # return 3
# print(c.get(4))    # return 4

c = LRUCache(2)
c.put(2, 1)
c.put(2, 2)
print(c.get(2))
c.put(1, 1)
c.put(4, 1)
print(c.get(2))


# ["LRUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]