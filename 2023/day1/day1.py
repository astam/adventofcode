import re

if __name__ == '__main__':
    # Part 1
    input_file = '2023/day1/input_example2.txt'
    input_file = '2023/day1/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines)
    digits_numbers= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    spelledout_digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    # digits = {
    #     ('oneight', '18'),
    #     ('threeight', '38'),
    #     ('fiveight', '58'),
    #     ('sevenine', '79'),
    #     ('eightwo', '82'),
    #     ('eighthree', '83'),
    #     ('zero', '0'),
    #     ('one', '1'),
    #     ('two', '2'),
    #     ('three', '3'),
    #     ('four', '4'),
    #     ('five', '5'),
    #     ('six', '6'),
    #     ('seven', '7'),
    #     ('eight', '8'),
    #     ('nine', '9')
    # }
    digits = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    # for digit in range(len(spelledout_digits)):
    #     lines = [x.replace(spelledout_digits[digit], digits[digit]) for x in lines]
    # parsed_lines = []
    # for line in lines:
    #     line2 = line
    #     while line2 != '':
    #         for digit in digits:
    #             if line2.startswith(digit[0]):
    #                 # print(spelledout_digits[i])
    #                 line = line.replace(digit[0], digit[1], 1)
    #         line2 = line2[1:]
    #     parsed_lines.append(line)



    # print(parsed_lines)
    # numbers = [[y for y in x if y in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]] for x in parsed_lines ]
    # print(numbers)
    # print(sum([int(x[0] + x[-1]) for x in numbers]))

    total = 0
    for line in lines:
        print()
        print(line)
        first = re.search(r'(\d|one|two|three|four|five|six|seven|eight|nine)', line)
        # print(match)
        print(first.group())
        last = re.search(r'(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)', line[::-1])
        print(last.group())
        first_number = first.group()
        last_number = last.group()[::-1]
        print(first_number + '-' + last_number)
        if first_number in spelledout_digits:
            first_number = digits[first_number]
        if last_number in spelledout_digits:
            last_number = digits[last_number]
        total += int(first_number + last_number)
        # print(match)
        # print(match.group())
        # print(match.group('first'))
    print(total)