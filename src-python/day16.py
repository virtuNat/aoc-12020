#!/usr/bin/env python
import re
from math import prod
from itertools import chain
import numpy as np
from aoc import get_input

def main():
    with get_input(__file__) as ifile:
        rules, ours, refs = ifile.read().split('\n\n')
        rules = np.array([
            list(map(int, re.findall(r'\d+', rule)))
            for rule in rules.split('\n')
            ])
        tickets = np.array([
            list(map(int, ticket.split(',')))
            for ticket in chain([ours.split('\n')[1]], refs.split('\n')[1:])
            ])

    a, b, c, d = rules.T # Transpose to make 1-D vectors
    n = tickets[:,:,np.newaxis] # Add an axis so that broadcasting works
    check = ((a <= n) & (n <= b)) | ((c <= n) & (n <= d)) # Axis 0: Tickets, 1: Fields, 2: Rules
    check_invalid = check.any(axis=2) # Table for each field fulfilling any rule
    print(tickets[~check_invalid].sum()) # 1
    # Filter by valid ticket, table for each field/rule combo if all tickets fulfill.
    matrix = check[check_invalid.all(axis=1)].all(axis=0) # Axis 0: Fields, 1: Rules
    trisum = matrix.sum(axis=0)[:,np.newaxis] + matrix.sum(axis=1) # Assume triangularization invariant
    print(prod(int(tickets[0,np.where(trisum[i] == trisum.shape[0] + 1)[0]]) for i in range(6))) # 2

if __name__ == '__main__':
    main()
