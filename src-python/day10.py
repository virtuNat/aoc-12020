#!/usr/bin/env python
from math import prod
from collections import Counter
import numpy as np
from numpy.linalg import matrix_power
from aoc import get_input

T = np.array([[1,1,1],[1,0,0],[0,1,0]], dtype='uint64')
def tribo(n):
    return int(matrix_power(T, n-3)[0, 0])

def main():
    with get_input(__file__) as ifile:
        alist = sorted(map(int, ifile))

    diffs = [b-a for b, a in zip(alist + [alist[-1]+3], [0] + alist)]
    print(prod(Counter(diffs).values())) # 1

    split = [i+1 for i, d in enumerate(diffs) if d == 3]
    print(prod(tribo(b-a+2) for b, a in zip(split + [split[-1]+1], [0] + split))) # 2

if __name__ == '__main__':
    main()
