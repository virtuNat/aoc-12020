#!/usr/bin/env python
import numpy as np
from scipy.signal import correlate2d
from aoc import get_input

fmat = np.array([[1,1,1],[1,0,1],[1,1,1]])
def convadjs(state):
    return correlate2d(state, fmat, 'same')

def convrays(state):
    return np.array([sum(state[ray] for ray in mask) for mask in rays]).reshape(state.shape)

def automata(seats, convfunc, lim):
    state = seats.copy()
    nstate = np.zeros(state.shape, dtype=int)
    while True: # GAME OF LIFE BABEY
        conv = convfunc(state)
        nstate[:] = np.where(conv, state, 1)
        nstate[conv >= lim] = 0
        nstate *= seats
        if (nstate == state).all(): return nstate.sum()
        state[:] = nstate

def main():
    with get_input(__file__) as ifile:
        seats = np.array([list(map('.L'.index, line.strip())) for line in ifile])
    print(automata(seats, convadjs, 4)) # 1

    vecs = np.array([[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]])
    global rays
    rays = []
    for i, tile in enumerate(seats.flatten()):
        rays.append([])
        if not tile: continue
        pos = divmod(i, seats.shape[1])
        for vec in vecs:
            npos = pos
            while True:
                npos += vec
                if ((0 > npos) | (npos >= seats.shape)).any():
                    break
                npos = tuple(npos)
                if seats[npos]:
                    rays[-1].append(npos)
                    break
    print(automata(seats, convrays, 5)) # 2

if __name__ == '__main__':
    main()
