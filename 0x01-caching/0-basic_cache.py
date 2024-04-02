#!/usr/bin/env python3
"""
Basic Dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    a caching system class that inherits from BaseCaching
    """
    def put(self, key, item):
        """method to assign item to cache_data
        if key is not None or item is not None:
            new_dict = {}
            for k, v in self.cache_data.items():
                new_dict[k] = v
            return new_dict"""
        self.cache_data[key] = item
        return self.cache_data

    def get(self, key):
        """a method that returns the value in self.cache_data linked to key"""
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data[key]
