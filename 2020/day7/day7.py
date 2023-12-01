import re

class Bag:
    def __init__(self, rulestring) -> None:
        s = rulestring.split(' bags contain ')
        self.name = s[0]
        rules = [x for x in s[1].split(',') if x != 'no other bags.']
        self.baglist = {}
        self.rulelist = []
        for rule in rules:
            match = re.match(r'^\s*(?P<count>\d+)\s+(?P<name>\w+\s\w+)', rule)
            self.rulelist.append(match.group('name'))

    def process_rules(self, bag_dictionary):
        self.baglist = {x:bag_dictionary[x] for x in self.rulelist}

    def has_bag(self, bag):
        if bag in self.rulelist:
            return True
        else:
            if len(self.baglist) > 0:
                for subbag in self.baglist.values():
                    if subbag.has_bag(bag):
                        return True
            else:
                return False
        return False

    # def add_bag(self, parent_bag, child_bag):
    #     if parent_bag == self:
    #         self.bags_inside.append(child_bag)
    #     else:
    #         for bag in self.bags_inside:
    #             bag.add_bag(parent_bag, child_bag)

    def __eq__(self, __value: object) -> bool:
        __value.name == self.name
    
    def __str__(self) -> str:
        return self.name + ' (' + str(len(self.baglist)) + ')'

if __name__ == '__main__':
    # Part 1
    input_file = '2020/day7/input_example.txt'
    input_file = '2020/day7/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    # print(lines)

    bag_dictionary = {}
    # Create bags
    for line in lines:
        bag = Bag(line)
        bag_dictionary[bag.name] = bag

    # Link bags
    for bag in bag_dictionary.values():
        bag.process_rules(bag_dictionary)
        # print(bag)

    # Find shiny gold bag
    has_bag_count = 0
    for bag in bag_dictionary.values():
        # print(bag)
        if bag.has_bag('shiny gold'):
            has_bag_count += 1
    print(has_bag_count)

# light_red
#     bright_white
#         shiny_gold
#             dark_olive
#                 faded_blue
#                 dotted_black
#             vibrant_plum
#                 faded_blue
#                 dotted_black
#     muted_yellow
#         shiny_gold
#             dark_olive
#                 faded_blue
#                 dotted_black
#             vibrant_plum
#                 faded_blue
#                 dotted_black
#         faded_blue