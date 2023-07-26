#!/usr/bin/env python3
""" 3-lru_cache """
Base = __import__("base_caching").BaseCaching


class LRUCache(Base):
    """ LRU Cache class """

    def __init__(self):
        super().__init__()
        self.__lru = {}

    def put(self, key, item):
        """ put key and item in cache_data """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.put_lru(key)
            if len(list(self.cache_data.keys())) > Base.MAX_ITEMS:
                lru = self.get_lru()
                del self.cache_data[lru]
                del self.__lru[lru]
                print("DISCARD: " + lru)

    def get_lru(self):
        """ get lru from __lru"""
        mn = min(list(self.__lru.values()))
        return list(self.__lru.keys())[list(self.__lru.values()).index(mn)]

    def put_lru(self, key):
        """ put lru into __lru"""
        if len(list(self.__lru.keys())):
            mx = max(list(self.__lru.values()))
            self.__lru[key] = mx + 1
        else:
            self.__lru[key] = 0

    def get(self, key):
        """ get item from cache_data """
        if key is not None and key in self.cache_data.keys():
            mx = max(list(self.__lru.values()))
            self.__lru[key] = mx + 1
            return self.cache_data[key]
        return None
