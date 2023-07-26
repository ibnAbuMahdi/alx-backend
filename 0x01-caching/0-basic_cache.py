#!/usr/bin/env python3
""" Basic Cache """
Base = __import__("base_caching").BaseCaching


class BasicCache(Base):
    """ Basic Cache class """

    def put(self, key, item):
        """ insert key and item into cache_data """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get item from cache_data """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
