from icecream import ic
import re
from functools import cmp_to_key

if __name__ == '__main__':
    input_file = '2024/day6/input_example.txt'
    # input_file = '2024/day6/input.txt'
    with open(input_file) as f:
        puzzle_input = [x for x in f.read().split('\n')]
    ic(puzzle_input)
