import re

input_file = '2020/day2/input_example.txt'
input_file = '2020/day2/input.txt'
with open(input_file) as f:
    lines = [line.strip() for line in f.readlines()]
print(lines)

# Part 1
correct_passwords = 0
for line in lines:
    match = re.match(r'(?P<min>\d+)-(?P<max>\d+)\s+(?P<char>\w{1}):\s+(?P<password>\w+)', line)
    print(match.groupdict())
    min = int(match.group('min'))
    max = int(match.group('max'))
    char = match.group('char')
    password = match.group('password')
    char_count = len([c for c in password if c in char])
    print(char_count)
    if min <= char_count <= max:
        print('True')
        correct_passwords += 1
    else:
        print('False')
print(correct_passwords)

# part 2
correct_passwords = 0
for line in lines:
    match = re.match(r'(?P<pos1>\d+)-(?P<pos2>\d+)\s+(?P<char>\w{1}):\s+(?P<password>\w+)', line)
    print(match.groupdict())
    pos1 = int(match.group('pos1')) - 1
    pos2 = int(match.group('pos2')) - 1
    char = match.group('char')
    password = match.group('password')
    if password[pos1] == char:
        if password[pos2] != char:
            correct_passwords += 1
    elif password[pos2] == char:
        if password[pos1] != char:
            correct_passwords += 1
print(correct_passwords)


