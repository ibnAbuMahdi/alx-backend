#!/usr/bin/env python3
""" 2-hypermedia_pagination """
from typing import Tuple, Dict, List, Union, Any
import csv
import math


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
        if lo >= len(ds):
            return []
        if up >= len(ds):
            up = len(ds) - 1
        return ds[lo:up]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """ return hyper media of a page as a dictionary """
        hyper: Dict = {'data': []}
        hyper['page'] = page
        hyper['data'] = self.get_page(page, page_size)
        hyper['page_size'] = len(hyper['data'])
        hyper['next_page'] = page + 1 \
            if len(hyper['data']) and len(hyper['data']) == page_size else None
        hyper['prev_page'] = page - 1 if page > 1 else None
        hyper['total_pages'] = math.ceil(len(self.dataset()) / page_size)

        return hyper
