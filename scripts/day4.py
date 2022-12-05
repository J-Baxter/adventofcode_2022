# Advent of Code 2022
# Day 4

import pandas as pd
import os

os.chdir('/Users/s1506888/Documents/PhD4/adventofcode_2022')


def getoverlaps(start1, end1, start2, end2, overlaptype):
    overlap = []
    start = {'elf1': start1, 'elf2': start2}
    end = {'elf1': end1, 'elf2': end2}

    max_start = max(start.values())
    min_end = min(end.values())

    if overlaptype == 'complete':
        key_start = [key for key in start if start[key] == max_start]
        key_end = [key for key in end if end[key] == min_end]

        if any(x in key_start for x in key_end):
            overlap = 1
        else:
            overlap = 0

    elif overlaptype == 'any':
        if max_start <= min_end:
            overlap = 1
        else:
            overlap = 0

    return overlap


def main():
    # Import data
    colnames = ['elf1_start', 'elf1_end', 'elf2_start', 'elf2_end']
    df = pd.read_csv('./data/day4', sep="\s|-|,", engine="python", names=colnames, header=None)

    # Infer complete overlaps
    df['complete_overlap'] = df.apply(lambda row: getoverlaps(row['elf1_start'], row['elf1_end'], row['elf2_start'],
                                                              row['elf2_end'], overlaptype='complete'), axis=1)

    # Solution Problem 1
    complete_overlaps = sum(df['complete_overlap'])
    print('In ', complete_overlaps, ' assignment pairs one range fully contains the other.')

    # Infer any overlaps
    df['any_overlap'] = df.apply(lambda row: getoverlaps(row['elf1_start'], row['elf1_end'], row['elf2_start'],
                                                         row['elf2_end'], overlaptype='any'), axis=1)

    # Solution Problem 2
    any_overlaps = sum(df['any_overlap'])
    print('In ', any_overlaps, ' assignment pairs the ranges overlap.')


if __name__ == "__main__":
    main()