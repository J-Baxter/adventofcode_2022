# Advent of Code 2022
# Day 3

import pandas as pd
import numpy as np
import os
from itertools import chain

os.chdir('/Users/s1506888/Documents/PhD4/adventofcode_2022')


def splitandfind(x):
    c1, c2 = x[:len(x) // 2], x[len(x) // 2:]
    common_chars = ''.join(set(c1).intersection(c2))

    return common_chars


def main():
    # Import data
    rucksacks = open('./data/day3').read().splitlines()

    # Init priorities
    alpha = [chr(n) for n in chain(range(97, 123), range(65, 91),)]
    num = list(range(1, 53))
    priorities = dict(zip(alpha, num))

    # Identify common characters
    commoners = [splitandfind(rucksack) for rucksack in rucksacks]
    commoners_priorities = []

    for commoner in commoners:
        if commoner in priorities:
            commoners_priorities.append(priorities[commoner])

    # Solution Problem 1
    sum_commoners_priorities = sum(commoners_priorities)
    print('The sum of the priorities of these item types is ', sum_commoners_priorities)




if __name__ == "__main__":
    main()
