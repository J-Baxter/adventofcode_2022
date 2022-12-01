# Advent of Code 2022
# Day 1

import pandas as pd
import numpy as np
import os

os.chdir('/Users/s1506888/Documents/PhD4/adventofcode_2022')


def main():

    df = pd.read_table('./data/day1', skip_blank_lines=False, header=None, index_col=None, dtype='Int64')

    df_list = np.split(df, df[df.isnull().all(1)].index)

    total_calories = [df.sum()[0] for df in df_list]

    total_calories.sort(reverse=True)

    # Solution Problem 1
    top_elf = total_calories[0]
    print('The greatest number of calories carried is', top_elf)

    # Solution Problem 2
    top3_elves = sum(total_calories[0:3])

    print('The sum of calories carried by the top three is', top3_elves)


if __name__ == "__main__":
    main()
