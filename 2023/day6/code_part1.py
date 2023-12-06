import math

if __name__ == '__main__':
    input_file = '2023/day6/input_example.txt'
    input_file = '2023/day6/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))

    times = [x for x in lines[0].split(' ') if x != '' and x != 'Time:']
    distances = [x for x in lines[1].split(' ') if x != '' and x != 'Distance:']

    # print(times)
    # print(distances)
    races = [(int(times[x]), int(distances[x])) for x in range(len(times))]
    # print(races)
    records = []
    for race in races:
        # print(race)
        race_time = race[0]
        record_distance = race[1]
        race_records = 0
        print('race_time: {}, record_distance: {}'.format(race_time, record_distance))
        for hold_time in range(1, race_time):
            # print(hold_time)
            rest_time = race_time - hold_time
            speed = hold_time
            distance_travelled = speed * rest_time
            print(distance_travelled)
            if distance_travelled > record_distance:
                race_records += 1
        records.append(race_records)
    print(records)
    print(math.prod(records))
    exit()
