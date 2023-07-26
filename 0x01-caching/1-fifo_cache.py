#!/usr/bin/env python3
""" 1-fifo_cache """
Base = __import__("base_caching").BaseCaching


class FIFOCache(Base):
    """ FIFO Cache class """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ put key and item in cache_data """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(list(self.cache_data.keys())) > self.MAX_ITEMS:
                ky = list(self.cache_data.keys())[0]
                del self.cache_data[ky]
                print("DISCARD: " + ky)

    def get(self, key):
        """ get item from cache_data """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
