import re

class Grab:
    def __init__(self, grab_init_string):
        self.red = 0
        self.blue = 0
        self.green = 0
        for cube in grab_init_string.split(','):
            # print(cube)
            count, color = cube.strip().split(' ')
            match color:
                case 'red': self.red = int(count)
                case 'blue': self.blue = int(count)
                case 'green': self.green = int(count)
    
    def __str__(self) -> str:
        return 'r{}b{}g{} '.format(self.red, self.blue, self.green)
    
    def is_possible(self, red, blue, green):
        if self.red <= red and self.blue <= blue and self.green <= green:
            return True
        else:
            return False

class Game:
    def __init__(self, init_string):
        self.name = init_string.split(':')[0]
        self.number = int(self.name.split(' ')[1])
        self.grabs = [Grab(x) for x in init_string.split(':')[1].split(';')]

    def __str__(self) -> str:
        return self.name + ' : ' + ', '.join([str(x) for x in self.grabs]) + ' -> ' + str(self.is_possible(12,14,13))
    
    def is_possible(self, red, blue, green):
        if len([x for x in self.grabs if not x.is_possible(red, blue, green)]) > 0 :
            return False
        else:
            return True
        
    def find_minimum(self):
        red = max([x.red for x in self.grabs])
        blue = max([x.blue for x in self.grabs])
        green = max([x.green for x in self.grabs])
        return red * blue * green

if __name__ == '__main__':
    # Part 1
    input_file = '2023/day2/input_example.txt'
    input_file = '2023/day2/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))
    # print()
    games = [Game(x) for x in lines]
    print('\n'.join([str(x) for x in games]))

    # print('\n'.join([str(x) for x in games if x.is_possible(12, 14, 13)]))
    count = sum([x.number for x in games if x.is_possible(12, 14, 13)])
    print(count)
    print(sum([x.find_minimum() for x in games]))