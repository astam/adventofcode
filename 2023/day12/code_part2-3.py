from multiprocessing import Pool, TimeoutError
import time
import os

def f(x):
    return x*x

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

def process_line(line):
    pattern, ranges = line.split(' ')
    pattern = '?'.join([pattern] * 5)
    ranges = ','.join([ranges] * 5)
    # print()
    # print(pattern)
    # print(ranges)
    regex_pattern = r'[\.\?]*' + r'[\.\?]+'.join([r'[#\?]{' + re.escape(x) + r'}' for x in ranges.split(',')])
    # print(regex_pattern)
    sub_sum = get_valid_pattern_count(pattern, ranges, regex_pattern)
    print(pattern + '->' + str(sub_sum))
    return sub_sum

if __name__ == '__main__':
    # start 4 worker processes
    # input_file = '2023/day12/input_example.txt'
    input_file = '2023/day12/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]

    with Pool(processes=8) as pool:

        # print "[0, 1, 4,..., 81]"
        print(pool.map(process_line, lines))

        # # print same numbers in arbitrary order
        # pool.imap_unordered(process_line, lines)
        # for i in pool.imap_unordered(f, range(10)):
        #     print(i)

        # # evaluate "f(20)" asynchronously
        # res = pool.apply_async(f, (20,))      # runs in *only* one process
        # print(res.get(timeout=1))             # prints "400"

        # # evaluate "os.getpid()" asynchronously
        # res = pool.apply_async(os.getpid, ()) # runs in *only* one process
        # print(res.get(timeout=1))             # prints the PID of that process

        # # launching multiple evaluations asynchronously *may* use more processes
        # multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        # print([res.get(timeout=1) for res in multiple_results])

        # # make a single worker sleep for 10 seconds
        # res = pool.apply_async(time.sleep, (10,))
        # try:
        #     print(res.get(timeout=1))
        # except TimeoutError:
        #     print("We lacked patience and got a multiprocessing.TimeoutError")

        # print("For the moment, the pool remains available for more work")

    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")