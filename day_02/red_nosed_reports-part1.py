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

    def check_if_safe(difference, initial_difference):
        """
        Checks if the delta between two levels if safe.
        :param difference: The difference of two adjacent integer levels in a report
        :param initial_difference: The difference of the first two integer levels in a report
        :return: True if the delta is safe, otherwise return False
        """
        directions_match = (difference < 0) == (initial_difference < 0)
        within_safe_threshold = SAFE_THRESHOLD_MIN <= abs(difference) <= SAFE_THRESHOLD_MAX
        return directions_match and within_safe_threshold

    # Check safety of first two levels
    initial_delta = report[0] - report[1]
    is_safe = check_if_safe(initial_delta, initial_delta)
    i = 1

    # Check the delta and direction of each remaining level in report
    num_levels = len(report)
    while i < num_levels - 1 and is_safe:
        is_safe = check_if_safe(report[i] - report[i + 1], initial_delta)
        i += 1

    if is_safe:
        total_safe_reports += 1

# Print final output
print(total_safe_reports)


