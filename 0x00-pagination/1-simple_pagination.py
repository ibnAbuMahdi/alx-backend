#!/usr/bin/env python3
""" 1-simple_pagination """
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ returns start and end index as a tuple """
    return (page_size * (page - 1), page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ return a page from dataset """
        assert(type(page) is int and type(page_size) is int)
        assert(page > 0 and page_size > 0)
        lo, up = index_range(page, page_size)
        ds = self.dataset()
        if lo >= len(ds) or up >= len(ds):
            return []
        return ds[lo:up]
