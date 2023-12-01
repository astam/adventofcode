from functools import lru_cache

# class Adapter():
#     def __init__(self, joltrate) -> None:
#         self.joltrate = joltrate

@lru_cache(maxsize=None)
def calc(adapterstring: str):
    adapters = [int(x) for x in adapterstring.split(',')]
    if len(adapters) == 1:
        return 1
    parent = int(adapters[0])
    # print(parent)
    rest = adapters[1:]
    ways = 0
    # print(str(rest[0]) + ': ' + str(rest))
    while len(rest) > 0 and rest[0] <= (parent + 3):
        # print(str(rest[0]) + ': ' + str(rest))
        # ways += 1
        ways += calc(",".join(str(x) for x in rest))
        rest = rest[1:]
        # print(rest)
    # print()
    return ways
        
if __name__ == '__main__':
    # Part 1
    input_file = '2020/day10/input_example.txt'
    input_file = '2020/day10/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print(lines)
    intlist = [int(x) for x in lines]
    intlist.append(0)
    intlist.append(max(intlist) + 3)
    sortedlist = sorted(intlist)
    mergedlist = tuple(zip(sortedlist[:-1], sortedlist[1:]))
    # print(mergedlist)
    difflist = [(x, y, y - x) for x,y in mergedlist]
    # print(difflist)
    onelist = [x for x in difflist if x[2] == 1]
    threelist = [x for x in difflist if x[2] == 3]
    print(len(onelist) * len(threelist))
    print()
    print(calc(",".join(str(x) for x in sortedlist)))