#!/usr/bin/env python
from timeit import timeit

times = []
for day in range(1, 26):
    times.append(1000*timeit(f'day{day}.main()', f'import day{day}', number=5)/5)

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
