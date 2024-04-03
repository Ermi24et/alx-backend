#!/usr/bin/env python3
"""
MRU caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """a class that inherits from BaseCaching and do the LFU caching"""
    def __init__(self):
        """initialization"""
        super().__init__()
        self.keys = {}

    def put(self, key, item):
        """a method that assigns the dictionary self.cache_data the item
        value for the key"""
        if key is not None and item is not None:
            if self.get(key) != item:
                self.cache_data[key] = item
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    ke = min(self.keys, key=self.keys.get)
                    self.cache_data.pop(ke)
                    print("DISCARD:", ke)
                    self.keys.pop(ke)
                if key not in self.keys:
                    self.keys[key] = 0

    def get(self, key):
        """a method that rerurns the value in self.cache_data linked to key"""
        value = self.cache_data.get(key, None)
        if value:
            self.keys[key] += 1
        return value
