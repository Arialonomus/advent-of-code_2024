"""
Advent of Code 2024
Day 7 - Bridge Repair (Part 2)

Solution by Jacob Barber
"""

from aoc_utils import get_args

# Parse program arguments
args = get_args(7, "Bridge Repair (Part 2)")

# Store calibration equations as tuples of a test value and list of operands
with args.input_file as file:
    calibration_equations = []
    for line in file:
        test_str, num_list_str = line.split(':')
        calibration_equations.append((int(test_str), list(map(int, num_list_str.split()))))

# Iterate through equations testing for validity
sum_valid_test_values = 0
for equation in calibration_equations:
    test_value, operands = equation
    num_operands = len(operands)
    queue = [operands[0]]
    i = 1
    # Build a tree of equations possible through left-to-right operations
    while i < num_operands:
        results = []
        # Process all values at this level, cull branches if result exceeds test_value
        while queue:
            value = queue.pop(0)

            # Addition
            addition_result = value + operands[i]
            if addition_result <= test_value:
                results.append(addition_result)

            # Multiplication
            multiplication_result = value * operands[i]
            if multiplication_result <= test_value:
                results.append(multiplication_result)

            # Concatenation
            concatenation_result = int(str(value) + str(operands[i]))
            if concatenation_result <= test_value:
                results.append(concatenation_result)

        # Swap buffers and advance to the next level
        queue = results
        i += 1

    # Final values will be in queue as a result of the last swap
    if test_value in queue:
        sum_valid_test_values += test_value

# Output result
print(sum_valid_test_values)
