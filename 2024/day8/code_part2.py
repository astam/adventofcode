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
        antenna_grid = [list(x) for x in f.read().split('\n')]
    # print('\n'.join([''.join(x) for x in puzzle_input]))
    print_matrix(antenna_grid)
    max_x, max_y = (len(antenna_grid[0]) - 1, len(antenna_grid) - 1)
    min_x, min_y = (0,0)
    antinode_grid = [['.'] * (max_x + 1) for _ in range(max_y + 1)]
    print_matrix(antinode_grid)
    # ic(antinode_grid)

    # exit(0)
    ic(max_x, max_y)
    antennas = defaultdict(list)
    for y in range(len(antenna_grid)):
        for x in range(len(antenna_grid[y])):
            if antenna_grid[y][x] != '.':
                antennas[antenna_grid[y][x]].append((x,y))
    ic(antennas)

    for antenna, locations in antennas.items():
        # ic(antenna, locations)
        for first in locations:
            for last in locations:
                if first != last:
                    diff_x = first[0] - last[0]
                    diff_y = first[1] - last[1]
                    antinode_x, antinode_y = first
                    while min_x <= antinode_x <= max_x and min_y <= antinode_y <= max_y:
                        antinode_grid[antinode_y][antinode_x] = '#'
                        antinode_x += diff_x
                        antinode_y += diff_y
                        antinode = (antinode_x, antinode_y)
                        ic(antenna, first, last, antinode)
                    # if min_x <= antinode_x <= max_x:
                    #     if min_y <= antinode_y <= max_y:
                    #         antinode_grid[antinode_y][antinode_x] = '#'
                    # print_matrix(antinode_grid)
                            
    print_matrix(antenna_grid)
    print_matrix(antinode_grid)
    ic(len([x for x in sum(antinode_grid, []) if x == '#']))