"""
Advent of Code 2024
Day 2 - Red-Nosed Reports (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

SAFE_THRESHOLD_MIN = 1
SAFE_THRESHOLD_MAX = 3

# Parse program arguments
args = get_args(2, "Red-Nosed Reports (Part 1)")

# Read input lines as reports
with args.input_file as file:
    reports = [list(map(int, line.split())) for line in file.read().splitlines()]

# Iterate through each report to determine if it is safe
total_safe_reports = 0
for report in reports:
    num_levels = len(report)
    delta = report[0] - report[1]
    is_increasing = delta < 0

    def check_if_safe(difference):
        """
        Checks if the delta between two levels if safe.
        Pre-Condition: Scoped variable is_increasing is set from the first 2 elements
        in a report
        :param difference: The difference of two adjacent integer levels in a report
        :return: True if the delta is safe, otherwise return False
        """
        return ((difference < 0) == is_increasing and
                SAFE_THRESHOLD_MIN <= abs(difference) <= SAFE_THRESHOLD_MAX)

    is_safe = check_if_safe(delta)
    i = 1

    # Check the delta and direction of each level in series
    while i < num_levels - 1 and is_safe:
        delta = report[i] - report[i + 1]
        is_safe = check_if_safe(delta)
        i += 1

    if is_safe:
        total_safe_reports += 1

# Print final output
print(total_safe_reports)


