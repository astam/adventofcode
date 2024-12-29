from icecream import ic
import re
from collections import defaultdict
import sys

def decode(disk_map:list, file_id:int=0) -> list:
    # print(''.join(map(str, disk_map)))
    if disk_map == []:
        return []
    elif len(disk_map) == 1:
        return [(str(file_id),disk_map[0])]
    else:
        return [(str(file_id), disk_map[0])] + \
            [('.',disk_map[1])] + \
                decode(disk_map[2:], file_id + 1)

def compress_freespace(blocks:list):
    # print(to_string(blocks))
    if blocks == []:
        return []
    elif blocks[0][0] == '.':
        i = 0
        total_space = 0
        while i < (len(blocks)) and blocks[i][0] == '.':
            # ic(i, blocks)
            total_space += blocks[i][1]
            i += 1
        # ic(total_space)
        if i < len(blocks) - 1:
            return [('.', total_space)] + compress_freespace(blocks[i:])
        else:
            return [('.', total_space)]   
    else:
        return [blocks[0]] + compress_freespace(blocks[1:])

def to_string(blocks:list):
    if blocks == []:
        return ''
    else:
        return blocks[0][0] * blocks[0][1] + to_string(blocks[1:])
        # return blocks[0][0] * blocks[0][1] + ',' + to_string(blocks[1:])

if __name__ == '__main__':
    input_file = '2024/day9/input_example.txt'
    # input_file = '2024/day9/input.txt'
    with open(input_file) as f:
        disk_map = list(map(int, f.read()))
    # print('\n'.join([''.join(x) for x in puzzle_input]))
    ic(disk_map)
    # print(''.join(map(str, disk_map)))
    # pairs = [tuple(disk_map[i:i + 2]) for i in range(0, len(disk_map), 2)]
    # ic(pairs)

    blocks = decode(disk_map)
    ic(blocks)
    new_blocks = []

    while True:
        for i in range(len(blocks)):
            if blocks[i][0] == '.':
                for j in range(len(blocks) - 1, -1 + i, -1):
                    # ic(i, blocks[i], j, blocks[j])
                    if blocks[j][0] != '.' and blocks[j][1] <= blocks[i][1]:
                        found = True
                        ic(i,blocks[i],j,blocks[j])
                        break
                    else:
                        found = False
                if found:
                    left_space = blocks[i][1] - blocks[j][1]
                    new_blocks = blocks[:i] + [blocks[j]]
                    if left_space > 0:
                        new_blocks += [('.', left_space)]
                    new_blocks += blocks[i + 1:j]
                    new_blocks += [('.', blocks[i][1] - left_space)]
                    if len(blocks) > j:
                        new_blocks += blocks[j + 1:]
                    # ic(new_blocks)
                    # if blocks[j][1] < blocks[i][1]:
                    #     left_space = blocks[i][1] - blocks[j][1]
                    #     new_blocks = blocks[:i] + [blocks[j]] + [('.', left_space)] + blocks[i + 1:j] + ()
                    # else:
                    #     new_blocks = blocks[:i] + [blocks[j]] + blocks[i + 1:j]
                break
        # print(f'{to_string(blocks)=}')
        # ic(new_blocks)
        try:
            new_blocks = compress_freespace(new_blocks)
        except RecursionError as e:
            ic(e)
        # ic(new_blocks)
        print(f'{to_string(new_blocks)}')
        # exit()
        if blocks == new_blocks:
            break
        else:
            blocks = new_blocks.copy()
        print()
    

    # sys.setrecursionlimit(20000)
    # ic(decode(disk_map))
    # blocks = decode(disk_map)
    # print(''.join(blocks))
    
    # for i in range(len(blocks)):
    #     if blocks[i] == '.':
    #         for j in range(len(blocks) - 1, -1 + i, -1):
    #             if blocks[j] != '.':
    #                 break
    #         blocks[i] = blocks[j]
    #         blocks[j] = '.'

    #         # print(''.join(blocks))

    # numerized = map(int, [x for x in blocks if x != '.'])
    # ic(sum([x * y for x,y in enumerate(numerized)]))



