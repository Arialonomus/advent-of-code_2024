"""
Advent of Code 2024
Day 5 - Print Queue (Part 2)

Solution by Jacob Barber
"""

from collections import defaultdict
from aoc_utils import get_args

# Parse program arguments
args = get_args(5, "Print Queue (Part 2)")

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

# Filter invalid orderings
invalid_updates = []
for update in updates:
    # Iterate backwards through the list since our rules are "must come before"
    i = len(update) - 1
    is_valid_ordering = True
    while is_valid_ordering and i > 0:
        # Slice the list of pages before and check against the ordering rules for this page
        if any(item in update[:i] for item in ordering_rules[update[i]]):
            invalid_updates.append(update)
            is_valid_ordering = False
        i -= 1

# Sort the invalid updates according to the ordering rules
# NOTE: This works but is very inefficient, revisit algorithm later.
sum_middle_pages = 0
for update in invalid_updates:
    i = len(update) - 1
    while i > 0:
        j = i - 1
        switch_made = False
        while j >= 0 and not switch_made:
            if update[j] in ordering_rules[update[i]]:
                page_num = update.pop(i)
                update.insert(j, page_num)
                switch_made = True
            else:
                j -= 1

        if not switch_made:
            i -= 1

    sum_middle_pages += update[len(update) // 2]
print(sum_middle_pages)