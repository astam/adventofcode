import re

if __name__ == '__main__':
    input_file = '2023/day1/input_example2.txt'
    input_file = '2023/day1/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines)
    digits_numbers= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    spelledout_digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
    digits = {'zero': '0','one': '1','two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9'}
    total = 0
    for line in lines:
        first = re.search(r'(\d|one|two|three|four|five|six|seven|eight|nine)', line)
        last = re.search(r'(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)', line[::-1])
        first_number = first.group()
        last_number = last.group()[::-1]
        if first_number in spelledout_digits:
            first_number = digits[first_number]
        if last_number in spelledout_digits:
            last_number = digits[last_number]
        total += int(first_number + last_number)
    print(total)