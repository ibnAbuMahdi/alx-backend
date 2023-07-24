#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ return hypermedia indexed dataset """
        ids: Dict = self.indexed_dataset()
        assert(index is not None and index >= 0 and index < len(ids.values()))
        hyper: Dict = {}
        hyper['index'] = index
        data: List = []
        pgs: int = page_size
        idx: Union[int, None] = index
        while idx is not None and pgs:
            if idx in ids.keys():
                pos: int = list(ids.keys()).index(idx)
                data.append(list(ids.values())[pos])
                idx += 1
                pgs -= 1
            else:
                idx += 1
            if idx > list(ids.keys())[-1]:
                break
        hyper['data'] = data
        hyper['page_size'] = len(hyper['data'])
        hyper['next_index'] = idx
        return hyper
