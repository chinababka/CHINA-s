from random import shuffle


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        if self.rank == "J":
            return 2
        elif self.rank == "Q":
            return 3
        elif self.rank == "K":
            return 4
        else:
            return "A23456789T".index(self.rank) + 1

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        result = 0
        for i in self.cards:
            result += i.card_value()
        return result

    def __str__(self):
        text = "%s contains:\n" % self.name
        for i in self.cards:
            text += str(i) + " "
        text += "\nHand value: " + str(self.get_value())
        return text


class Deck:
    def __init__(self):
        ranks = "23456789TJQKA"
        suits = "DCHS"
        self.cards = [Card(r, s) for r in ranks for s in suits]
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


def new_game():
    d = Deck()
    player_hand = Hand("Player")
    dealer_hand = Hand("Dealer")
    player_hand.add_card(d.deal_card())
    player_hand.add_card(d.deal_card())
    dealer_hand.add_card(d.deal_card())
    print(dealer_hand)
    print("=" * 20)
    print(player_hand)
    in_game = True
    while player_hand.get_value() < 21:
        x = input("Hit or stand?(h/s)")
        if x == "h":
            player_hand.add_card(d.deal_card())
            print(player_hand)
            if player_hand.get_value() > 21:
                print("You lose")
                in_game = False
        else:
            print("You stand!")
            break
    print("=" * 20)
    if in_game:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(d.deal_card())
            print(dealer_hand)
            if dealer_hand.get_value() > 21:
                print("Dealer bust")
                in_game = False
    if in_game:
        if player_hand.get_value() > dealer_hand.get_value():
            print("You win")
        else:
            print("Dealer win")


new_game()
