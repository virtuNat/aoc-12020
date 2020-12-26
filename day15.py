#!/usr/bin/env python
from van_eck import van_eck

def main():
    with open(f'{__file__[:-3].capitalize()}Input.txt', 'r') as ifile:
        seed = list(map(int, ifile.read().split(',')))

    print(van_eck(seed, 2020)) # 1
    print(van_eck(seed, 30000000)) # 2
