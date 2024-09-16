#!/usr/bin/python3
""" Basic Caching module
"""


BaseCache = __import__('base_caching').BaseCaching


class BasicCache(BaseCache):
    """
    Basic Caching module
    """

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
