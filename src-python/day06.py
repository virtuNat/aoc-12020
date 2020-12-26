#!/usr/bin/env python
from aoc import get_input

def main():
    with get_input(__file__) as ifile:
        groups = [
            [set(q) for q in group.split()]
            for group in ifile.read().split('\n\n')
            ]

    print(sum(len(set.union(*group)) for group in groups)) # 1
    print(sum(len(set.intersection(*group)) for group in groups)) # 2

if __name__ == '__main__':
    main()
