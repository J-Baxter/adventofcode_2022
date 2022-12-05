# Advent of Code 2022
# Day 1

import pandas as pd
import numpy as np
import os
import re

os.chdir('/Users/s1506888/Documents/PhD4/adventofcode_2022')


def main():

    # Import data
    inputfile = './data/day5'
    initial_layout = []
    procedure = []

    with open(inputfile, 'r') as filedata:
        lineslist = filedata.readlines()

        filedata.close()


        for textline in (lineslist[:9]):
            lst = [i.stip() for j in re.findall(regex, textline) for i in j if j]

            initial_layout.append(lst)

        for textline in (lineslist[10:]):
            procedure.append(textline)

    filedata.close()

    # Format initial layout
    initial_layout_prep = [re.split(r'\s{1,}') for x in initial_layout]


    # Format rearrangement procedures
    procedure_clean = pd.DataFrame()
    for i in list(range(1, 501)):
        cleaned = [float(s) for s in re.findall(r'-?\d+\.?\d*', procedure[i-1])]
        cleaned_df = pd.DataFrame(data=cleaned).T
        procedure_clean = procedure_clean.append(cleaned_df)

    procedure_clean.columns = ['qty', 'origin', 'destination']







if __name__ == "__main__":
    main()
