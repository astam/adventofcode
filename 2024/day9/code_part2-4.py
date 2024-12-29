from icecream import ic
import re
from collections import defaultdict
import sys
sys.setrecursionlimit(300000)

def decode(disk_map:list, file_id:int=0) -> list:
    if disk_map == []:
        return []
    elif len(disk_map) == 1:
        return [str(file_id)] * disk_map[0]
    else:
        return [str(file_id)] * disk_map[0] + ['.'] * disk_map[1] +\
                decode(disk_map[2:], file_id + 1)
    
if __name__ == '__main__':
    # input_file = '2024/day9/input_example.txt'
    input_file = '2024/day9/input.txt'
    with open(input_file) as f:
        disk_map = list(map(int, f.read()))
    # ic(disk_map)
    disk = decode(disk_map)
    file_types = ''
    for i in disk:
        if i == '.':
            file_types += '.'
        else:
            file_types += 'F'
    files = [x for x in enumerate(disk) if x[1] != '.']
    max_file_id = int(files[-1][1])
    for file_id in range(max_file_id, -1, -1):
        ic(file_id)
        start = min(x[0] for x in files if x[1] == str(file_id))
        end = max(x[0] for x in files if x[1] == str(file_id))
        size = end - start + 1
        space = file_types[:start].find('.' * size)
        if space >= 0:
            file_types = file_types[:start] + '.' * size + file_types[end + 1:]
            file_types = file_types[:space] + 'F' * size + file_types[space + size:]
            for i in range(size):
                disk[start + i] = '.'
                disk[space + i] = str(file_id)
    ic(sum(index * int(file_id) for index, file_id in enumerate(disk) if file_id != '.'))
