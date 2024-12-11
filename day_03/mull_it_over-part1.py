"""
Advent of Code 2024
Day 3 - Mull It Over (Part 1)

Solution by Jacob Barber
"""

import re
from aoc_utils import get_args

# Parse program arguments
args = get_args(3, "Mull It Over (Part 1)")

# Locate all valid multiplication commands
with args.input_file as file:
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    commands = re.findall(pattern, file.read())

# Parse factors and sum the multiplication results
sum_products = 0
for command in commands:
    x, y = map(int, command.lstrip('mul(').rstrip(')').split(','))
    sum_products += x * y
print(sum_products)