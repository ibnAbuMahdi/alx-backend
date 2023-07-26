#!/usr/bin/env python3
""" 4-mru_cache """
Base = __import__("base_caching").BaseCaching


class MRUCache(Base):
    """ MRU Cache class """

    def __init__(self):
        super().__init__()
        self.__mru = {}

    def put(self, key, item):
        """ put key and item in cache_data """
        if key is not None and item is not None:
            mru = self.get_mru()
            self.cache_data[key] = item
            self.put_mru(key)
            if len(list(self.cache_data.keys())) > Base.MAX_ITEMS:
                del self.cache_data[mru]
                del self.__mru[mru]
                print("DISCARD: " + mru)

    def get_mru(self):
        """ get mru from __mru """
        if not len(list(self.cache_data.keys())):
            return 0
        mn = max(list(self.__mru.values()))
        return list(self.__mru.keys())[list(self.__mru.values()).index(mn)]

    def put_mru(self, key):
        """ put mru into __mru """
        if len(list(self.__mru.keys())):
            mx = max(list(self.__mru.values()))
            self.__mru[key] = mx + 1
        else:
            self.__mru[key] = 0

    def get(self, key):
        """ get item from cache_data """
        if key is not None and key in self.cache_data.keys():
            mx = max(list(self.__mru.values()))
            self.__mru[key] = mx + 1
            return self.cache_data[key]
        return None
