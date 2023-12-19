def isvalid_pattern(pattern, ranges):
    split_pattern = [x for x in pattern.split('.') if x != '']
    count_groups = [str(len(x)) for x in split_pattern]
    if ','.join(count_groups) == ranges:
        return True
    else:
        return False

def get_possibilties(pattern, ranges):
    print()
    print(pattern)
    if '?' not in pattern:
        if isvalid_pattern(pattern, ranges):
            # print(pattern)
            return 1
        else:
            return 0
    
    pattern_so_far = pattern.split('?')
    print(pattern_so_far)
    if '#' in pattern_so_far[0]:
        groups = [x for x in pattern_so_far[0].split('.') if x != '']
        print(groups)
        groups_count = len(groups)
        print(groups_count)
        ranges_so_far = ranges.split(',')[0:groups_count]
        print(ranges_so_far)
        print(isvalid_pattern(pattern_so_far[0], ','.join(ranges_so_far)))
        exit()
        if len(ranges_so_far) > 0 and not isvalid_pattern(pattern_so_far[0], ','.join(ranges_so_far)):
            return 0
    # ranges_count = len(ranges.split(','))
    # print(ranges_count)
    # groups_count = len([x for x in pattern.split('.') if x != ''])
    # print(groups_count)
    # if ranges_count <= groups_count:
        # return get_possibilties(pattern.replace('?', '.', 1), ranges) + get_possibilties(pattern.replace('?', '#', 1), ranges)
    # else:
        # return 0
    return get_possibilties(pattern.replace('?', '.', 1), ranges) + get_possibilties(pattern.replace('?', '#', 1), ranges)


 
        


if __name__ == '__main__':
    input_file = '2023/day12/input_example.txt'
    # input_file = '2023/day12/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))
    sum = 0
    for line in lines[5:]:
        pattern, ranges = line.split(' ')
        pattern = '?'.join([pattern] * 5)
        ranges = ','.join([ranges] * 5)
        print(pattern)
        print(ranges)
        sum += get_possibilties(pattern, ranges)
    print(sum)
        