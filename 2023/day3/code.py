import math

class Point():
    def __init__(self, x, y , value):
        self.x = x
        self.y = y
        self.value = value
        self.previous = None
        self.next = None
        self.parent = None
        self.number = None
        self.gear_parents = []

    def get_number(self):
        # if not self.is_number():
        #     return ''
        if not self.next:
            return self.value
        else:
            return self.value + self.next.get_number()
        
    def is_number(self):
        return self.value in '0123456789'
    
    def is_empty(self):
        return self.value in '.'
    
    def is_symbol(self):
        return not self.is_number() and not self.is_empty()
    
    def __str__(self) -> str:
        if self.is_number():
            type = 'number'
        elif self.is_symbol():
            type = 'symbol'
        else:
            type = 'empty'
        return '{},{}: {} ({})'.format(self.x, self.y, self.value, type)


if __name__ == '__main__':
    # Part 1
    input_file = '2023/day3/input_example.txt'
    input_file = '2023/day3/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))

    lines.insert(0, '.' * len(lines[0]))
    lines.append('.' * len(lines[0]))
    lines = ['.{}.'.format(x) for x in lines]
    print('\n'.join(lines))
    points=[]

    for x in range(len(lines)):
        # print(x, end='')
        previous = None
        # points.append([])
        for y in range(len(lines[x])):
            # print(y, end='')
            value = lines[x][y]
            point = Point(x, y, value)
            if previous:
                if previous.is_number():
                    if point.is_number():
                        previous.next = point
                        point.previous = previous
                        point.parent = previous.parent
                else:
                    if point.is_number():
                        point.parent = point
            else:
                if point.is_number():
                    point.parent = point
            points.append(point)
            previous = point
            # if previous and value in '0123456789' and previous.value in '0123456789':
            #     previous.next = point
            #     point.previous = previous
            #     point.parent = previous.parent
            # if not previous and value in '0123456789':
            #     point.parent = point
            # if previous and value not in '0123456789' and previous.value in '0123456789':
            #     previous.number = previous.parent.calculate_number()
        # print()
    parents = []
    for point in points:
        if point.is_number():
            for x in range(point.x - 1, point.x + 2):
                for y in range(point.y - 1, point.y + 2):
                    for p in points:
                        if point != p and p.x == x and p.y == y and p.is_symbol():
                            parents.append(point.parent)
                            if p.value == '*':
                                p.gear_parents.append(point.parent)
                                

    unique_parents = list(set(parents))
    numbers = [x.get_number() for x in unique_parents]
    print(numbers)
    print(sum([int(x) for x in numbers]))

    gears_ratios = 0
    for point in points:
        if point.value == '*':
            unique_parents = list(set(point.gear_parents))
            if len(unique_parents) == 2:
                numbers = [x.get_number() for x in unique_parents]
                # print(numbers)
                gears_ratios += math.prod([int(x) for x in numbers])
    print(gears_ratios)