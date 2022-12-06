# Advent of Code 2022
# Day 1

import pandas as pd
from collections import deque
from itertools import zip_longest
import os
import re

os.chdir('/Users/s1506888/Documents/PhD4/adventofcode_2022')


def rearrange(grid, qty, origin, dest, type):
    move = []

    if type == 'singular':
        for i in range(1, qty + 1):
            move = grid[origin - 1].pop()
            grid[dest - 1].append(move)

    elif type == 'grouped':
        for i in range(1, qty + 1):
            move.append(grid[origin - 1].pop())

        move_reversed = list(reversed(move))
        grid[dest - 1].extend(move_reversed)

    return grid


def main():
    # Import data
    inputfile = './data/day5'
    stacks = []
    procedure = []

    with open(inputfile, 'r') as filedata:
        lineslist = filedata.readlines()

        for textline in (lineslist[:9]):
            stacks.insert(0, [textline[i] for i in range(1, len(textline), 4)])

        stacks = list(zip_longest(*stacks, fillvalue=' '))
        stacks_p1 = [deque([crate for crate in stack if crate != ' ']) for stack in stacks]
        stacks_p2 = [deque([crate for crate in stack if crate != ' ']) for stack in stacks]

        for textline in (lineslist[10:]):
            procedure.append(textline)

    filedata.close()

    # Format rearrangement procedures
    procedure_clean = pd.DataFrame()
    for i in range(0, len(procedure)):
        cleaned = [float(s) for s in re.findall(r'-?\d+\.?\d*', procedure[i])]
        cleaned_df = pd.DataFrame(data=cleaned, ).T.astype(int)
        procedure_clean = procedure_clean.append(cleaned_df)

    procedure_clean.columns = ['qty', 'origin', 'destination']

    # Problem 1
    for i in range(0, len(procedure_clean)):
        moves = procedure_clean.iloc[i]
        rearrange(stacks_p1, moves['qty'], moves['origin'], moves['destination'], type='singular')

    # Top element in each stack (Solution 1)
    top_element_p1 = [x.pop() for x in stacks_p1]
    print('When moved individually, the top crates are: ', (''.join(top_element_p1)))

    # Problem 2
    for i in range(0, len(procedure_clean)):
        moves = procedure_clean.iloc[i]
        rearrange(stacks_p2, moves['qty'], moves['origin'], moves['destination'], type='grouped')

    # Top element in each stack (Solution 1)
    top_element_p2 = [x.pop() for x in stacks_p2]
    print('When moved as groups, the top crates are: ', (''.join(top_element_p2)))


if __name__ == "__main__":
    main()
