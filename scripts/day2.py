# Advent of Code 2022
# Day 2

import pandas as pd
import numpy as np
import os

os.chdir('/Users/s1506888/Documents/PhD4/adventofcode_2022')


def whowins_p1(oponent, you):
    score = {}

    if oponent == 'A': #Rock
        if you == 'X': #Rock
            score += 3

        if you == 'Y': #Paper
            score += 6

        if you == 'Z': #Scissors
            score += 0

    elif oponent == 'B': #Paper
        if you == 'X': #Rock
            score += 0

        if you == 'Y': #Paper
            score += 3

        if you == 'Z': #Scissors
            score += 6

    elif oponent == 'C': #Scissors
        if you == 'X': #Rock
            score += 6

        if you == 'Y': #Paper
            score += 0

        if you == 'Z': #Scissors
            score += 3

    return score


def whowins_p2(you):
    score = {}

    if you == 'X': #Rock
        score += 0

    if you == 'Y': #Paper
        score += 3

    if you == 'Z': #Scissors
        score += 6

    return score


def main():

    df = pd.read_table('./data/day2', skip_blank_lines=False, header=None, index_col=None, delimiter=' ')
    df.columns = ['opponent', 'you']

    # Get winner of each game
    df['yourscore_p1'] = df.apply(lambda row: whowins_p1(row['opponent'], row['you']), axis=1)

    # Translate letters to numeric scores
    lst = [(['A', 'X'], 1), (['B', 'Y'], 2), (['C', 'Z'], 3)]
    repl_dict = {}
    for x, y in lst:
        repl_dict.update(dict.fromkeys(x, y))

    df_numeric = df.replace(repl_dict)

    # Calculate Scores: Problem 1
    df_numeric['yourscore_p1'] += df_numeric['you']

    # Solution Problem 1
    totalscore_p1 = sum(df_numeric['yourscore_p1'])
    print('The total score if everything goes to plan is', totalscore_p1)

    # Calculate Scores: Problem 2
    df['yourscore_p2'] = df.apply(lambda row: whowins_p2(row['you']), axis=1)
    df_numeric['yourscore_p2'] += df_numeric['you']

    # Solution Problem 1
    totalscore_p2 = sum(df_numeric['yourscore_p2'])
    print('The total score if everything goes to plan is', totalscore_p2)


if __name__ == "__main__":
    main()
