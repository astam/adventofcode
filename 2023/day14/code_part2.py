from __future__ import annotations
import timeit
from tqdm import tqdm
from dataclasses import dataclass
from functools import cache
import re
import pysnooper

def rotate(platform):
    return ' '.join(map(order_line, map(''.join,zip(*(platform.split())[::-1]))))

def order_block(block):
    return '.' * block.count('.') + 'O' * block.count('O')

def order_line(line):
    return '#'.join(map(order_block, line.split('#')))

def order_platform(platform):
    return ' '.join(map(order_line, platform.split(' ')))

def load(weight=1, platform=[]):
    print(weight, platform)
    if platform == '':
        return 0
    match platform[0]:
        case 'O':
            return 1 + load(weight=weight,platform=platform[1:])
        case ' ':
            return load(weight=weight + 1, platform=platform[1:])
        case _:
            return 0 + load(weight=weight, platform=platform[1:])

def load(platform):
    weight = len(platform.split())
    load = 0
    for line in platform.split():
        line_count = len([x for x in line if x == 'O'])
        line_load = line_count * weight
        load += line_load
        weight -= 1
    return(load)

if __name__ == '__main__':
    input_file = '2023/day14/input_example.txt'
    input_file = '2023/day14/input.txt'
    platform = open(input_file).read().replace('\n',' ')
    cycle_count = 1_000_000_000
    repeats = []
    cycles = []
    for cycle in range(1, cycle_count):
        for _ in range(4):
            platform = rotate(platform)
        if platform in cycles:
            if cycles in repeats:
                break
            repeats.append(cycles)
            cycles = []
        cycles.append(platform)
    last_platform = repeats[1][(cycle_count - (len(repeats[0]) - len(repeats[1]))) % len(repeats[1]) - 1]
    print(load(last_platform))
