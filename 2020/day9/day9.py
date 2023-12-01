
if __name__ == '__main__':
    input_file = '2020/day9/input_example.txt'
    input_file = '2020/day9/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print(lines)
    numbers = [int(x) for x in lines]
    # print(numbers)

    preamble = 25
    for pos in range(preamble, len(numbers)):
        # print(numbers[pos])
        # print(numbers[pos - preamble:pos])
        sums = []
        for x in range(pos - preamble,pos):
            # print(x)
            for y in range(pos - preamble,pos):
                if x != y:
                    sums.append(numbers[x] + numbers[y])
        # print(sums)
        if numbers[pos] not in sums:
            invalid_number = numbers[pos]
        # print()
    print(invalid_number)

    for start in range(0, len(numbers)):
        for end in range(start + 2, len(numbers) + 1):
            r = numbers[start:end]
            # print(r)
            if sum(r) == invalid_number:
                print(r)
                print(min(r))
                print(max(r))
                print(min(r) + max(r))