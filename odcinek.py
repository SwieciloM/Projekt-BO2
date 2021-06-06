#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import inf
from copy import deepcopy
import numpy as np

def odcinek(matrix):
    rows, cols = matrix.shape
    Vertex = []
    Cost = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r,c] == 0:
                Vertex.append((r,c))
                row1 = deepcopy(matrix[r])
                row1 = np.delete(row1, c, 0)
                col1 = deepcopy(matrix[:,c])
                col1 = np.delete(col1, r, 0)
                min_row = np.min(row1)
                min_col = np.min(col1)
                Cost.append(min_row + min_col)
    max_Cost = np.max(Cost)
    i = Cost.index(max_Cost)
    opt = Vertex[i]
    return max_Cost, opt