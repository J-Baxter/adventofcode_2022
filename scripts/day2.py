# Advent of Code 2022
# Day 1

import pandas as pd
import numpy as np
import os

os.chdir('/Users/s1506888/Documents/PhD4/adventofcode_2022')


def main():

    df = pd.read_table('./data/day2', skip_blank_lines=False, header=None, index_col=None)

    # Create key A/X = Rock = 1 , B/Y = Paper = 2 , C/Z = Scissors = 3

    df.keys()

    # Calculate Scores


if __name__ == "__main__":
    main()
