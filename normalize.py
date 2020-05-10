import math
from typing import List, Tuple

import numpy as np


# class ColumnNormalizeInfo:
#     def __init__(self, min: float, max: float):
#         self.min = min
#         self.max = max
#         self.range = max - min
#
#
# def normalize(data: np.ndarray) -> Tuple[np.array, List[ColumnNormalizeInfo]]:
#
#     def norm(value: float, column_info: ColumnNormalizeInfo) -> float:
#         return value if math.isnan(value) else (value - column_info.min) / column_info.range
#
#     def get_column_info(column: List) -> ColumnNormalizeInfo:
#         filtered = list(filter(lambda el: not math.isnan(el), column))
#         return ColumnNormalizeInfo(min(filtered), max(filtered)) if len(filtered) != 0 else None
#
#     rows_number, row_length = data.shape
#     row_length_range = range(row_length)
#     column_infos = {i: get_column_info(data[:, i]) for i in row_length_range}
#     return np.array(
#         [[norm(data[i, j], column_infos[j]) for j in row_length_range] for i in range(rows_number)]
#     )
