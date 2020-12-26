#!/usr/bin/env python
from math import prod, sqrt
from itertools import combinations, product
import numpy as np
from scipy.signal import correlate2d

def permutate(tile):
    for _ in range(4):
        yield tile
        tile = np.rot90(tile)
    tile = tile[::-1]
    for _ in range(4):
        yield tile
        tile = np.rot90(tile)

def insert(y, x, tid, tile):
    tiles[tid] = tile
    image[y*8:(y+1)*8,x*8:(x+1)*8] = tile[1:-1,1:-1]
    grid[y, x] = tid

def main():
    global tiles; global image; global grid
    with open(f'{__file__[:-3].capitalize()}Input.txt', 'r') as ifile:
        tiles = {}
        for tile in ifile.read().split('\n\n'):
            tid, *tdata = tile.strip().split('\n')
            tiles[int(tid[5:-1])] = np.array([['.#'.index(c) for c in row] for row in tdata])

    size = int(sqrt(len(tiles)))
    image = np.zeros((8*size,)*2, dtype=int)
    grid = np.zeros((size,)*2, dtype=int)

    borders = {}
    for tid, tile in tiles.items(): # Top, Right, Bottom, Left
        rows = np.vstack((tile[0], tile[:,-1], tile[-1], tile[:,0]))
        rows = np.vstack((rows, rows[:,::-1]))
        borders[tid] = rows

    adjs = {tid: [] for tid in tiles}
    for i, j in combinations(tiles, 2):
        rows = borders[i][:,:,np.newaxis]
        cols = borders[j][:4].T
        if not (rows == cols).all(axis=1).any(): continue
        adjs[i].append(j)
        adjs[j].append(i)

    corners = [k for k, v in adjs.items() if len(v) == 2]
    print(prod(corners)) # 1

    insert(0, 0, corners[0], tiles[corners[0]])
    for _ in range(2): # Construct left strip
        for y in range(1, size):
            ptid = grid[y-1, 0]
            for ntid in adjs[ptid]:
                for perm in permutate(tiles[ntid]):
                    if (tiles[ptid][-1] == perm[0]).all():
                        insert(y, 0, ntid, perm)
                        break
                else: continue
                break
            else: break
        else: break
        # If no matches occured, flip the reference corner
        insert(0, 0, ptid, tiles[ptid][::-1])
    for _ in range(2): # Tile the rest
        for y, x in product(range(size), range(1, size)):
            ptid = grid[y, x-1]
            for ntid in adjs[ptid]:
                for perm in permutate(tiles[ntid]):
                    if (tiles[ptid][:,-1] == perm[:,0]).all():
                        insert(y, x, ntid, perm)
                        break
                else: continue
                break
            else: break
        else: break
        # If no matches occured, matching side is facing away from the grid
        image[:,:8] = image[:,7::-1]
        for tid in grid[:,0]:
            tiles[tid] = tiles[tid][:,::-1]

    mask = np.array([
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
        [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],
        [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0],
        ])
    total = mask.sum()
    for perm in permutate(image):
        corr = correlate2d(perm, mask, 'same') == total
        if (count := corr.sum()): break
    print(perm.sum() - total*count) # 2
    # for y, x in zip(*np.where(corr)):
    #     perm[y-1:y+2,x-9:x+11] += mask
    # perm[perm == 0] = 0x0d1c9f
    # perm[perm == 1] = 0x020f66
    # perm[perm == 2] = 0x08702e
    # import pygame as pg
    # surf = pg.Surface(perm.shape)
    # pg.surfarray.blit_array(surf, perm.T)
    # pg.image.save(pg.transform.scale(surf, np.multiply(perm.shape, 8)), 'day20.png')
