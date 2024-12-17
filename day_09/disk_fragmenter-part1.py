"""
Advent of Code 2024
Day 9 - Disk Fragmenter (Part 1)

Solution by Jacob Barber
"""

from aoc_utils import get_args

# Parse program arguments
args = get_args(9, "Disk Fragmenter (Part 1)")

# Read input line into disk map lists
with args.input_file as file:
    disk_map = file.read().strip()
    unplaced_file_blocks = list(map(int, disk_map[::2]))
    unfilled_gaps = list(map(int, disk_map[1::2]))

# Iteratively calculate checksum of properly de-fragmented filesystem
checksum = 0
position = 0
current_file = 0
end_file = len(unplaced_file_blocks) - 1
current_gap = 0

while sum(unplaced_file_blocks) != 0:    # Loop until all file blocks have been placed
    # Place all blocks of current file, updating checksum each iteration
    while unplaced_file_blocks[current_file] != 0:
        checksum += position * current_file   # File ID corresponds to file list index
        position += 1
        unplaced_file_blocks[current_file] -= 1

    # Fill gap using file blocks from end file until no empty blocks remain
    while unfilled_gaps[current_gap] != 0:
        checksum += position * end_file
        position += 1
        unplaced_file_blocks[end_file] -= 1
        unfilled_gaps[current_gap] -= 1
        if unplaced_file_blocks[end_file] == 0:
            # All blocks from end file are moved
            end_file -= 1

            # Discard empty block data after new end file
            unfilled_gaps[end_file] = 0

    # Advance iterators
    current_file += 1
    current_gap += 1

# Output results
print(checksum)
