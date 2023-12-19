import itertools
import operator

def get_diff(history):
    if len(history) != len([x for x in history if x == 0]):
        return history[0] - get_diff(list(map(operator.sub, history[1:], history[:-1])))
    else:
        return 0

if __name__ == '__main__':
    input_file = '2023/day9/input_example.txt'
    input_file = '2023/day9/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    
    total = 0
    for line in lines:
        history = [int(x) for x in  line.split(' ')]
        total += get_diff(history)
    print(total)