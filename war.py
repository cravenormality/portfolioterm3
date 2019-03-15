#Michael Freeman, Cameron Murphy, Nicholaus Whites, Jessica Weinburger
#2/19
#War
#Python 4th

import cards, games, time

class W_Card(cards.Card):

    @property
    def value(self):
        """This sets the value of the cards. It takes the positional value of a rank and adds one to it.
            for example, number 2 is in index 1, and i+1 is 1. A K is in index 12, 12 + 1 is 13."""
        if self.is_face_up:
            v = W_Card.RANKS.index(self.rank) + 1
        else:
            v  = None
        return v

class W_Deck(cards.Deck):

    """This is the deck the cards are shuffled from. Cards are matched with their rank and suit, and added to the deck.
    """
    def populate(self):
        for suit in W_Card.SUITS:
            for rank in W_Card.RANKS:
                self.cards.append(W_Card(rank, suit))


class W_Hand(cards.Hand):

    """This defines a name and properties of a player and their cards."""

    def __init__(self, name):
        super(W_Hand, self).__init__()
        self.name = name



class W_Player(W_Hand):
    """ A War Player. """

    def play(self,hand):
        """This tells the hands which card to play."""
        top_card = self.cards[0]
        self.give(top_card,hand)

    def lose(self):
        """Sets the losing message for the hand losing the round."""
        print(self.name, "loses.")
        self.cards.clear()

    def win(self):
        """Sets the wining message for the hand winning the round."""
        print(self.name, "wins.")

class Pot(W_Hand):
    """Where the wild cards are."""
    def __init__(self, players):
        super(W_Hand, self).__init__()
        self.players = players

    @property
    def check_winner(self):
        """Pot is its own hand. It checks the value of the two cards and sees which is greater.
            After deciding the winner it returns a number to be compared against the W_Game function."""
        if self.cards[0].value > self.cards[1].value:
            winner = 0
        elif self.cards[0].value < self.cards[1].value:
            winner = 1
        else:
            winner = None
        return winner
    @property
    def check_win_war(self):
        """This function checks the winner of the war. p1card and p2card are variables to determine which cards of the
        entire
            war pile represent who and compares them. Then it runs similar to the check_winner function above."""
        p1card = int(len(self.cards))-2
        p2card = int(len(self.cards))-1
        if self.cards[p1card].value > self.cards[p2card].value:
            winner = 0
        elif self.cards[p1card].value < self.cards[p2card].value:
            winner = 1
        else:
            winner = None
        return winner


    def give_cards(self, winner):
        """The function that tells the pot what to do with the hands."""
        for i in range(len(self.cards)):
            self.give(self.cards[0],self.players[winner])


class W_Game(object):
    """ A War Game. """

    def __init__(self, names):
        """Initializes the names, sets them to a hand, deals the cards and shuffles them."""
        self.players = []
        for name in names:
            player = W_Player(name)
            self.players.append(player)

        self.pot = Pot(self.players)


        self.deck = W_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def game_over(self):
        """Defines what happens when the game is over. This prints the final hand values of both players."""
        for player in self.players:
            x = len(player.cards)
            print(player.name,x)
            if x <= 0:
                return True
        return False

    def play(self):
        game_over = None
        self.deck.deal(self.players, per_hand = 26)
        """As long as the game is not over, play these."""
        while  not game_over:
            """Try to work with cards, if either hand is empty or cannot be interacted with, head for except."""
            try:
                for player in self.players:
                    """Prints the hand totals of each player after a draw."""
                    player.play(self.pot)
                    x = len(player.cards)
                    print(player.name,x)

                """The winning message."""
                winner = self.pot.check_winner
                print(self.players[0].name+" ",self.pot,self.players[1].name)

                """Defines who wins and where the cards go."""
                if winner == 0:
                    print(self.players[0].name,"Wins") 
                elif winner == 1:
                    print(self.players[1].name,"Wins")
                   
                    
                else:
                    """If neither player wins, the computer checks against the player hand length. If player has enough
                        cards to participate in the war, they get to pool their cards in. Then, displays the winner and 
                        loser."""
                    p1len = len(self.players[0].cards)
                    p2len = len(self.players[1].cards)
                    if p1len >= 4 and p2len >=4:    
                        print ("\nWAR")
                        for i in range (4):
                            for player in self.players:
                                player.play(self.pot)
                        print(self.pot)
                        
                        winner = self.pot.check_win_war
                        if winner == 0:
                            print(self.players[0].name,"Wins")
                            
                        elif winner == 1:
                            print(self.players[1].name,"Wins")
                    else:
                        if p1len <= 4:
                            self.players[0].lose()
                        else:
                            self.players[1].lose()
                                        
                self.pot.give_cards(winner)
                input("\nPress enter to draw.")   
            except:
                game_over = self.game_over()


def main():
    while True:
        """Asks for player name. To avoid blank entries, checks to see if name is alpha numerical."""
        p1 = input("\nEnter Player 1: ")
        while p1.isalnum():
            p2 = input("\nEnter Player 2: ")
            if p2.isalnum():
                names = []
                names.append(p1)
                names.append(p2)
                game = W_Game(names)
                game.play()
                print("\nThe War has been Won!")
                time.sleep(10)
                input("\nPress Enter to Quit.")
                return False
            else:
                print("\nInvalid. Try again!")
                    
        else:
            print("\nInvalid. Try again!")
    

main()
