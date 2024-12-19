from icecream import ic
import re

if __name__ == '__main__':
    # input_file = '2024/day3/input_example.txt'
    input_file = '2024/day3/input.txt'
    with open(input_file) as f:
        memory = f.read()
    ic(memory)

    x = sum([int(x) * int(y) for x,y in re.findall(r'mul\((\d+),(\d+)\)', memory)])
    ic(x)