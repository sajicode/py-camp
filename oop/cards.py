from random import shuffle

class Card():
  def __init__(self, value, suit):
    self.value = value
    self.suit = suit

  def __repr__(self):
    return "{} of {}".format(self.value, self.suit)

c = Card("Ace", "Hearts")

# print(c.suit)
# print(c)

class Deck:
  def __init__(self):
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    #* list compehension below substitutes for a nested loop to return  every possible instance of suits and values
    self.cards = [Card(value, suit) for suit in suits for value in values]

  def __repr__(self):
    return f"Deck of {self.count()} cards"

  def __iter__(self):
    return iter(self.cards)

  def count(self):
    return len(self.cards)

  def _deal(self, num):
    count = self.count()
    actual = min([count, num])
    if count == 0:
      raise ValueError("All cards have been dealt!")
    #* remove last num of cards
    self.cards[-actual:]
    #*  update cards list
    self.cards  = self.cards[:-actual]
    return self.cards

  def deal_card(self):
    return self._deal(1)[0]

  def deal_hand(self, hand_size):
    return self._deal(hand_size)

  def shuffle(self):
    if self.count() < 52:
      raise ValueError("Only full decks can be shuffled")
    shuffle(self.cards)
    return self

d1 =  Deck()
d1.shuffle()

print(d1.cards)
# print(d1.deal_card())
# print(d1._deal(52))