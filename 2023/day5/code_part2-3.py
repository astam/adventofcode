# import time
import random
from multiprocessing import Pool
# from tqdm import tqdm
import tqdm

def find_lowest_location(seed):
    allmapranges = []
    for map in maps[1:]:
        _,mapranges = map.split(' map:  ')
        allmapranges.append([[int(y) for y in x.split(' ')] for x in mapranges.split('  ')])
    seed_start, seed_range = seed
    min_loc = -1
    for seed in range(seed_start, seed_start + seed_range):
        # next_item_name = 'seed'
        next_item_number = seed
        for mapranges in allmapranges:
            for maprange in mapranges:
                # print(range)
                matched = False
                dest, source, reach = maprange
                if source <= next_item_number <= source + reach:
                    next_item_number = next_item_number + (dest - source)
                    matched = True
                # print('source: {}, dest: {}, range: {} -> {}'.format(source, dest, range, matched))
                if matched:
                    break
        if min_loc == -1 or next_item_number < min_loc:
                min_loc = next_item_number
    return min_loc

if __name__ == '__main__':
    input_file = '2023/day5/input_example2.txt'
    # input_file = '2023/day5/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))
    maps = []
    map = ""
    for line in lines:
        if line != '':
            map += '  ' + line
        else:
            maps.append(map.strip())
            map = ""
    maps.append(map.strip())
    seeds = [int(y) for y in [x.split(': ') for x in maps if x.startswith('seeds')][0][1].split(' ')]
    seed_ranges = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]
    # allmapranges = []
    # for map in maps[1:]:
    #     _,mapranges = map.split(' map:  ')
    #     allmapranges.append([[int(y) for y in x.split(' ')] for x in mapranges.split('  ')])
    # # print(allmapranges)
    
    # for seed_start, seed_range in seed_ranges:
    #     print(str(seed_start) + '->' + str(seed_start + seed_range))
    #     find_lowest_location(seed_start, seed_range)
    
    exit()
    with Pool(1) as p:
        r = list(tqdm.tqdm(p.imap(find_lowest_location, seed_ranges), total=len(seed_ranges)))
        print(r)



# pool = Pool(8)
# for _ in tqdm.tqdm(pool.imap_unordered(myfunc, range(100)), total=100):
#     pass
# pool.close()
# pool.join()