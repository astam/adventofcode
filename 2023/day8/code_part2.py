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
    # input_file = '2023/day8/input.txt'
    
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))
    instructions_default = lines[0]

    nodes = {line[:3]:{'L':line[7:10],'R':line[12:15]} for line in lines[2:]}
    # print('\n'.join(sorted(nodes)))
    # exit()
    # print(nodes['AAA'])

    # print(navigate())
    next = [x for x in nodes if x.endswith('A')]
    len_start = len(next)
    steps = 0
    instructions = []
    print(next)
    # next_round = 0
    while len([x for x in next if x.endswith('Z')]) != len_start:
        if instructions == []:
            instructions = [x for x in instructions_default]
            # next_round += 1
            # print(next_round)
        next = [nodes[x][instructions[0]] for x in next]
        # if len([x for x in next if x.endswith('Z')]) > 0:            
        # print(next)
        steps += 1
        if steps % 1000000 == 0:
            print(steps)
        instructions = instructions[1:]
    print(steps)
    print(next)
