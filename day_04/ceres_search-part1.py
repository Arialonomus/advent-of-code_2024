"""
Advent of Code 2024
Day 4 - Ceres Search (Part 1)

Solution by Jacob Barber
"""

import numpy as np
from aoc_utils import get_args

MATCH_STRING = 'XMAS'

# Parse program arguments
args = get_args(4, "Ceres Search (Part 1)")

# Read input into character matrix
with args.input_file as file:
    word_search = np.array([list(line) for line in file.read().splitlines()], dtype='U1')

def check_for_occurrence(start_row, start_col, direction):
    """
    Checks if an occurrence of the match string can be found in the passed-in direction
    :param start_row: The row position of the starting character
    :param start_col: The column position of the starting character
    :param direction: The direction to search
    :return: True if an occurrence is found, otherwise returns False
    """

    # Set the iteration intervals for the search direction
    match direction:
        case 'E':
            interval = (0,1)
        case 'SE':
            interval = (1,1)
        case 'S':
            interval = (1,0)
        case 'SW':
            interval = (1,-1)
        case 'W':
            interval = (0,-1)
        case 'NW':
            interval = (-1,-1)
        case 'N':
            interval = (-1,0)
        case 'NE':
            interval = (-1,1)
        case _:
            print("Invalid direction")
            return False

    # Iterate in the desired direction to determine if a match is found
    # Start from the second character, since first will always match
    cur_row = start_row + interval[0]
    cur_col = start_col + interval[1]
    for char in MATCH_STRING[1:]:
        if word_search[cur_row][cur_col] != char:
            return False
        cur_row = cur_row + interval[0]
        cur_col = cur_col + interval[1]

    # All characters match, occurrence found
    return True

# Find all possible starting positions and test for occurrences
start_positions = np.argwhere(word_search == MATCH_STRING[0])
match_len = len(MATCH_STRING)
height, width = word_search.shape
total_occurrences = 0

for position in start_positions:
    # Determine possible search directions for this start position
    row, col = position
    can_check_N = match_len - 1 <= row < height
    can_check_E = 0 <= col < width - match_len + 1
    can_check_S = 0 <= row < height - match_len + 1
    can_check_W = match_len - 1 <= col < width

    # Check all possible search directions for occurrence
    if can_check_E:
        total_occurrences += 1 if check_for_occurrence(row, col, 'E') else 0
        if can_check_S:
            total_occurrences += 1 if check_for_occurrence(row, col, 'SE') else 0
        if can_check_N:
            total_occurrences += 1 if check_for_occurrence(row, col, 'NE') else 0

    if can_check_S:
        total_occurrences += 1 if check_for_occurrence(row, col, 'S') else 0

    if can_check_W:
        total_occurrences += 1 if check_for_occurrence(row, col, 'W') else 0
        if can_check_S:
            total_occurrences += 1 if check_for_occurrence(row, col, 'SW') else 0
        if can_check_N:
            total_occurrences += 1 if check_for_occurrence(row, col, 'NW') else 0

    if can_check_N:
        total_occurrences += 1 if check_for_occurrence(row, col, 'N') else 0

print(total_occurrences)

