'''
game.py

Author          : Jeremy Watson
Created on      : 2/16/18
Last modified   : 2/24/18

'''

from card_deck import Deck, Card
from player import Player
from random import randint
import json

class Game:

    def __init__(self):

        self.__deck = Deck()
        self.__a_Team = []
        self.__b_Team = []

        # players 1-3 on team A
        # players 4-6 on team B
        self.__current_player_id = 1
        self.__score = [0,0]

        # create players with alternating team
        for i in range(1,4):
            self.__a_Team.append(Player(i, i))
            self.__b_Team.append(Player(i, i + 3))

        # deal cards to players
        i = 0
        for card in self.__deck.get_cards():
            if i < 3:
                self.__a_Team[i].receive_card(card)
            else:
                self.__b_Team[i-3].receive_card(card)
            i = (i + 1) % 6

    # ----------------------------------------------------------------
    # ----------------------------------------------------------------

    # Here we return the requested player object, defaulting to the
    #   current player if none specified
    def get_player(self, player_id=None):

        if player_id is None or player_id not in range(1,7):
            player_id = self.__current_player_id

        if player_id < 4:
            return self.__a_Team[player_id - 1]
        else:
            return self.__b_Team[player_id - 4]
    
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------

    def get_current_player_id(self):
        return self.__current_player_id

    # ----------------------------------------------------------------
    # ----------------------------------------------------------------

    def set_current_player(self, player_id):
        if player_id > 0 and player_id < 7:
            self.__current_player_id = player_id

    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    # If the askee has the card, they lose said card 
    # and the current player gets another turn. 
    # Else, the current player loses there turn and
    # the askee is the new current player.

    def player_inquiry(self, askee_id, suit, number):

        card = Card(suit, number)
        asker = self.get_player()
        askee = self.get_player(askee_id)

        if askee.has_card(card):
            askee.lose_card(card)
            asker.receive_card(card)

            if asker.can_declare():
                self.__current_player_declares()

            return True
        else:
            self.set_current_player(askee_id)
            return False
    
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------

    def __current_player_declares(self):

        player = self.get_player()
        declaration = player.declare()
        self.__score[player.get_team()] += (declaration[1] + 1)

    # ----------------------------------------------------------------
    # ----------------------------------------------------------------

    def get_json(self):

        game_over = (self.__score[0] + self.__score[1]) == 12
        current_team = 0 if self.__current_player_id < 4 else 1

        return json.dumps({
                            'current_player': self.get_player().get_info(),
                            'current_team'  : current_team,
                            'score'         : self.__score,
                            'game_over'     : game_over
        })

# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------

# for debugging
if __name__ == '__main__':
    deck = Deck() 