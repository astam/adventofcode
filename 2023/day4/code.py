if __name__ == '__main__':
    input_file = '2023/day4/input_example.txt'
    input_file = '2023/day4/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))

    cards = [1] * len(lines)
    score = 0
    pointer = 0
    for line in lines:
        numbers = line.split(': ')[1]
        winning, drawn = numbers.split(' | ')
        winning_numbers = [int(x) for x in winning.split(' ') if x != '']
        drawn_numbers = [int(x) for x in drawn.split(' ') if x != '']
        hits = [x for x in drawn_numbers if x in winning_numbers]
        for count in range(len(hits)):
            cards[pointer + count + 1] += 1 * cards[pointer]
        print(str(pointer + 1) + ': ' + str(cards))
        # print(hits)
        if len(hits) > 0:
            # print(2 ** (len(hits) - 1))
            score += 2 ** (len(hits) - 1)
        pointer += 1
    print(score)
    print(cards)
    print(sum(cards))

    


