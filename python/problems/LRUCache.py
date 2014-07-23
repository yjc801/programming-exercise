import collections


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cacheList = collections.deque()
        self.cacheMap = dict()
        
    # @return an integer
    def get(self, key):
        if key not in self.cacheMap:
            return -1
        self.cacheList.remove(key)
        self.cacheList.appendleft(key)
        return self.cacheMap[key]
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.cacheMap:
            if self.capacity == len(self.cacheList):
                del self.cacheMap[self.cacheList.pop()]
            self.cacheList.appendleft(key)
            self.cacheMap[key] = value
        else:
            self.cacheMap[key] = value
            self.cacheList.remove(key)
            self.cacheList.appendleft(key)

if __name__ == '__main__':
    cache = LRUCache(5)
    cache.set(5,5)
    cache.set(4,4)
    cache.set(3,3)
    cache.set(2,2)
    cache.set(1,1)
    print cache.cacheList
    cache.set(6,6)
    print cache.cacheList
    print cache.get(5)
    cache.set(1,7)
    print cache.cacheList
    print cache.get(1)