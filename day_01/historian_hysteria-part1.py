"""
Advent of Code 2024
Day 1 - Historian Hysteria (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

# Parse program arguments
args = get_args(1, "Historian Hysteria (Part 1)")

# Read and sort input columns as parallel lists
with args.input_file as file:
    left_list = []
    right_list = []
    for line in file:
        left_num, right_num = map(int, line.strip().split('   '))
        left_list.append(left_num)
        right_list.append(right_num)
    left_list.sort()
    right_list.sort()

# Accumulate the differences between each list index
total_distance = 0
for i in range(len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])
print(total_distance)