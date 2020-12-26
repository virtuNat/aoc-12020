#!/usr/bin/env python
from collections import deque
from itertools import accumulate, islice
from aoc import get_input

def main():
    with get_input(__file__) as ifile:
        stream = list(map(int, ifile))

    queue = deque(stream[:25], maxlen=25)
    for pivot in stream[25:]:
        if not any(pivot - test in queue for test in queue): break
        queue.append(pivot)
    print(pivot) # 1

    rsums = list(accumulate(stream))
    for i, lower in enumerate(rsums):
        sfloor = i + 1; sceil = len(stream) - 1
        while sceil >= sfloor:
            j = (sfloor + sceil) >> 1
            if pivot < rsums[j] - lower:
                sceil = j - 1
            elif pivot > rsums[j] - lower:
                sfloor = j + 1
            else: break
        else: continue
        break
    print(min(zlice := stream[i+1:j+1]) + max(zlice)) # 2

if __name__ == '__main__':
    main()