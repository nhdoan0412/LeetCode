#https://leetcode.com/problems/lru-cache/description/
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        
        node.prev.next = node.next
        node.next.prev = node.prev

     
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
        elif len(self.cache) >= self.capacity:
            lru = self.tail.prev
            del self.cache[lru.key]
            lru.prev.next = lru.next
            lru.next.prev = lru.prev

        
        new_node = Node(key, value)
        self.cache[key] = new_node
        new_node.prev = self.head
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node
        
        
        



