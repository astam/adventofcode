import pysnooper

type Range = tuple[int, int]
type Ranges = list(Range)
type Map = list(tuple(int, int, int))
type Maps = list(Map)
type Lines = list(str)

@pysnooper.snoop()
def find(ranges: Ranges, maps: Maps):
    if maps == []:
        return min(ranges)
    locations = []
    old_ranges = ranges[:]
    ranges.append((9,9))
    new_ranges = []
    for mapping in maps[0]:
        print(mapping)
        # while

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
    find(seeds, maps)
    print(seeds)