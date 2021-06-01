#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import inf
from copy import deepcopy
import numpy as np


def reduce_matrix(matrix):
    new_matrix = deepcopy(matrix)
    rows, cols = new_matrix.shape
    LB = 0
    # reduce rows
    for r in range(rows):
        min_el = min(new_matrix[r])
        LB += min_el
        for c in range(cols):
            new_matrix[r, c] -= min_el
    # reduce cols
    for c in range(cols):
        min_el = min(new_matrix[:, c])
        LB += min_el
        for r in range(rows):
            new_matrix[r, c] -= min_el
    return new_matrix, LB


matrix = np.array([[1, 2, 3],
                   [2, 3, 4],
                   [3, 2, 1]])
print(matrix)
print(reduce_matrix(matrix))
