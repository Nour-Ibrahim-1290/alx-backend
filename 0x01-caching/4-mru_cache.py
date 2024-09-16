#!/usr/bin/python3
""" Basic Caching module
"""


BaseCache = __import__('base_caching').BaseCaching


class MRUCache(BaseCache):
    """
    MRU Caching module
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.mru_order.remove(key)
            elif len(self.cache_data) >= BaseCache.MAX_ITEMS:
                mru_key = self.mru_order.pop()
                print("DISCARD: {}".format(mru_key))
                del self.cache_data[mru_key]
            self.cache_data[key] = item
            self.mru_order.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.mru_order.remove(key)
        self.mru_order.append(key)
        return self.cache_data.get(key)
