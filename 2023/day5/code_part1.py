if __name__ == '__main__':
    input_file = '2023/day5/input_example.txt'
    # input_file = '2023/day5/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))

    # Part 1
    maps = []
    map = ""
    for line in lines:
        if line != '':
            map += '  ' + line
        else:
            maps.append(map.strip())
            map = ""
    maps.append(map.strip())
    print(maps)
    print()
    seeds = [int(y) for y in [x.split(': ') for x in maps if x.startswith('seeds')][0][1].split(' ')]
    print(seeds)
    print()
    
    locations = []
    for seed in seeds:
        next_item_name = 'seed'
        next_item_number = seed
        while next_item_name != 'location':
            print()
            print(next_item_name + ': ' + str(next_item_number))
            mapname, mapstring = [x for x in maps if x.startswith(next_item_name + '-')][0].split(' map: ')
            print(mapname)
            # print(mapstring)
            mapranges = mapstring.strip().split('  ')
            # print(mapranges)
            _, next_item_name = mapname.split('-to-')
            for range in mapranges:
                # print(range)
                matched = False
                dest, source, range = [int(x) for x in range.split(' ')]
                if source <= next_item_number <= source + range:
                    next_item_number = next_item_number + (dest - source)
                    matched = True
                print('source: {}, dest: {}, range: {} -> {}'.format(source, dest, range, matched))
                if matched:
                    break
                # print(next_item_number)
            print(next_item_name + ': ' + str(next_item_number))
        locations.append(next_item_number)
        exit()
    print(locations)
    print(min(locations))
