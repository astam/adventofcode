from icecream import ic
import re
from collections import defaultdict

def print_matrix(matrix):
    print('\n'.join([''.join(x) for x in matrix]))
    print()

if __name__ == '__main__':
    # input_file = '2024/day8/input_example.txt'
    input_file = '2024/day8/input.txt'
    with open(input_file) as f:
        puzzle_input = [list(x) for x in f.read().split('\n')]
    # print('\n'.join([''.join(x) for x in puzzle_input]))
    print_matrix(puzzle_input)
    max_x, max_y = (len(puzzle_input[0]) - 1, len(puzzle_input) - 1)
    min_x, min_y = (0,0)

    # exit(0)
    ic(max_x, max_y)
    antennas = defaultdict(list)
    for y in range(len(puzzle_input)):
        for x in range(len(puzzle_input[y])):
            if puzzle_input[y][x] != '.':
                antennas[puzzle_input[y][x]].append((x,y))

    antinodes = 0
    for antenna, locations in antennas.items():
        # ic(antenna, locations)
        for first in locations:
            for last in locations:
                if first != last:
                    antinode_x = first[0] + (first[0] - last[0])
                    antinode_y = first[1] + (first[1] - last[1])
                    antinode = (antinode_x, antinode_y)
                    ic(antenna, first, last, antinode)
                    if min_x <= antinode_x <= max_x:
                        if min_y <= antinode_y <= max_y:
                            # antinodes += 1
                            # if puzzle_input[antinode_y][antinode_x] == '.':
                            puzzle_input[antinode_y][antinode_x] = '#'
    ic(antinodes)
    print_matrix(puzzle_input)
    ic(len([x for x in sum(puzzle_input, []) if x == '#']))