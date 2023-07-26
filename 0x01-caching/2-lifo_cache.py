#!/usr/bin/env python3
""" 2-lifo_cache """
Base = __import__("base_caching").BaseCaching


class LIFOCache(Base):
    """ FIFO Cache class """

    def __init__(self):
        super().__init__()
        self.__lk = None

    def put(self, key, item):
        """ put key and item in cache_data """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(list(self.cache_data.keys())) > Base.MAX_ITEMS:
                del self.cache_data[self.__lk]
                print("DISCARD: " + self.__lk)
            self.__lk = key

    def get(self, key):
        """ get item from cache_data """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
