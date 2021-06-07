#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import inf
from copy import deepcopy
import numpy as np


### KROK 1 - redukcja macierzy ###
def reduce_matrix(matrix):
    new_matrix = deepcopy(matrix)
    rows, cols = new_matrix.shape
    LB = 0
    # reduce rows
    for r in range(rows):
        min_el = min(new_matrix[r])
        if min_el != inf:
            LB += min_el
            for c in range(cols):
                new_matrix[r, c] -= min_el
    # reduce cols
    for c in range(cols):
        min_el = min(new_matrix[:, c])
        if min_el != inf:
            LB += min_el
            for r in range(rows):
                new_matrix[r, c] -= min_el
    return new_matrix, LB


### KROK 3 - podział problemu na 2 podproblemy ###
def division(matrix, vertex):
    PP_1 = deepcopy(matrix)
    PP_2 = deepcopy(matrix)
    r, c = vertex
    # 1 podproblem (zawierający odcinek)
    PP_1[r, :] = inf
    PP_1[:, c] = inf
    new_mat1, new_LB_1 = reduce_matrix(PP_1)
    # 2 podproblem (nie zawiera odcinka)
    PP_2[r, c] = inf
    new_mat2, new_LB_2 = reduce_matrix(PP_2)
    return (PP_1, new_LB_1), (PP_2, new_LB_2)


### TEST POWYŻSZYCH FUNKCJI ###
'''matrix = np.array([[1, 2, 3],
                   [2, 3, 4],
                   [3, 2, 1]], 'float')
print(matrix)
print(reduce_matrix(matrix))

p1, p2 = division(matrix, (1, 2))'''

