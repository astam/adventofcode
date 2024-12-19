from icecream import ic
import re

def print_matrix(matrix):
    print('\n'.join([''.join(x) for x in matrix]))
    print()

if __name__ == '__main__':
    # input_file = '2024/day6/input_example.txt'
    input_file = '2024/day6/input.txt'
    with open(input_file) as f:
        puzzle_input = [list(x) for x in f.read().split('\n')]
    # print('\n'.join([''.join(x) for x in puzzle_input]))
    # print_matrix(puzzle_input)

    max_x, max_y = (len(puzzle_input[0]) - 1, len(puzzle_input) - 1)
    min_x, min_y = (0,0)                
    pos_x, pos_y = (0,0)
    steps = 0
    # Find start point
    for y in range(len(puzzle_input)):
        # ic(y)
        if '^' in puzzle_input[y]:
            # ic(puzzle_input[y])
            pos_y = y
            pos_x = puzzle_input[y].index('^')
    # ic(pos_x, pos_y)
    while True:
        match puzzle_input[pos_y][pos_x]:
            case '<':
                puzzle_input[pos_y][pos_x] = 'X'
                if pos_x - 1 < min_x:
                    break
                elif puzzle_input[pos_y][pos_x - 1] == '#':
                    pos_y -= 1
                    puzzle_input[pos_y][pos_x] = '^'
                else:
                    pos_x -= 1
                    puzzle_input[pos_y][pos_x] = '<'
            case '>':
                puzzle_input[pos_y][pos_x] = 'X'
                if pos_x + 1 > max_x:
                    break
                elif puzzle_input[pos_y][pos_x + 1] == '#':
                    pos_y += 1
                    puzzle_input[pos_y][pos_x] = 'v'
                else:
                    pos_x += 1
                    puzzle_input[pos_y][pos_x] = '>'
            case '^':
                puzzle_input[pos_y][pos_x] = 'X'
                if pos_y - 1 < min_y:
                    break
                elif puzzle_input[pos_y - 1][pos_x] == '#':
                    pos_x += 1
                    puzzle_input[pos_y][pos_x] = '>'
                else:
                    pos_y -= 1
                    puzzle_input[pos_y][pos_x] = '^'
            case 'v':
                puzzle_input[pos_y][pos_x] = 'X'
                if pos_y + 1 > max_y:
                    break
                elif puzzle_input[pos_y + 1][pos_x] == '#':
                    pos_x -= 1
                    puzzle_input[pos_y][pos_x] = '<'
                else:
                    pos_y += 1
                    puzzle_input[pos_y][pos_x] = 'v'
            case _:
                break
        # print_matrix(puzzle_input)
    ic(len([item for sublist in puzzle_input for item in sublist if item == 'X']))
