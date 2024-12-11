"""
Advent of Code 2024
Day 3 - Mull It Over (Part 2)

Solution by Jacob Barber
"""

import re
from aoc_utils import get_args

# Parse program arguments
args = get_args(3, "Mull It Over (Part 2)")

# Locate all valid commands
with args.input_file as file:
    do_command_pat = r'do\(\)'
    dont_command_pat = r"don't\(\)"
    mul_command_pat = r'mul\(\d{1,3},\d{1,3}\)'
    pattern = fr"{do_command_pat}|{dont_command_pat}|{mul_command_pat}"
    commands = re.findall(pattern, file.read())

# Parse commands and sum the valid multiplication results
sum_products = 0
mul_enabled = True
for command in commands:
    match command:
        case 'do()':
            mul_enabled = True
        case "don't()":
            mul_enabled = False
        case _:
            if mul_enabled:
                x, y = map(int, command.lstrip('mul(').rstrip(')').split(','))
                sum_products += x * y
print(sum_products)