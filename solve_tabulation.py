import numpy as np
from ks_utils import *


def solve_tabulation(items, capacity):
    value = 0
    n = len(items)
    W = capacity
    taken = np.zeros((n, W + 1))

    # ----Primera Parte del Algoritmo----
    # --RELLENAR LA TABLA--#

    # El Beneficio cuando N = 0 es 0
    for j in range(0, W):
        taken[0, j] = 0
    for i in range(1, n):
        taken[i, 0] = 0

    for i in range(1, n):
        for j in range(1, W + 1):
            if items[i].weight <= j:
                if items[i].value + taken[i - 1, j - items[i].weight] > taken[i - 1, j]:
                    taken[i, j] = items[i].value + taken[i - 1, j - items[i].weight]
                else:
                    taken[i, j] = taken[i - 1, j]
            else:
                taken[i, j] = taken[i - 1, j]

    # ----Segunda Parte del Algoritmo----
    # --BUSCAR LA TABLA--#
    res = [0]*len(items)
    i = n - 1
    k = W
    while i > 0 and k > 0:
        if taken[i, k] != taken[i - 1, k]:
            res[i] = 1
            k = k - items[i].weight
        else:
            i = i - 1
    return taken[n - 1, W], res