"""
Advent of Code 2024
Day 8 - Resonant Collinearity (Part 1)

Solution by Jacob Barber
"""

import numpy as np
from itertools import combinations
from aoc_utils import get_args

# Parse program arguments
args = get_args(8, "Resonant Collinearity (Part 1)")

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
