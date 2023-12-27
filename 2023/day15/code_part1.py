def hash(input: str, current_value=0):
    if input == '':
        return current_value
    current_value += ord(input[0])
    current_value *= 17
    current_value = current_value % 256
    return hash(input[1:], current_value)

if __name__ == '__main__':
    input_file = '2023/day15/input_example.txt'
    input_file = '2023/day15/input.txt'
    sequence = open(input_file).read().split(',')
    print(sum(list(map(hash,sequence))))