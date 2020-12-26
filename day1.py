#!/usr/bin/env python
from itertools import combinations
from math import prod

def tally(nlist, n):
    return next(prod(i) for i in combinations(nlist, n) if sum(i) == 2020)

def main():
    with open(f'{__file__[:-3].capitalize()}Input.txt', 'r') as ifile:
        nlist = list(map(int, ifile.readlines()))

    print(tally(nlist, 2)) # 1
    print(tally(nlist, 3)) # 2
