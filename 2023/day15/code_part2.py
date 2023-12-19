if __name__ == '__main__':
    input_file = '2023/day15/input_example2.txt'
    # input_file = '2023/day15/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    print('\n'.join(lines))