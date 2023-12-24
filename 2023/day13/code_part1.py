if __name__ == '__main__':
    input_file = '2023/day13/input_example.txt'
    # input_file = '2023/day13/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    print('\n'.join(lines))
    print()

    patterns = []
    pattern = []
    for line in lines:
        if line != '':
            pattern.append(line)
        else:
            patterns.append(pattern)
            pattern = []
    patterns.append(pattern)

    # print(patterns)

    # Vertical
    for pattern in patterns:
        for line in pattern:
            print(line, int(len([x for x in pattern if x == line ])))
        print()

    # Rotate
    
