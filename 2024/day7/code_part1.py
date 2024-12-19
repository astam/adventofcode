from icecream import ic
import re

def traverse(to_be:int, result:int, numbers:list):
    # ic(to_be, result, numbers)
    if numbers == []:
        if result == to_be:
            return True
        else:
            return False
    elif result == 0:
        return traverse(to_be, numbers[0], numbers[1:])
    else:
        return traverse(to_be, result + numbers[0], numbers[1:]) or \
        traverse(to_be, result * numbers[0], numbers[1:]) or \
        traverse(to_be, int(str(result) + str(numbers[0])), numbers[1:])
        

if __name__ == '__main__':
    # input_file = '2024/day7/input_example.txt'
    input_file = '2024/day7/input.txt'
    with open(input_file) as f:
        puzzle_input = f.read().split('\n')
    ic(len(puzzle_input))
    # equations = {int(x.split(': ')[0]):list(map(int, x.split(': ')[1].split(' '))) for x in puzzle_input}
    # ic(len(equations))
    # print('\n'.join([''.join(x) for x in puzzle_input]))
    # print_matrix(puzzle_input)
    total_calibration = 0
    for equation in puzzle_input:
        # ic(equation)
        to_be = int(equation.split(':')[0])
        numbers = list(map(int, equation.split(': ')[1].split(' ')))
        # ic(to_be, numbers)
        if traverse(to_be, 0, numbers):
            total_calibration += to_be
        # break

    ic(total_calibration)
