#!/usr/bin/env python
import numpy as np
from scipy.signal import correlate
from aoc import get_input

def automata(grid, dims):
    grid = np.pad(np.expand_dims(grid, tuple(range(2, dims))), 6)
    mask = np.ones((3,) * dims, dtype=int)
    mask[(1,)*dims] = 0
    for _ in range(6):
        conv = correlate(grid, mask, 'same')
        grid[(conv < 2) | (conv > 3)] = 0
        grid[conv == 3] = 1
    return grid.sum()

def main():
    with get_input(__file__) as ifile:
        grid = np.array([['.#'.index(i) for i in line.strip()] for line in ifile])

    print(automata(grid, 3)) # 1
    print(automata(grid, 4)) # 2

if __name__ == '__main__':
    main()
