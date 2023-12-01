
if __name__ == '__main__':
    # Part 1
    # input_file = '2020/day8/input_example.txt'
    input_file = '2020/day8/input.txt'
    with open(input_file) as f:
        instructions = [line.strip() for line in f.readlines()]
    print(instructions)
    terminate = False
    for i in range(len(instructions)):
        accumulator = 0
        visited = []
        next_hop = 0
        while next_hop not in visited:
            if next_hop + 1 > len(instructions):
                print('terminated')
                print(accumulator)
                terminate = True
                break
            visited.append(next_hop)
            instruction = instructions[next_hop]
            command, parameter = instruction.split(' ')
            print(command)
            print(parameter)
            if next_hop == i:
                match command:
                    case 'nop':
                        command = 'jmp'
                    case 'jmp':
                        command = 'nop'
            match command:
                case 'nop':
                    next_hop += 1
                case 'acc':
                    next_hop += 1
                    accumulator += int(parameter)
                case 'jmp':
                    next_hop += int(parameter)
        if next_hop in visited:
            print('loop detected!')
        if terminate:
            break
        # print(accumulator)
        

