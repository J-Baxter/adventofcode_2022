# Advent of Code 2022
# Day 2

import pandas as pd
import numpy as np
import os

os.chdir('/Users/s1506888/Documents/PhD4/adventofcode_2022')


def whowins(opponent, you):
    score = {}

    if opponent == 'A': #Rock
        if you == 'X': #Rock
            score = 3

        if you == 'Y': #Paper
            score = 6

        if you == 'Z': #Scissors
            score = 0

    elif opponent == 'B': #Paper
        if you == 'X': #Rock
            score = 0

        if you == 'Y': #Paper
            score = 3

        if you == 'Z': #Scissors
            score = 6

    elif opponent == 'C': #Scissors
        if you == 'X': #Rock
            score = 6

        if you == 'Y': #Paper
            score = 0

        if you == 'Z': #Scissors
            score = 3

    return score


def determineplay(opponent, you):
    play = {}

    if you == 'Y':  # Draw
        if opponent == 'A':  # Rock
            play = 'X'  # Rock

        if opponent == 'B':  # Paper
            play = 'Y'  # Paper

        if opponent == 'C':  # Scissors
            play = 'Z'  # Scissors

    elif you == 'X':  # Lose
        if opponent == 'A':  # Rock
            play = 'Z'  # Scissors

        if opponent == 'B':  # Paper
            play = 'X'  # Rock

        if opponent == 'C':  # Scissors
            play = 'Y'  # Paper

    elif you == 'Z':  # Win
        if opponent == 'A':  # Rock
            play = 'Y'  # Paper

        if opponent == 'B':  # Paper
            play = 'Z'  # Scissors

        if opponent == 'C':  # Scissors
            play = 'X'  # Rock


    return play


def main():

    df = pd.read_table('./data/day2', skip_blank_lines=False, header=None, index_col=None, delimiter=' ')
    df.columns = ['opponent', 'you']

    # Get winner of each game
    df['yourscore_p1'] = df.apply(lambda row: whowins(row['opponent'], row['you']), axis=1)
    df['yourplay_p2'] = df.apply(lambda row: determineplay(row['opponent'], row['you']), axis=1)
    df['yourscore_p2'] = df.apply(lambda row: whowins(row['opponent'], row['yourplay_p2']), axis=1)

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
    df_numeric['yourscore_p2'] += df_numeric['yourplay_p2']

    # Solution Problem 2
    totalscore_p2 = sum(df_numeric['yourscore_p2'])
    print('The total score if everything goes to plan is', totalscore_p2)


if __name__ == "__main__":
    main()
