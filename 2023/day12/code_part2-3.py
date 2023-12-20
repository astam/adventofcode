from multiprocessing import Pool
import re
# from tqdm import tqdm
import time
from tqdm.auto import tqdm
from p_tqdm import p_map, p_umap, p_imap, p_uimap

MAX_WORKERS = 5
CHUNK_SIZE = 5

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
    if regex_pattern.match(pattern):
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

def process_line(line):
    pattern, ranges = line.split(' ')
    pattern = '?'.join([pattern] * 5)
    ranges = ','.join([ranges] * 5)
    # print()
    # print(pattern)
    # print(ranges)
    regex_pattern = re.compile(r'[\.\?]*' + r'[\.\?]+'.join([r'[#\?]{' + re.escape(x) + r'}' for x in ranges.split(',')]))
    # print(regex_pattern)
    sub_sum = get_valid_pattern_count(pattern, ranges, regex_pattern)
    # print(pattern + '->' + str(sub_sum))
    return sub_sum

if __name__ == '__main__':
    input_file = '2023/day12/input_example.txt'
    input_file = '2023/day12/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # results = []
    # for line in tqdm(lines):
    #     result = process_line(line)
    #     results.append(result)

    results = p_umap(process_line, lines)

    print(sum(results))


    # with Pool(processes=8) as pool:
    #     print(sum(pool.map(process_line, lines)))

    # with Pool(processes=8) as pool:
    #     results = tqdm(
    #         pool.map(
    #             process_line,
    #             lines, 
    #             chunksize=CHUNK_SIZE
    #         ),
    #         total=len(lines),
    #     )
    #     print(results)

    # pool = Pool(processes=8)

    # result_list_tqdm = []
    # for result in tqdm(pool.imap(func=process_line, iterable=lines), total=len(lines)):
    #     result_list_tqdm.append(result)

    # print(result_list_tqdm)