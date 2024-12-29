from icecream import ic
import re
from collections import defaultdict

if __name__ == '__main__':
    # input_file = '2024/day8/input_example.txt'
    input_file = '2024/day8/input.txt'
    with open(input_file) as f:
        puzzle_input = [list(x) for x in f.read().split('\n')]
    # print('\n'.join([''.join(x) for x in puzzle_input]))
    ic(puzzle_input)
    