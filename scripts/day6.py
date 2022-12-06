# Advent of Code 2022
# Day 6

import os

os.chdir('/Users/s1506888/Documents/PhD4/adventofcode_2022')


def findfirstuniquekmer(string, length):
    kmers = [string[idx:idx + length] for idx in range(len(string) -length + 1)]

    unique = 0
    i = 0

    while unique < length:
        s = set(kmers[i])
        unique = len(s)
        i += 1

    return kmers[i], (i+(length-1))


def main():
    # Import string
    string = open('./data/day6').read()

    p1_seq, p1_index = findfirstuniquekmer(string, 4)

    # Solution problem 1
    print('The first start-of-packet-marker, ', p1_seq, ', occurs at position', p1_index)

    p2_seq, p2_index = findfirstuniquekmer(string, 14)

    # Solution problem 2
    print('The first start-of-message-marker, ', p2_seq, ', occurs at position', p2_index)


if __name__ == "__main__":
    main()