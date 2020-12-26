#!/usr/bin/env python
from itertools import combinations
from math import prod
from aoc import get_input

def tally(nlist, n):
    return next(prod(i) for i in combinations(nlist, n) if sum(i) == 2020)

def main():
    with get_input(__file__) as ifile:
        nlist = list(map(int, ifile.readlines()))

    print(tally(nlist, 2)) # 1
    print(tally(nlist, 3)) # 2

if __name__ == '__main__':
    main()
