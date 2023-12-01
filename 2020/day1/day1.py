input_file = '2020/day1/input_example.txt'
input_file = '2020/day1/input.txt'
with open(input_file) as f:
    lines = [int(line.strip()) for line in f.readlines()]
print(lines)
for left in lines:
    for right in lines:
        if left + right == 2020:
            print(left * right)
for left in lines:
    for mid in lines:
        for right in lines:
            if left + mid + right == 2020:
                print(left * mid * right)