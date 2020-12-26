#!/usr/bin/env python
def main():
    with open(f'{__file__[:-3].capitalize()}Input.txt', 'r') as ifile:
        passes = set(
            int(p.translate(str.maketrans('FBLR', '0101')), 2)
            for p in ifile
            )

    print(maxseat := max(passes)) # 1
    print(*(set(range(min(passes), maxseat)) - passes)) # 2
