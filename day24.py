#!/usr/bin/env python
import re
import numpy as np
from scipy.signal import correlate2d

dirs = {
    'e': np.array([1,0]), 'se': np.array([1,-1]), 'sw': np.array([0,-1]),
    'w': np.array([-1,0]), 'nw': np.array([-1,1]), 'ne': np.array([0,1]),
    }
size = 20

def main():
    with open(f'{__file__[:-3].capitalize()}Input.txt', 'r') as ifile:
        paths = [re.findall(r'[ns][we]|[we]', line) for line in ifile]

    tiles = np.zeros((2*size+1,)*2, dtype=int)
    for path in paths:
        tiles[tuple(sum(map(dirs.__getitem__, path)) + (size, size))] ^= 1
    print(tiles.sum()) # 1

    tiles = np.pad(tiles, 50)
    mask = np.array([[0,1,1],[1,0,1],[1,1,0]])
    for _ in range(100):
        corr = correlate2d(tiles, mask, 'same')
        tiles[corr == 2] = 1
        tiles[(corr == 0) | (corr > 2)] = 0
    print(tiles.sum()) # 2
