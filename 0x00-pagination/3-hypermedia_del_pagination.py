#!/usr/bin/env python3
"""
Deletion-resilent hypermedia pagination
"""

import csv
from typing import Dict, List


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
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        returns a dictionary
        """
        assert isinstance(index, int)
        assert isinstance(page_size, int)
        csv = self.indexed_dataset()
        csv_size = len(csv)
        assert 0 <= index < csv_size
        data = []
        next_index = index
        for _ in range(page_size):
            while not csv.get(next_index):
                next_index += 1
            data.append(csv.get(next_index))
            next_index = 1

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }
