import math
from collections import Counter

CARDS = 'AKQT98765432J'
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
    def __init__(self, cards: str, bid=0, highest_possible_hand=None) -> None:
        if highest_possible_hand:
            counts = Counter(highest_possible_hand)
        else:
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


def get_possibilities(cards):
    match cards.count('J'):
        case 0:
            return cards
        case _:
            possibilities = []
            joker_index = cards.index('J')
            for card in [x for x in CARDS if x != 'J']:
                possibilities.append(Hand(get_possibilities(cards[:joker_index] + card + cards[joker_index+1:])))
            return sorted(possibilities)[0].cards

if __name__ == '__main__':
    input_file = '2023/day7/input_example.txt'
    input_file = '2023/day7/input.txt'
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    hands = []
    for line in lines:
        cards, bid = line.split(' ')
        highest_possible_hand = get_possibilities(cards=cards)
        hands.append(Hand(cards=cards, bid=bid, highest_possible_hand=highest_possible_hand))
    sorted_hands = sorted(hands, reverse=True)
    print(sum([(x.bid * (sorted_hands.index(x) + 1)) for x in sorted_hands]))