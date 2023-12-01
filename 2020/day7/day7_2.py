import re

class Bag:
    def __init__(self, rulestring) -> None:
        s = rulestring.split(' bags contain ')
        self.name = s[0]
        self.count = 0
        rules = [x for x in s[1].split(',') if x != 'no other bags.']
        self.baglist = {}
        self.rulelist = []
        self.countlist = {}
        for rule in rules:
            match = re.match(r'^\s*(?P<count>\d+)\s+(?P<name>\w+\s\w+)', rule)
            self.rulelist.append((int(match.group('count')), match.group('name')))
            self.countlist[match.group('name')] = int(match.group('count'))
        
        if self.name == 'shiny gold':
            print(rulestring)
            print(rules)
            print(self.rulelist)
            print(self.countlist)
        # print(self.rulelist)

    def process_rules(self, bag_dictionary):
        self.baglist = {y:bag_dictionary[y] for x,y in self.rulelist}
        if self.name == 'shiny gold':
            print(self.baglist)

    def print_tree(self, depth=0):
        print('  ' * depth + str(self))
        for bag in self.baglist.values():
            print(str(self.countlist[bag.name]) + ' * ', end='')
            bag.print_tree(depth+1)
    
    def count_bags(self):
        self.count = 0
        # if len(self.baglist) == 0:
        #     return 1
        for bag in self.baglist.values():
            # bag.count_bags()
            self.count += self.countlist[bag.name] + (self.countlist[bag.name] * bag.count_bags())
        return self.count

    def __eq__(self, __value: object) -> bool:
        __value.name == self.name
    
    def __str__(self) -> str:
        return self.name + ' (' + str(len(self.baglist)) + ')' + ' (' + str(self.count) + ')'

if __name__ == '__main__':
    # Part 1
    input_file = '2020/day7/input_example.txt'
    # input_file = '2020/day7/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print(lines)

    bag_dictionary = {}
    # Create bags
    for line in lines:
        bag = Bag(line)
        # print(bag)
        bag_dictionary[bag.name] = bag

    # Link bags
    for bag in bag_dictionary.values():
        bag.process_rules(bag_dictionary)
        # print(bag)
    for bag in bag_dictionary.values():
        bag.count_bags()
        # print(bag)
    print(len(set([x.name for x in bag_dictionary.values()])))
    # Count bags in shiny gold bag
    # bag_dictionary['shiny gold'].count_bags()
    bag_dictionary['shiny gold'].print_tree()
    # print(bag_dictionary['shiny gold'].rulelist)
