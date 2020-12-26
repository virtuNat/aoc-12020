#!/usr/bin/env python
from aoc import get_input

def main():
    with get_input(__file__) as ifile:
        passes = set(
            int(p.translate(str.maketrans('FBLR', '0101')), 2)
            for p in ifile
            )

    print(maxseat := max(passes)) # 1
    print(*(set(range(min(passes), maxseat)) - passes)) # 2

if __name__ == '__main__':
    main()
