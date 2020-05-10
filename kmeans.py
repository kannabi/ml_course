import math
from random import random
from typing import List, Dict, Tuple, Callable

import numpy as np


class ColumnNormalizeInfo:
    def __init__(self, min: float, max: float):
        self.min = min
        self.max = max
        self.range = max - min


class KMeansClusterer:

    def __init__(
        self,
            clusters_number: int,
            calculate_distance: Callable[[np.array, np.array], float],
            centers_epsilon: float = 0.0000001
     ):
        self.clusters_number = clusters_number
        self._normalize_info: Dict[int, ColumnNormalizeInfo] = {}
        self._centers = self._generate_initial_centers()
        self._calculate_distance = calculate_distance
        self._centers_epsilon = centers_epsilon

    def cluster(self, data: np.array):
        normed, self._normalize_info = self._normalize(data)
        clusters: Dict[int, List[np.array]] # data associated by cluster indexes
        current_centers: List[float] = self._centers
        new_centers: List[float]
    #     lol what python doesn't have do ... while. It's not a language it's a joke.
        while True:
            clusters = self._associate_by_clusters(data, current_centers)
            new_centers = self._calculate_new_centers(clusters)




    @staticmethod
    def _normalize(data: np.array) -> Tuple[np.array, Dict[int, ColumnNormalizeInfo]]:
        def norm(value: float, column_info: ColumnNormalizeInfo) -> float:
            return value if math.isnan(value) else (value - column_info.min) / column_info.range

        def get_column_info(column: List) -> ColumnNormalizeInfo:
            filtered = list(filter(lambda el: not math.isnan(el), column))
            return ColumnNormalizeInfo(min(filtered), max(filtered)) if len(filtered) != 0 else None

        rows_number, row_length = data.shape
        row_length_range = range(row_length)
        column_infos = {i: get_column_info(data[:, i]) for i in row_length_range}
        return np.array(
            [[norm(data[i, j], column_infos[j]) for j in row_length_range] for i in range(rows_number)]
        )

    def _is_centers_convergent(self, old_centers: List[float], new_centers: List[float]):
        pass

    def _associate_by_clusters(self, data, centers) -> Dict[int, List[np.array]]:
        pass

    def _calculate_new_centers(self, clusters: Dict[int, List[np.array]]) -> List[float]:
        pass

    def _generate_initial_centers(self) -> [[float]]:
        return [random.uniform(0.0, 1.0) in range(self.clusters_number)]
