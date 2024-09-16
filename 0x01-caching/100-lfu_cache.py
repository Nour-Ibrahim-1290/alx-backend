#!/usr/bin/python3
""" LFU Caching module
"""


BaseCache = __import__('base_caching').BaseCaching


class LFUCache(BaseCache):
    """
    MRU Caching module
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.usage_frequency = {}
        self.usage_order = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.usage_order.remove(key)
            elif len(self.cache_data) >= BaseCache.MAX_ITEMS:
                min_freq = min(self.usage_frequency.values())
                lfu_keys = [
                    k for k, v in self.usage_frequency.items() if v == min_freq
                    ]
                if len(lfu_keys) > 1:
                    lfu_key = next(
                        k for k in self.usage_order if k in lfu_keys
                        )
                else:
                    lfu_key = lfu_keys[0]
                print("DISCARD: {}".format(mru_key))
                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                self.usage_order.remove(lfu_key)
            self.cache_data[key] = item
            self.usage_frequency[key] = self.usage_frequency.get(key, 0) + 1
            self.usage_order.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
