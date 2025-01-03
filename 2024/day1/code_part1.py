from icecream import ic

if __name__ == '__main__':
    # input_file = '2024/day1/input_example.txt'
    input_file = '2024/day1/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    print('\n'.join(lines))

    left_list = sorted([int(x.split(' ')[0]) for x in lines])
    right_list = sorted([int(x.split(' ')[-1]) for x in lines])
    ic(left_list)
    ic(right_list)
    diff = [abs(x[0]-x[1]) for x in zip(left_list, right_list)]
    ic(diff)
    ic(sum(diff))