#!/usr/bin/env python3
""" 0-simple_helper_function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ returns start and end index as a tuple """
    return (page_size * (page - 1), page_size * page)
