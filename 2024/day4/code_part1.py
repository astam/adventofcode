from icecream import ic
import re

if __name__ == '__main__':
    # input_file = '2024/day4/input_example.txt'
    input_file = '2024/day4/input.txt'
    with open(input_file) as f:
        puzzle_input = f.read()
    # ic(puzzle_input)
    total_count = 0

    matrix = [x for x in puzzle_input.split('\n')]
    for _ in range(4):
        # ic(matrix)
        matrix = list(map("".join, zip(*reversed(matrix))))
        total_count += sum([x.count('XMAS') for x in matrix])
        # ic(matrix)

        trailing = len(matrix[0]) - 1
        leading = 0
        offsetted = []
        for line in matrix:
            offsetted.append(' ' * leading + line + ' ' * trailing)
            leading += 1
            trailing -= 1
        # ic(offsetted)
        rotated = list(map("".join, zip(*reversed(offsetted))))
        # ic(rotated)
        total_count += sum([x.count('XMAS') for x in rotated])


    ic(total_count)