#!/usr/bin/env python3
""" 100-lfu_cache """
Base = __import__("base_caching").BaseCaching


class LFUCache(Base):
    """ LFU Cache class """

    def __init__(self):
        super().__init__()
        self.__lru = {}
        self.__lfu = {}

    def put(self, key, item):
        """ put key and item in cache_data """
        if key is not None and item is not None:
            lfu = self.get_lfu()
            self.cache_data[key] = item
            self.put_lfu(key)
            if len(list(self.cache_data.keys())) > Base.MAX_ITEMS:
                del self.cache_data[lfu]
                del self.__lfu[lfu]
                del self.__lru[lfu]
                print("DISCARD: " + lfu)

    def get_lru(self, mins):
        """ get lru """
        mn = min([val for val in list(self.__lru.values())
                  if list(self.__lru.values()).index(val) in mins])
        return list(self.__lru.keys())[list(self.__lru.values()).index(mn)]

    def put_lru(self, key):
        """ put lru """
        if len(list(self.__lru.keys())):
            mx = max(list(self.__lru.values()))
            self.__lru[key] = mx + 1
        else:
            self.__lru[key] = 0

    def get_lfu(self):
        """ get lfu """
        if not len(list(self.__lfu.keys())):
            return 0
        mn = min(list(self.__lfu.values()))
        mins = [list(self.__lfu.values()).index(x) for x in
                list(self.__lfu.values()) if mn == x]
        if len(mins) > 1:
            return self.get_lru(mins)
        return list(self.__lfu.keys())[list(self.__lfu.values()).index(mn)]

    def put_lfu(self, key):
        """ put lru """
        if key in list(self.__lfu.keys()):
            self.__lfu[key] = self.__lfu[key] + 1
        else:
            self.__lfu[key] = 1
        self.put_lru(key)

    def get(self, key):
        """ get item from cache_data """
        if key is not None and key in self.cache_data.keys():
            self.put_lfu(key)
            return self.cache_data[key]
        return None
