import math

instructions_default = []
nodes = {}

def navigate(next='AAA', instructions=[]):
    if instructions == []:
        instructions = [x for x in instructions_default]
    if next == 'ZZZ':
        return 0
    else:
        return 1 + navigate(nodes[next][instructions[0]], instructions[1:])

if __name__ == '__main__':
    input_file = '2023/day8/input_example2.txt'
    input_file = '2023/day8/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))
    instructions_default = lines[0]

    nodes = {line[:3]:{'L':line[7:10],'R':line[12:15]} for line in lines[2:]}
    # print(nodes)
    # print(nodes['AAA'])

    # print(navigate())
    next = 'AAA'
    steps = 0
    instructions = []
    
    while next != 'ZZZ':
        if instructions == []:
            instructions = [x for x in instructions_default]
        next = nodes[next][instructions[0]]
        steps += 1
        instructions = instructions[1:]
    print(steps)
