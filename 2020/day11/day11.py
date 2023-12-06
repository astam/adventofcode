import copy

def print_grid(grid):
    for line in grid:
        # print(line)
        print(''.join(line))

def serialize(grid):
    return ''.join([''.join(x) for x in grid])


if __name__ == '__main__':
    # Part 1
    input_file = '2020/day11/input_example.txt'
    input_file = '2020/day11/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print(lines)
    lines.insert(0, '.' * len(lines[0]))
    lines.append('.' * len(lines[0]))
    lines = ['.{}.'.format(x) for x in lines]
    for line in lines:
        print(line)
    # exit()
    # print([[y for y in x] for x in lines])
    # print([x for sublist in lines for x in sublist])
    grid = [[y for y in x] for x in lines]
    # grid_new = [['.' for y in x] for x in lines]
    # print(grid)
    # print_grid(grid)
    # exit()
    # print_grid(grid_new)
    # grid_new = copy.deepcopy(grid)
    # for _ in range(5):
    # print(serialize(grid))
    # print(serialize(grid_new))
    previous = serialize(grid)
    current = ''
    while previous != current:
        previous = current
        # print_grid(grid)
        grid_shadow = copy.deepcopy(grid)
        for x in range(1, len(grid[0]) - 1):
            for y in range(1, len(grid) - 1):
                # print('{},{}:{}'.format(x,y,grid[x][y]))
                # # if grid[x][y] == 'L':
                # print()
                # print(grid[x - 1])
                # print(grid[x])
                # print(grid[x + 1])
                # print()
                # print(grid[x - 1][y - 1:y + 2])
                adjacent = grid_shadow[x - 1][y - 1:y + 2] + grid_shadow[x + 1][y - 1:y + 2] + [grid_shadow[x][y - 1]] + [grid_shadow[x][y + 1]]
                count_adjacent_occupied = len([x for x in adjacent if x == '#'])
                # print()
                # print(adjacent)
                if grid_shadow[x][y] == 'L' and '#' not in adjacent:
                    grid[x][y] = '#'
                elif grid_shadow[x][y] == '#' and count_adjacent_occupied >= 4:
                    grid[x][y] = 'L'
                print(serialize(grid))
        current = serialize(grid)
        # print(previous)
        # print(current)
        # print('************************')

    # print_grid(grid)
    # print(serialize(grid))
    print(len([x for x in serialize(grid) if x == '#']))
    # print_grid(grid)
    # exit(0)
    