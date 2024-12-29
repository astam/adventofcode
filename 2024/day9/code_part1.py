from icecream import ic
import re
from collections import defaultdict
import sys

def decode(disk_map:list, file_id:int=0) -> list:
    # print(''.join(map(str, disk_map)))
    if disk_map == []:
        return []
    elif len(disk_map) == 1:
        return [str(file_id)] * disk_map[0]
    else:
        return [str(file_id)] * disk_map[0] + \
            ['.'] * disk_map[1] + \
                decode(disk_map[2:], file_id + 1)

if __name__ == '__main__':
    # input_file = '2024/day9/input_example.txt'
    input_file = '2024/day9/input.txt'
    with open(input_file) as f:
        disk_map = list(map(int, f.read()))
    # print('\n'.join([''.join(x) for x in puzzle_input]))
    # ic(disk_map)
    # print(''.join(map(str, disk_map)))

    sys.setrecursionlimit(20000)
    # ic(decode(disk_map))
    blocks = decode(disk_map)
    # print(''.join(blocks))
    
    for i in range(len(blocks)):
        if blocks[i] == '.':
            for j in range(len(blocks) - 1, -1 + i, -1):
                if blocks[j] != '.':
                    break
            blocks[i] = blocks[j]
            blocks[j] = '.'

            # print(''.join(blocks))

    numerized = map(int, [x for x in blocks if x != '.'])
    ic(sum([x * y for x,y in enumerate(numerized)]))



