type Range = tuple[int, int]
type Map = list(tuple(int, int, int))
type Maps = list(Map)
type Lines = list(str)

# seed: 79..92
# map : 98..99 -> 50..51 
# seed: 79..92
# map : 50..97 -> 52..99
# seed: 81..94



# seed: 55..57
# map : 98..99 -> 50..51 
# seed: 55..57
# map : 50..97 -> 52..99
# seed: 57..59


# seed: 81..94
# map : 25..94 -> 18..87
# seed: 74..87








def find(input_range: Range, maps: Maps):
    print()
    if maps == []:
        return min(range)
    locations = []
    for map_range in maps[0]:
        print(map_range)
        dest_range_start, source_range_start, range_length = map_range
        dest_range_end = dest_range_start + range_length - 1
        source_range_end = source_range_start + range_length - 1
        diff_dest_source = dest_range_start - source_range_start
        range_start = input_range[0]
        range_length = input_range[1]
        print(dest_range_start, dest_range_end)
        print(source_range_start, source_range_end)
        print(diff_dest_source)
        print(range_start, range_length)
        if range_start >= source_range_start:
            if range_start  <= source_range_end:
                locations.append(find((range_start + diff_dest_source, range_length), maps[1:]))
            else:
                print('edga case!')
                exit()
        else:
            locations.append(find(input_range, maps[1:]))
    # exit()
    return locations

# def parse(lines: Lines):
#     if lines == []:
#         return []
#     if lines[0].startswith('seeds:'):



if __name__ == '__main__':
    input_file = '2023/day5/input_example.txt'
    # input_file = '2023/day5/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))
    # print(lines[0].split()[1:])
    seeds = lines[0].split()[1:]
    seeds = [(int(seeds[x]), int(seeds[x + 1])) for x in range(0, len(seeds), 2)]
    print(seeds)
    maps = []
    map_ranges = []
    for line in lines[2:]:
        # print(line)
        if line != '':
            if not line.endswith('map:'):
                # print(line)
                map_ranges.append(tuple(map(int, line.split(' '))))
        else:
            maps.append(map_ranges)
            map_ranges = []
    maps.append(map_ranges)
    print(maps)
    for seed in seeds:
        find(seed, maps)
        exit()