from icecream import ic
import re

if __name__ == '__main__':
    # input_file = '2024/day3/input_example2.txt'
    input_file = '2024/day3/input.txt'
    with open(input_file) as f:
        memory = f.read()
    ic(memory)

    # x = sum([int(x) * int(y) for x,y in re.findall(r'mul\((\d+),(\d+)\)', memory)])
    # ic(x)
    x = re.findall(r'(mul\(\d+,\d+\)|don\'t\(\)|do\(\))', memory)
    ic(x)
    total = 0
    do = 1
    for action in x:
        if action.startswith('mul'):
            m = re.match(r'mul\((\d+),(\d+)\)', action)
            total += int(m.group(1)) * int(m.group(2)) * do
        elif action == 'don\'t()':
            do = 0
        elif action == 'do()':
            do = 1
    ic(total)