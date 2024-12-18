"""
Advent of Code 2024
Day 10 - Hoof It (Part 1)

Solution by Jacob Barber
"""

import numpy as np
from aoc_utils import get_args

MAX_ELEVATION = 9

# Parse program arguments
args = get_args(10, "Hoof It (Part 1)")

# Read input into matrix representing topographical trail map
with args.input_file as file:
    trail_map = np.array([list(line) for line in file.read().splitlines()], dtype=int)

# Get the trailhead positions and map boundaries
trailhead_positions = np.argwhere(trail_map == 0)

def score_path(trailhead_position, elevation_map):
    """
    Calculates the score of a path starting from a trailhead at elevation 0. The score
    is defined as the number of positions of elevation 9 that can be reached from a
    given trailhead.
    :param trailhead_position: The row/col position of the trailhead on the trail map.
    :param elevation_map: A 2D Numpy array of digits representing topographical elevations
    :return: An int representing the score of the path. Returns 0 if no complete path exists
    from this trailhead.
    """

    height, width = elevation_map.shape
    next_elevation = 1
    queue = [trailhead_position]

    while next_elevation <= MAX_ELEVATION:
        valid_paths = []

        # Determine valid paths
        while queue:
            row, col = queue.pop()

            # North
            if 0 < row < height and trail_map[row - 1][col] == next_elevation:
                valid_paths.append((row - 1, col))
            # East
            if 0 <= col < width - 1 and trail_map[row][col + 1] == next_elevation:
                valid_paths.append((row, col + 1))
            # South
            if 0 <= row < height - 1 and trail_map[row + 1][col] == next_elevation:
                valid_paths.append((row + 1, col))
            # West
            if 0 < col < width and trail_map[row][col - 1] == next_elevation:
                valid_paths.append((row, col - 1))

        # Swap buffers, removing duplicate values
        queue = set(valid_paths)

        # No valid paths, end search
        if not queue:
            return 0

        # Continue pathfinding
        next_elevation += 1

    # Valid positions will be in queue after last swap
    return len(queue)

# Calculate the score for each trailhead
sum_trailhead_scores = 0
for trailhead in trailhead_positions:
    sum_trailhead_scores += score_path(trailhead, trail_map)

# Output results
print(sum_trailhead_scores)