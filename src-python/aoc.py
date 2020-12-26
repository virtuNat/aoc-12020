#!/usr/bin/env python
from os.path import join as pjoin, split as psplit, splitext as fsplit
from contextlib import contextmanager
from timeit import timeit

@contextmanager
def get_input(file_name):
    fpath, fname = psplit(file_name)
    file = open(pjoin(psplit(fpath)[0], 'input', f'{fsplit(fname)[0]}.txt'), 'r')
    try:
        yield file
    finally:
        file.close()


def main():
    times = []
    for day in range(1, 26):
        time = timeit(f'day{day:02}.main()', f'import day{day:02}', number=5)
        times.append(1000*time/5)

    total = sum(times)
    ftimes = [t for t in times if t < 1000]
    print()
    print('\n'.join(
        f'Day {day:02d} completed in {time:8.3f} ms.'
        for day, time in enumerate(times, 1)
        ))
    print(
        f'\n'
        f'Total time taken: {total:0.03f} ms.\n'
        f'Mean time per day: {total/len(times):0.3f} ms.\n'
        f'Mean time per day w/o outliers (>= 1s): {sum(ftimes)/len(ftimes):0.3f} ms.\n\n'
        f'Fastest day: {(mintime := min(times)):0.3f} ms on day {times.index(mintime)+1}.\n'
        f'Slowest day: {(maxtime := max(times)):0.3f} ms on day {times.index(maxtime)+1}.'
        )

if __name__ == '__main__':
    main()
