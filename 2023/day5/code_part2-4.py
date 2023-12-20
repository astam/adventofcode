type Ranges = list[tuple[int, int]]

(79, 14)

50 98 2
52 50 48



def find(input_ranges: Range, map_number=0):
    new_ranges = []
    for r in input_ranges:
        for map_range in allmapranges[map_number]:
            dst, src, rng = map_range



if __name__ == '__main__':
    input_file = '2023/day5/input_example.txt'
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
    seed_ranges = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
    allmapranges = []
    for map in maps[1:]:
        _,mapranges = map.split(' map:  ')
        allmapranges.append([[int(y) for y in x.split(' ')] for x in mapranges.split('  ')])
    print(allmapranges)
    print(seed_ranges)
    
    # for seed_start, seed_range in seed_ranges:
    #     print(str(seed_start) + '->' + str(seed_start + seed_range))
    #     exit()
