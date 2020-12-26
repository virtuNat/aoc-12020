#!/usr/bin/env python
from functools import cache
from itertools import accumulate

@cache
def combat(deck1, deck2, recurse, level=0):
    if level:
        m1 = max(deck1); m2 = max(deck2)
        if m1 > m2 and m1 > 1 + len(deck1) + len(deck2):
            return deck1, deck2
    deck1 = list(deck1); deck2 = list(deck2)
    seen = set()
    while deck1 and deck2:
        state = (tuple(deck1), tuple(deck2))
        if state in seen: break
        seen.add(state)
        c1 = deck1.pop(0); c2 = deck2.pop(0)
        if recurse and c1 <= len(deck1) and c2 <= len(deck2):
            if combat(tuple(deck1[:c1]), tuple(deck2[:c2]), recurse, level+1)[0]:
                deck1.extend((c1, c2))
            else:
                deck2.extend((c2, c1))
        elif c1 > c2:
            deck1.extend((c1, c2))
        else:
            deck2.extend((c2, c1))
    return deck1, deck2

def main():
    with open(f'{__file__[:-3].capitalize()}Input.txt', 'r') as ifile:
        deck1, deck2 = (
            tuple(map(int, line.split('\n')[1:]))
            for line in ifile.read().split('\n\n')
            )
    
    for flag in range(2):
        w1, w2 = combat(deck1, deck2, flag)
        print(sum(accumulate(w1 or w2))) # 1, 2
