import random
class Card(object):
    """A playing card.
    this class will build a single card
    to build a card call Card() and pass in a rank and suit
    card1 = Card(rank = "A", suit = "s"
    """
    RANKS = ["A", "2", "3", "4", "5", "6","7","8","9","10","J", "Q", "K"]
    SUITS = ["♣","♦","♥","♠"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
 #       self.face_up = True

 #   def flip(self):
 #       self.face_up = not self.face_up

    def __str__(self):
        rep = self.rank + self.suit
        return rep
class Hand(object):
    """A hand of playing cards
    also can empty a hand my_hand.clear() print(my_hand)
    and give my_hand.give(my_hand.cards[0], your_hand)print(my_hand) print(your_hand)
    and add cards to a hand for i in range(5): my_hand.add(deck.pop())
    """
    def __init__(self):
        self.cards=[]
    def __str__(self):
        if self.cards:
            rep=""
            for card in self.cards:
                rep +=str(card) + " "
        else:
            rep ="<empty>"
        return rep
    def clear(self):
        self.cards = []
    def add(self,card):
        self.cards.append(card)
    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)
class Deck(Hand):
    """This populates the deck and also passes out hands with unlimited amount of cards"""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Positionable_Card(rank,suit))
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue to deal. Out of Cards")
class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up=False):
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep
    def flip(self):
        self.is_face_up = not self.is_face_up

