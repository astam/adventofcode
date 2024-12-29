from icecream import ic
import math
from memoization import cached

@cached
def blink(value:int, depth:int):
    if depth == 0:
        return 1
    elif value == 0:
        return blink(1, depth - 1)
    digits = int(math.log10(value)) + 1
    if digits % 2 == 0:
        first = value // pow(10, digits // 2)
        last = value - first * pow(10, digits // 2)
        return blink(first, depth - 1) + blink(last, depth - 1)
    else:
        return blink(value * 2024, depth - 1)

if __name__ == '__main__':
    # input_file = '2024/day11/input_example.txt'
    input_file = '2024/day11/input.txt'
    with open(input_file) as f:
        puzzle_input = [int(x) for x in f.read().split(' ')]
    ic(puzzle_input)
    ic(sum(blink(x, 25) for x in puzzle_input))
