"""
Advent of Code 2024
Day 5 - Print Queue (Part 1)

Solution by Jacob Barber
"""

from collections import defaultdict
from aoc_utils import get_args

# Parse program arguments
args = get_args(5, "Print Queue (Part 1)")

with args.input_file as file:
    # Split the input file at the blank line
    section1, section2 = file.read().split('\n\n')

    # Build the dict of ordering rules
    ordering_rules = defaultdict(list)
    ordering_pairs = section1.splitlines()
    for pair in ordering_pairs:
        page_num, must_come_before = map(int, pair.split('|'))
        ordering_rules[page_num].append(must_come_before)

    # Build the list of page updates
    updates = []
    update_lines = section2.splitlines()
    for line in update_lines:
        page_list = list(map(int, line.split(',')))
        updates.append(page_list)

# Filter valid orderings and sum the page numbers
sum_valid_middle_pages = 0
for update in updates:
    # Iterate backwards through the list since our rules are "must come before"
    i = len(update) - 1
    is_valid_ordering = True
    while is_valid_ordering and i > 0:
        # Slice the list of pages before and check against the ordering rules for this page
        if any(item in update[:i] for item in ordering_rules[update[i]]):
            is_valid_ordering = False
        i -= 1

    # All updates are of odd-numbered length, calculate midpoint using integer division
    if is_valid_ordering:
        sum_valid_middle_pages += update[len(update) // 2]

print(sum_valid_middle_pages)