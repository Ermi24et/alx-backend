#!/usr/bin/env python3
"""
Deletion-resilent hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Any


class Server:
    """
    a class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        dataset indexed by sorting position indexed 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            t_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                  page_size: int = 10) -> Dict:
        """
        returns a dictionary
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        return {
            "index": index,
            "next_index": index + page_size,
            "page_size": page_size,
            "data": self.__dataset[index:index + page_size]
        }
