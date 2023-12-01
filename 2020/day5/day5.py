# Part 1
def get_seat(begin, end, code):
    mid = begin + (end - begin ) // 2
    if len(code) == 0:
        return begin
    else:
        match code[0]:
            case 'F':
                return get_seat(begin, mid, code[1:])
            case 'B':
                return get_seat(mid + 1, end, code[1:])
            case 'L':
                return get_seat(begin, mid, code[1:])
            case 'R':
                return get_seat(mid + 1, end, code[1:])

if __name__ == '__main__':
    # print(get_seat(0, 127, 'FBFBBFFRLR'[:-3]))
    # print(get_seat(0, 7, 'FBFBBFFRLR'[-3:]))
    # print(get_seat(0, 127, 'FBFBBFFRLR'[:-3]) * 8 + get_seat(0, 7, 'FBFBBFFRLR'[-3:]))

    input_file = '2020/day5/input_example.txt'
    input_file = '2020/day5/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print(lines)

    # for line in lines:
    #     print(get_seat(0, 127, line[:-3]) * 8 + get_seat(0, 7, line[-3:]))
    print(max([get_seat(0, 127, x[:-3]) * 8 + get_seat(0, 7, x[-3:]) for x in lines]))

    # of met 1 regel
    print(max([int(x.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'), 2) for x in lines]))

    # Part 2
    # Filter 1st and last row
    minus_rows = [x for x in lines if not x.startswith('BBBBBBB') and not x.startswith('FFFFFFF')]
    # Make list with values
    values = [int(x.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'), 2) for x in minus_rows]
    seat = [x for x in range(min(values), max(values)) if x not in values and (x - 1) in values and (x + 1) in values]
    print(seat)