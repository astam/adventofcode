def check_pattern(pattern, ranges):
    spaced_pattern = pattern.replace('.', ' ')
    split_pattern = [x for x in spaced_pattern.split(' ') if x != '']
    count_groups = [str(len(x)) for x in split_pattern]
    if ','.join(count_groups) == ranges:
        return True
    else:
        return False

def get_possibilties(pattern):
    possibilties = []
    if '?' not in pattern:
        possibilties.append(pattern)
    else:
        possibilties += get_possibilties(pattern.replace('?', '.', 1))
        possibilties += get_possibilties(pattern.replace('?', '#', 1))
    return possibilties
        


if __name__ == '__main__':
    input_file = '2023/day12/input_example.txt'
    input_file = '2023/day12/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))
    sum = 0
    for line in lines:
        pattern, ranges = line.split(' ')
        # print(pattern)
        # print(ranges)
        possibilities = get_possibilties(pattern)
        sum += len([x for x in possibilities if check_pattern(x, ranges)])
        # print()
    # print(check_pattern('#.#.###', '1,1,3'))
    print(sum)
        