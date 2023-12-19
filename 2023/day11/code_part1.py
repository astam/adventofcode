class Position():
    def __init__(self, character, x, y) -> None:
        self.character = character
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return self.character
    
    def shortest_path(self, other):
        # if g1.idx == 3 and g2.idx == 6:
            # print('x:{}, x:{}, diff_x: {}'.format(self.x, other.x, abs(self.x - other.x)))
            # print('y:{}, y:{}, diff_y: {}'.format(self.y, other.y, abs(self.y - other.y)))
        shortest_path = abs(self.y - other.y) + abs(self.x - other.x)
        # print(shortest_path)
        return(shortest_path)
    
class Galaxy(Position):
    def __init__(self, character, x, y, idx) -> None:
        super().__init__(character, x, y)
        self.idx = idx
    
    def __str__(self) -> str:
        return str(self.idx)

def print_universe(universe):
    print('\n'.join([''.join([str(z) for z in y]) for y in universe]))
    print()

if __name__ == '__main__':
    input_file = '2023/day11/input_example.txt'
    input_file = '2023/day11/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print('\n'.join(lines))

    universe_lines = []
    for line in lines:
        universe_lines.append(line)
        if '#' not in line:
            for _ in range(1):
                universe_lines.append(line)
    # print('\n'.join(universe_lines))
    
    universe = []
    x = 0
    for universe_line in universe_lines:
        universe.append([])
        for y in range(len(universe_lines[0])):
            universe[x].append(universe_line[y])
            if '#' not in [line[y] for line in universe_lines]:
                for _ in range(1):
                    universe[x].append(universe_line[y])
        x += 1
    # print_universe(universe)
    # exit()
    galaxies = []
    idx = 1
    for x in range(len(universe)):
        for y in range(len(universe[x])):
            if universe[x][y] == '#':
                galaxy = Galaxy(universe[x][y], x, y, idx)
                universe[x][y] = galaxy
                galaxies.append(galaxy)
                idx += 1
            else:
                universe[x][y] = Position(universe[x][y], x, y)

    # print_universe(universe)

    sh_path = 0
    count = 0
    for g1 in galaxies:
        for g2 in galaxies:
            if g1.x == g2.x and g1.y == g2.y:
                pass
            else:
                count += 1
                # print(g1.x)
                # print(g2.x)
                shortest_path = g1.shortest_path(g2)
                # if g1.idx == 3 and g2.idx == 6:
                #     print(g1.x)
                #     print(g2.y)
                #     print('{}->{}: {}'.format(g1.idx, g2.idx, shortest_path))
                sh_path += shortest_path
    print(sh_path / 2)
    # print(count/2)

    # g2 = Galaxy('#', 6, 1, 5)
    # g1 = Galaxy('#', 11, 5, 7)
    # print(g1.shortest_path(g2))
                
