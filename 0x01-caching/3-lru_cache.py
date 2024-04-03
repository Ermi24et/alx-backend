#!/usr/bin/env python3
"""
LRU caching
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    a class that inherits from BaseCaching and do the LRU caching
    """
    def __init__(self):
        """initialization"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """a method to assign the dict self.cache_data the item
        value for the key"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_item = self.cache_data.popitem(last=False)
                print(f"DISCARD: {first_item[0]}")

    def get(self, key):
        """a method that returns the value in self.cache_data linked to key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
