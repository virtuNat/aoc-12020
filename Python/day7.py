#!/usr/bin/env python
import re
from functools import cache

@cache
def find_gold(bag):
    return 'shiny gold' in rules[bag] or any(find_gold(b) for b in rules[bag])

@cache
def count_bags(bag):
    return 1 + sum(n * count_bags(b) for b, n in rules[bag].items())

def main():
    with open(f'{__file__[:-3].capitalize()}Input.txt', 'r') as ifile:
        lines = [re.findall(r'(\d+ )?(\w+ \w+) bag', line) for line in ifile]
        global rules
        rules = {
            k: {c: int(n) for (n, c) in bags} if bags[0][0] else {}
            for (_, k), *bags in lines
            }

    print(sum(map(find_gold, rules))) # 1
    print(count_bags('shiny gold') - 1) # 2
