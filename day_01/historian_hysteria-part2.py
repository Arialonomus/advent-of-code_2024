"""
Advent of Code 2024
Day 1 - Historian Hysteria (Part 2)

Solution by Jacob Barber
"""

from collections import Counter
from aoc_utils import get_args

# Parse program arguments
args = get_args(1, "Historian Hysteria (Part 2)")

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

# Accumulate the similarity scores for each element in the left list
right_counts = Counter(right_list)  # Store the occurrence counts for each right list element
total_similarity_score = 0
for num in left_list:
    total_similarity_score += num * right_counts[num]
print(total_similarity_score)