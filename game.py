'''
game.py

Author          : Jeremy Watson
Created on      : 2/16/18
Last modified   : 4/26/18

Description     : Holds class Game. Class game holds all of the game information,
                    facilitates interactions between players, and serves up game info.

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

        # create players
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

    # return the id of the current player
    def get_current_player_id(self):
        return self.__current_player_id

    # ----------------------------------------------------------------

    # set a new current player
    def set_current_player(self, player_id):
        if player_id > 0 and player_id < 7:
            self.__current_player_id = player_id

    # ----------------------------------------------------------------
    
    # This facilitates the current player asking for a card.
    # If the askee has the card, they lose said card 
    # and the current player gets another turn. 
    # Else, the current player loses there turn and
    # the askee is the new current player.
    def player_inquiry(self, askee_id, suit, number):

        card = Card(suit, number)
        asker = self.get_player()
        askee = self.get_player(askee_id)
        message = ""
        success = True

        if askee.has_card(card):
            askee.lose_card(card)
            asker.receive_card(card)

            # if the player has a completed suit, said player declares
            if asker.can_declare():
                self.__current_player_declares()

            message = 'You recieved the %s' % (card.get_verbose_name())
            
        else:
            self.set_current_player(askee_id)
            message = 'This player does not have the %s. You lose your turn.' % (card.get_verbose_name())
        
        # return message indicates success or failure
        return json.dumps({'success': success, 'message': message})
    
    # ----------------------------------------------------------------

    # the current player declares a suit
    def __current_player_declares(self):

        player = self.get_player()
        declaration = player.declare()
        self.__score[0 if self.__current_player_id < 4 else 1] += (declaration[1] + 1)

    # ----------------------------------------------------------------

    # return the status of the game as json
    def get_json(self):

        game_over = (self.__score[0] + self.__score[1]) == 12
        current_team = 0 if self.__current_player_id < 4 else 1

        return json.dumps({
                            'current_player': self.get_player().get_info(),
                            'current_team'  : current_team,
                            'score'         : self.__score,
                            'game_over'     : game_over
        })

# --------------------------------------------------------------------
# ---------------- end class Game ------------------------------------
# --------------------------------------------------------------------