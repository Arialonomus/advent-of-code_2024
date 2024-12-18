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
    disk_map_str = file.read().strip()
    unplaced_file_blocks = list(map(int, disk_map_str[::2]))
    unfilled_gaps = list(map(int, disk_map_str[1::2]))
    unfilled_gaps.append(0) # Add an empty gap to the end so the lists are the same size

    # Build a list of files and their gaps using array representing ID, size, and gap length
    file_layout = []
    for i in range(len(unplaced_file_blocks)):
        file_layout.append([i, unplaced_file_blocks[i], unfilled_gaps[i]])

# Attempt to move files leftward to fill gaps
num_files = len(file_layout)
current_file = num_files - 1
while current_file >= 0:
    # Find the leftmost gap that can fit the file, if one exists
    current_gap = 0
    current_file_id, current_file_size, right_gap_len = file_layout[current_file]
    while current_gap < current_file and file_layout[current_gap][2] < current_file_size:
        current_gap += 1

    # Leftmost gap found
    if current_gap != current_file:
        # Update the gap length of the file to the left
        file_layout[current_file - 1][2] += current_file_size + right_gap_len

        # Remove the file from the list
        file_layout.pop(current_file)

        # Insert the file in the leftmost block of the gap, update gap lengths for it and its neighbor
        filled_gap_size = file_layout[current_gap][2]
        file_layout.insert(current_gap + 1,
                           [current_file_id, current_file_size, filled_gap_size - current_file_size])
        file_layout[current_gap][2] = 0

    # No gap exists
    else:
        # Only decrement here since the index of the next file to search
        # is equal to the previous file if the previous file was moved
        # into a more leftward gap
        current_file -= 1

# Calculate checksum based on file sizes and gap lengths
checksum = 0
position = 0
for file in file_layout:
    file_id, file_size, gap_len = file
    end_index = position + file_size - 1
    checksum += file_id * ( file_size / 2) * ( position + end_index )
    position += file_size + gap_len

# Output results
print(checksum)
