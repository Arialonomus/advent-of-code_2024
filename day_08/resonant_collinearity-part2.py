"""
Advent of Code 2024
Day 8 - Resonant Collinearity (Part 2)

Solution by Jacob Barber
"""

import numpy as np
from itertools import combinations
from aoc_utils import get_args

# Parse program arguments
args = get_args(8, "Resonant Collinearity (Part 2)")

# Read input into character matrix
with args.input_file as file:
    antenna_map = np.array([list(line) for line in file.read().splitlines()], dtype='U1')

# Get the list of frequencies from the map
frequency_list = np.unique(antenna_map[antenna_map != '.'])

# Build the list of antenna pairs
antenna_pairs = []
for frequency in frequency_list:
    positions = np.argwhere(antenna_map == frequency)
    num_antennae = positions.shape[0]
    if num_antennae > 1:  # Lone antennas don't create antinodes
        antenna_pairs += list(combinations(positions, 2))

# Calculate antinode positions and place them on map
height, width = antenna_map.shape

def is_on_map(position):
    """
    Validates a position is within the bounds of the grid map
    :param position: A 2D array representing the row/col indices for the position
    :return: True if the position is on the grid, otherwise return False
    """

    row, col = position
    return 0 <= row < height and 0 <= col < width

for pair in antenna_pairs:
    # Use vector subtraction to calculate distance between pairs
    antenna_a, antenna_b = pair
    distance = antenna_b - antenna_a

    # Place all antinode positions in each direction
    antinode = antenna_b - distance
    while is_on_map(antinode):
        antenna_map[antinode[0]][antinode[1]] = '#'
        antinode -= distance

    antinode = antenna_a + distance
    while is_on_map(antinode):
        antenna_map[antinode[0]][antinode[1]] = '#'
        antinode += distance

# Sum unique antinode positions and output result
num_antinode_locations = np.sum(antenna_map == '#')
print(num_antinode_locations)
