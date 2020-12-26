#!/usr/bin/env python
def main():
    with open(f'{__file__[:-3].capitalize()}Input.txt', 'r') as ifile:
        groups = [
            [set(q) for q in group.split()]
            for group in ifile.read().split('\n\n')
            ]

    print(sum(len(set.union(*group)) for group in groups)) # 1
    print(sum(len(set.intersection(*group)) for group in groups)) # 2
