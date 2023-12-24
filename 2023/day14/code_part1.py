import timeit

def print_patform(platform):
    for x in platform:
        for y in x:
            print(y, end='')
        print()

if __name__ == '__main__':
    input_file = '2023/day14/input_example.txt'
    input_file = '2023/day14/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))
    # print()
    platform = [[y for y in x] for x in lines]
    # print_patform(platform)
    # print()
    starttime = timeit.default_timer()
    for _ in range(len(platform)):
        for x in range(len(platform) - 1):
            for y in range(len(platform[0])):
                if platform[x + 1][y] == 'O' and platform[x][y] == '.':
                    platform[x][y] = 'O'
                    platform[x + 1][y] = '.'
            # print_patform(platform)
            # print()
    diff =  timeit.default_timer() - starttime
    print("The time difference is :", diff)

    weight = len(platform)
    load = 0
    for line in platform:
        load += weight * len([x for x in line if x == 'O'])
        weight -= 1
    print(load)