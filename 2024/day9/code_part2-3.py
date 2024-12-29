from icecream import ic
import re
from collections import defaultdict
import sys
sys.setrecursionlimit(30000)

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
        # return ','.join(blocks[0][0] * blocks[0][1]) + ',' + to_string(blocks[1:])

if __name__ == '__main__':
    input_file = '2024/day9/input_example2.txt'
    # input_file = '2024/day9/input.txt'
    with open(input_file) as f:
        disk_map = list(map(int, f.read()))
    # print('\n'.join([''.join(x) for x in puzzle_input]))
    # ic(disk_map)
    # print(''.join(map(str, disk_map)))
    # pairs = [tuple(disk_map[i:i + 2]) for i in range(0, len(disk_map), 2)]
    # ic(pairs)

    print('Decoding')
    blocks = decode(disk_map)
    ic(len(blocks))
    ic(sum(x[1] for x in blocks))
    # ic(blocks)
    # print(f'{to_string(blocks)}')
    new_blocks = []
    loop = 0
    files = []
    block_count = len(blocks)
   
    print('Defragging')
    for j in [x for x in reversed(blocks)]:
        file_id = j[0]
        file_size = j[1]
        if file_id != '.':
            # print()
            if j[0] == '3':
                print(f'{to_string(blocks)}')
            # ic(j)
            j_idx = [x for x in enumerate(blocks) if x[1][0] == file_id][0][0]
            # ic(j_idx, j)
            for i_idx, i in enumerate(blocks):
                # ic(i_idx, i, j_idx, j)
                if i[0] == '.' and file_size <= i[1] and i_idx < j_idx:
                    found = True
                    break
                else:
                    found = False
            if found:
                left_space = i[1] - j[1]
                # ic(left_space)
                new_blocks = blocks[:i_idx] + [j]
                # print(f'{to_string(new_blocks)}')

                if left_space > 0:
                    if blocks[i_idx + 1][0] == '.':
                        blocks[i_idx + 1][1] = \
                            (blocks[i_idx + 1][0], blocks[i_idx + 1][1] + left_space)
                    else:
                        new_blocks += [('.', left_space)]
                # print(f'{to_string(new_blocks)}')
                
                new_blocks += blocks[i_idx + 1:j_idx]
                # print(f'{to_string(new_blocks)}')

                if new_blocks[-1][0] == '.':
                    new_blocks[-1] = \
                        (new_blocks[-1][0], new_blocks[-1][1] + file_size)
                    # print(f'{to_string(new_blocks)}')
                    if len(blocks) - 1 > j_idx  and blocks[j_idx + 1][0] == '.':
                        new_blocks[-1] = \
                            (new_blocks[-1][0], new_blocks[-1][1] + blocks[j_idx + 1][1])
                        if j[0] == '3':
                            print(f'{to_string(new_blocks)}')
                        # ic(len(blocks), j_idx)
                        if len(blocks) > j_idx:
                            new_blocks += blocks[j_idx + 2:]
                            # print(f'{to_string(new_blocks)}')
                else:
                    if len(blocks) - 1 > j_idx and blocks[j_idx + 1][0] == '.':
                        blocks[j_idx + 1] = \
                            (blocks[j_idx + 1][0], blocks[j_idx + 1][1] + file_size)
                        if len(blocks) > j_idx + j[1] + 1:
                            new_blocks += blocks[j_idx + 2:]
                    else:
                        new_blocks += [('.', j[1])]
                        if len(blocks) > j_idx + j[1]:
                            new_blocks += blocks[j_idx + 1:]
            # try:
            #     new_blocks = compress_freespace(new_blocks)
            # except RecursionError as e:
            #     ic(e)
            blocks = new_blocks.copy()
        # if j[0] == '6':
        #     exit()

        
        if j[0] == '3':
            print(f'{to_string(blocks)}')
    print('Checksumming')
    # 3675058781150
    # 102579145
    checksum = 0
    idx = 0
    for x in blocks:
        # ic(idx, x)
        if x[0] != '.':
            for delta_idx in range(idx, idx + x[1]):
                checksum += delta_idx * int(x[0])
                # ic(delta_idx, x, delta_idx * int(x[0]))
        idx += x[1]

    ic(checksum)
