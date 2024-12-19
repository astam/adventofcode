from icecream import ic
import re

if __name__ == '__main__':
    # input_file = '2024/day4/input_example.txt'
    input_file = '2024/day4/input.txt'
    with open(input_file) as f:
        puzzle_input = f.read()
    # ic(puzzle_input)
    matrix = [list(x) for x in puzzle_input.split('\n')]
    # ic(matrix)

    # M.S
    # .A.
    # M.S

    total_count = 0
    for _ in range(4):
        matrix = list(map("".join, zip(*reversed(matrix))))
        for line in range(len(matrix) - 2):
            # ic(line)
            # ic(matrix[line])
            for character in range(len(matrix[line]) - 2):
                if (matrix[line][character] == 'M' and
                matrix[line][character + 2] == 'S' and
                matrix[line + 1][character + 1] == 'A' and
                matrix[line + 2][character] == 'M' and
                matrix[line + 2][character + 2] == 'S'):
                    total_count += 1
    ic(total_count)

            