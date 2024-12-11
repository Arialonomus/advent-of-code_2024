"""
Advent of Code 2024
Day 4 - Ceres Search (Part 2)

Solution by Jacob Barber
"""

import numpy as np
from aoc_utils import get_args

# Parse program arguments
args = get_args(4, "Ceres Search (Part 2)")

# Read input into character matrix
with args.input_file as file:
    word_search = np.array([list(line) for line in file.read().splitlines()], dtype='U1')

def check_for_x_mas(a_row, a_col):
    """
    Checks if a valid X-MAS is formed around the passed-in position of the 'A' character
    :param a_row: The row position of the 'A' character
    :param a_col: The column position of the 'A' character
    :return: True if an X-MAS is found, otherwise returns False
    """

    def mas_formed(check_char, opposite_char):
        match check_char:
            case 'M':
                return opposite_char == 'S'
            case 'S':
                return opposite_char == 'M'

    # Check NW/SE diagonal
    nw_char = word_search[a_row - 1][a_col - 1]
    se_char = word_search[a_row + 1][a_col + 1]
    nw_se_mas = mas_formed(nw_char, se_char)

    # Check SW/NE diagonal
    sw_char = word_search[a_row + 1][a_col - 1]
    ne_char = word_search[a_row - 1][a_col + 1]
    sw_ne_mas = mas_formed(sw_char, ne_char)

    return nw_se_mas and sw_ne_mas

# Find all 'A' positions and check for X-MAS occurences
start_positions = np.argwhere(word_search == 'A')
height, width = word_search.shape
total_occurrences = 0

for position in start_positions:
    row, col = position
    if 0 < row < height - 1 and 0 < col < width - 1:
        total_occurrences += 1 if check_for_x_mas(row, col) else 0
print(total_occurrences)

