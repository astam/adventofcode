import math
from collections import Counter

CARDS = 'AKQJT98765432'
HANDS = ['5', '41', '32', '311', '221', '2111', '11111']

class CardGroup():
    def __init__(self, card, count) -> None:
        self.card = card
        self.count = count

    def __lt__(self, other):
        if self.count < other.count:
            return True
        elif self.count == other.count:
            if CARDS.index(self.card) < CARDS.index(other.card):
                return False
            else:
                return True
        else:
            return False
        
    def __str__(self):
        return self.card * self.count

class Hand():
    def __init__(self, line: str) -> None:
        cards, bid = line.split(' ')
        counts = Counter(cards)
        self.cards = cards
        self.pattern = ''.join(sorted([str(counts[x]) for x in counts], reverse=True))
        self.bid = int(bid)
    
    def __str__(self):
        return self.cards
    
    def __lt__(self, other):
        if HANDS.index(self.pattern) < HANDS.index(other.pattern):
            return True
        elif HANDS.index(self.pattern) == HANDS.index(other.pattern):
            for i in range(5):
                if CARDS.index(self.cards[i]) < CARDS.index(other.cards[i]):
                    return True
                elif CARDS.index(self.cards[i]) > CARDS.index(other.cards[i]):
                    return False
        else:
            return False

if __name__ == '__main__':
    input_file = '2023/day7/input_example2.txt'
    input_file = '2023/day7/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    hands = [Hand(line=line) for line in lines]
    sorted_hands = sorted(hands, reverse=True)
    print(sum([(x.bid * (sorted_hands.index(x) + 1)) for x in sorted_hands]))