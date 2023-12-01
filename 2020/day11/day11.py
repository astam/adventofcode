def print_grid(grid):
    for line in grid:
        # print(line)
        print(''.join(line))


if __name__ == '__main__':
    # Part 1
    input_file = '2020/day11/input_example.txt'
    # input_file = '2020/day10/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print(lines)
    lines.insert(0, '.' * len(lines[0]))
    lines.append('.' * len(lines[0]))
    lines = ['.{}.'.format(x) for x in lines]
    # for line in lines:
    #     print(line)
    # print([[y for y in x] for x in lines])
    # print([x for sublist in lines for x in sublist])
    grid = [[y for y in x] for x in lines]
    # print(grid)
    print_grid(grid)
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            print('{},{}:{}'.format(x,y,grid[x][y]))
            if 
    