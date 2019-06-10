import random

class Card(object):
    """Represents a standard playing card.
    attributes: suit, rank
    """
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
        '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0,rank=2):
        self.suit = suit
        self.rank = rank

    # Print the card
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
            Card.suit_names[self.suit])

    # If Self is > Other, return True
    def __gt__(self, other):
        # check the suits
        if self.suit > other.suit: return True
        if self.suit < other.suit: return False
        # suits are the same... check ranks
        if self.rank > other.rank: return True
        if self.rank < other.rank: return False
        # ranks are the same... it's a tie
        return False


    def __lt__(self, other):
        # check the suits
        if self.suit > other.suit: return False
        if self.suit < other.suit: return True
        # suits are the same... check ranks
        if self.rank > other.rank: return False
        if self.rank < other.rank: return True
        # ranks are the same... it's a tie
        return False

    def __eq__(self, other):
        # check the suits
        if self.suit > other.suit: return False
        if self.suit < other.suit: return False
        # suits are the same... check ranks
        if self.rank > other.rank: return False
        if self.rank < other.rank: return False
        # ranks are the same... it's a tie
        return True



class Deck(object):
    """Represents a deck of cards
    attributes: cards
    """

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    # Prints the deck
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    # Returns bottom card of deck
    def pop_card(self):
        return self.cards.pop()

    # Add a card to the deck
    def add_card(self, card):
        self.cards.append(card)

    # Shuffle the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # Sort the deck
    def sort(self):
        self.cards.sort()

    # Move num(amount) cards from Deck -> Hand or vice versa :)
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

class Hand(Deck):
    """
    Represents a hand of playing cards
    attributes: cards (list), label (str)
    """
    # An init that overides the Deck init
    def __init__(self, label=''):
        self.cards = []
        self.lebel = label


deck = Deck()

hand = Hand('new hand')
hand.add_card(deck.pop_card()) # Drawing a card
print(hand)
