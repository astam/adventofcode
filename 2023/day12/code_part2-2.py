import re
from tqdm import tqdm

def isvalid_pattern(pattern, ranges):
    split_pattern = [x for x in pattern.split('.') if x != '']
    count_groups = [str(len(x)) for x in split_pattern]
    if ','.join(count_groups) == ranges:
        return True
    else:
        return False

def get_valid_pattern_count(pattern, ranges, regex_pattern):
    # print()
    # print(pattern)
    if re.match(regex_pattern, pattern):
        if '?' not in pattern:
            # print(pattern)
            # print('found')
            if isvalid_pattern(pattern, ranges):
                # print(pattern)
                return 1
            else:
                return 0
        else:
            # print('match')
            return get_valid_pattern_count(pattern.replace('?', '.', 1), ranges, regex_pattern) + get_valid_pattern_count(pattern.replace('?', '#', 1), ranges, regex_pattern)
    else:
        return 0
    # return get_valid_pattern_count(pattern.replace('?', '.', 1), ranges, regex_pattern) + get_valid_pattern_count(pattern.replace('?', '#', 1), ranges, regex_pattern)



if __name__ == '__main__':
    input_file = '2023/day12/input_example2.txt'
    # input_file = '2023/day12/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    print('\n'.join(lines))
    sum = 0
    for line in lines:
        pattern, ranges = line.split(' ')
        pattern = '?'.join([pattern] * 5)
        ranges = ','.join([ranges] * 5)
        # print()
        print(pattern)
        print(ranges)
        regex_pattern = r'[\.\?]*' + r'[\.\?]+'.join([r'[#\?]{' + re.escape(x) + r'}' for x in ranges.split(',')])
        # print(regex_pattern)
        sub_sum = get_valid_pattern_count(pattern, ranges, regex_pattern)
        print(pattern + '->' + str(sub_sum))
        sum += sub_sum
        # exit()
    print(sum)
        