


if __name__ == '__main__':
    # Part 1
    input_file = '2020/day6/input_example.txt'
    input_file = '2020/day6/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print(lines)

    groups = []
    group = ""
    for line in lines:
        if line != '':
            group = group + line
        else:
            groups.append(group.strip())
            group = ""
    groups.append(group.strip())
    # print(groups)
    unique = sum([len(list(set(x))) for x in groups])
    print(unique)

    # Part 3

    groups = []
    group = []
    for line in lines:
        if line != '':
            group.append(list(line))
        else:
            groups.append(group)
            group = []
    groups.append(group)
    print(sum([len(set.intersection(*[set(x) for x in group])) for group in groups]))
