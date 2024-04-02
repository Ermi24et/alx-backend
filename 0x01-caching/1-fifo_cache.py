#!/usr/bin/env python3
"""
FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """a method that is responsible to do FIFO caching"""
    def __init__(self):
        """initialization"""
        super().__init__()

    def put(self, key, item):
        """a method to assign the dict self.cache_data the
        item value for the key"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                self.cache_data.pop(first_key)
                print(f"DISCARD: {first_key}")
            else:
                self.cache_data[key] = item

    def get(self, key):
        """a method that returns the value in self.cache_data linked to key"""
        if key is None and key not in self.cache_data:
            return None
        return self.cache_data[key]
