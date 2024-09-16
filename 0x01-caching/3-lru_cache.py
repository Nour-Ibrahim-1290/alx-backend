#!/usr/bin/python3
""" Basic Caching module
"""


BaseCache = __import__('base_caching').BaseCaching


class LRUCache(BaseCache):
    """
    LRU Caching module
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.lru_order.remove(key)
            elif len(self.cache_data) >= BaseCache.MAX_ITEMS:
                lru_key = self.lru_order.pop(0)
                print("DISCARD: {}".format(lru_key))
                del self.cache_data[lru_key]
            self.cache_data[key] = item
            self.lru_order.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data.get(key)
