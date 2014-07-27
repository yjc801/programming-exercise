class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        
    # @return an integer
    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache[key]
        del self.cache[key]
        self.cache[key] = value
        return self.cache[key]
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.cache:
            if self.capacity == len(self.cache):
                self.cache.popitem(last=False)
            self.cache[key] = value
        else:
            del self.cache[key]
            self.cache[key] = value
