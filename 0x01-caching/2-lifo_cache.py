#!/usr/bin/python3
""" Basic Caching module
"""


BaseCache = __import__('base_caching').BaseCaching


class LIFOCache(BaseCache):
    """
    LIFO Caching module
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCache.MAX_ITEMS:
                last = list(self.cache_data.keys())[-1]
                print("DISCARD: {}".format(last))
                self.cache_data.pop(last)
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
