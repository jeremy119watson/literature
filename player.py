'''
player.py

Author          : Jeremy Watson
Created on      : 2/21/18
Last modified   : 4/26/18

Description     : Holds the Player class.
'''

from card_deck import Deck, Card
from random import randint
import json, copy

suits = {1 : 'Clubs', 2 : 'Spades', 3 : 'Hearts', 4 : 'Diamonds'}

class Player:
    
    def __init__(self, number, id):
        self.__number = number # player's number in respect to their team
        self.__id = id # unique id
        self.__hand = []
        self.__suits = [[0,0],[0,0],[0,0],[0,0]] # this allow the player to count how many cards they have of each suit, high and low.
        self.__declaration = None # [0,0] [suit, l_h] | this is where the player's current declaration is stored, if any.
    
    # ----------------------------------------------------------------
    
    # Here we sort the player's hand first by suit, then number.
    def sort_hand(self):
        self.__hand.sort(key=lambda x: (x.get_suit_number(), x.get_card_number()))
    
    # ----------------------------------------------------------------

    # return player's number
    def get_number(self):
        return self.__number

    # ----------------------------------------------------------------

    # return player's id
    def get_id(self):
        return self.__id

    # ----------------------------------------------------------------

    # Here a player can recieve a card. 
    def receive_card(self, card):

        if self.has_card(card):
            return

        # be safe and set declaration to none, probably not needed here, so ignore
        self.__declaration = None

        # keep track of what card you recieved, in terms of high/low suit
        suit = card.get_suit_number()
        l_h = card.get_low_or_high()

        suit_counter = self.__suits[suit - 1][l_h] + 1
        self.__suits[suit - 1][l_h] = suit_counter

        # set card declaration if this card completed a suit
        if suit_counter == 6:
            self.__declaration = [suit, l_h]
        
        self.__hand.append(card)
        self.sort_hand()
    
    # ----------------------------------------------------------------

    # Here a player loses a card
    def lose_card(self, card):

        if not self.has_card(card):
            return

        self.__hand.remove(card)
        
        # remove card from suit tracker
        suit = card.get_suit_number()
        l_h = card.get_low_or_high()
        self.__suits[suit-1][l_h] -= 1

    # ----------------------------------------------------------------

    # determine if this player has a certain card
    def has_card(self, card):

        for pcard in self.__hand:
            if pcard == card:
                return True
        return False
    
    # ----------------------------------------------------------------

    # return player info as dictionary, for easy json conversion
    def get_info(self):

        hand = []
        for card in self.__hand:
            hand.append(card.get_card_info())

        return {
                'number' : self.__number,
                'id'     : self.__id,
                'can_declare'   : self.can_declare(),
                'declaration'   : self.__get_declaration_str(),
                'hand'          : hand
        }
    
    # ----------------------------------------------------------------

    # determine if the player can declare a suit at this moment
    def can_declare(self):

        return self.__declaration is not None

    # ----------------------------------------------------------------
    
    # process the player's declaration of a suit, mostly just getting rid of those cards
    def declare(self):

        declaration = copy.copy(self.__declaration)
        hand = copy.copy(self.__hand)
        for card in hand:
            if [card.get_suit_number(), card.get_low_or_high()] == self.__declaration:
                self.lose_card(card)

        return declaration

    # ----------------------------------------------------------------

    # get the string of the declared suit
    def __get_declaration_str (self):
        
        if self.__declaration is None:
            return 'None'
        
        decl = copy.copy(self.__declaration)
        self.__declaration = None
        
        h_or_l = 'low' if decl[1] == 0 else 'high'

        return '%s %s' % (h_or_l, suits[decl[0]])

# --------------------------------------------------------------------
# ---------------- end class Player ----------------------------------
# --------------------------------------------------------------------