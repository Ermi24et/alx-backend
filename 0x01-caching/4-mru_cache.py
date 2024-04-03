#!/usr/bin/env python3
"""
MRU caching
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """a class that inherits from BaseCaching and do the MRU caching"""
    def __init__(self):
        """initialization"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """a method that assigns the dictionary self.cache_data the item
        value for the key"""
        if key is not None and item is not None:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_item, _ = self.cache_data.popitem(False)
                print(f"DISCARD: {mru_item}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """a method that rerurns the value in self.cache_data linked to key"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
