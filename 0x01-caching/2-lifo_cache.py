#!/usr/bin/env python3
"""
LIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """a class inherits from BaseCaching and do the LIFO caching"""
    def __init__(self):
        """initialization"""
        super().__init__()

    def put(self, key, item):
        """a method to assign the dict self.cache_data item value
        for the key"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data)[len(self.cache_data) - 2]
                self.cache_data.pop(last_key)
                print(f"DISCARD: {last_key}")
            else:
                self.cache_data[key] = item

    def get(self, key):
        """a method that returns the value in self.cache_data linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
