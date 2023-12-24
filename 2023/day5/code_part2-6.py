import pysnooper

# @pysnooper.snoop()
def intersection(interval1, interval2):
    if interval1[-1] < interval2[0]:
        return (interval1, (), interval2)
    elif interval2[-1] < interval1[0]:
        return (interval2, (), interval1)
    else:
        min_left = min(interval1[0], interval2[0])
        max_right = max(interval1[-1], interval2[-1])
        min_mid = max(interval1[0], interval2[0])
        max_mid = min(interval1[-1], interval2[-1])
        mid = (min_mid, max_mid)
        left = (min_left, min_mid - 1) if min_mid > min_left else ()
        right = (max_mid + 1, max_right) if max_mid < max_right else ()
        return(left, mid, right)

# @pysnooper.snoop()
def find(input_range, source_range):
    _ , mid, _ = intersection(input_range, source_range)
    if mid == ():
        return (input_range, (), ())
    else:
        return intersection(mid, input_range)

# @pysnooper.snoop()
def process(input_range, map_ranges):
    if map_ranges == []:
        return [input_range]
    result = []
    map_range = map_ranges.pop()
    source_range = (map_range[1], map_range[1] + map_range[2] - 1)
    left, mid, right = find(input_range, source_range)
    if left != ():
        result += process(left, map_ranges[:])
    if right != ():
        result += process(right, map_ranges[:])
    if mid != ():
        diff = map_range[0] - map_range[1]
        result.append((mid[0] + diff, mid[1] + diff))
    return result

if __name__ == '__main__':
    input_file = '2023/day5/input_example.txt'
    input_file = '2023/day5/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))
    # print(lines[0].split()[1:])
    seeds = lines[0].split()[1:]
    input_ranges = tuple([(int(seeds[x]), int(seeds[x]) + int(seeds[x + 1]) - 1) for x in range(0, len(seeds), 2)])
    # print(input_ranges)
    # exit()
    maps = []
    range_line = []
    for line in lines[2:]:
        # print(line)
        if line != '':
            if not line.endswith('map:'):
                # print(line)
                range_line.append(tuple(map(int, line.split(' '))))
        else:
            maps.append(range_line)
            range_line = []
    maps.append(range_line)
    # print(maps)
    # with pysnooper.snoop():
    for map_ranges in maps:
        # exit()
        # print(input_ranges)
        new_input_ranges = []
        for input_range in input_ranges:
            # new_input_ranges += process(input_range, map_ranges)
            new_input_ranges += process(input_range, map_ranges[:])
        # print(new_input_ranges)
        input_ranges = new_input_ranges[:]
    # print(input_ranges)
    print(min([x[0] for x in input_ranges]))
