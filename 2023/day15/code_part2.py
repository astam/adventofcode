def hash(input: str, current_value=0):
    if input == '':
        return current_value
    current_value += ord(input[0])
    current_value *= 17
    current_value = current_value % 256
    return hash(input[1:], current_value)

if __name__ == '__main__':
    input_file = '2023/day15/input_example.txt'
    input_file     = '2023/day15/input.txt'
    sequence = open(input_file).read().split(',')
    # print(sum(list(map(hash,sequence))))
    # print(list(map(hash,sequence)))
    boxes = {}
    for operation in sequence:
        print(operation)
        label = operation.replace('=',' ').replace('-', ' ').split()[0]
        box = hash(label)
        if '-' in operation:
            if box in boxes:
                boxes[box] = [x for x in boxes[box] if x[0] != label]
                if len(boxes[box]) == 0:
                    del boxes[box]
        else:
            if box not in boxes:
                boxes[box] = []
            value = int(operation.split('=')[1])
            
            if label in [x[0] for x in boxes[box]]:
                new = []
                for lens in boxes[box]:
                    if label == lens[0]:
                        new.append((label, value))
                    else:
                        new.append(lens)
                boxes[box] = new
            else:
                boxes[box].append((label, value))
            # print(label)
        print(boxes)
        print()
    power = 0
    for number, box in boxes.items():
        print(number, box)
        for i in range(len(box)):
            power += (number + 1) * (i + 1) * box[i][1]
    print(power)



    
# rn: 1 (box 0) * 1 (first slot) * 1 (focal length) = 1
# cm: 1 (box 0) * 2 (second slot) * 2 (focal length) = 4
# ot: 4 (box 3) * 1 (first slot) * 7 (focal length) = 28
# ab: 4 (box 3) * 2 (second slot) * 5 (focal length) = 40
# pc: 4 (box 3) * 3 (third slot) * 6 (focal length) = 72

# So, the above example ends up with a total focusing power of 145.