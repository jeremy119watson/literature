from card_deck import Deck, Card
from random import randint
import json
import copy

suits = {1 : 'Clubs', 2 : 'Spades', 3 : 'Hearts', 4 : 'Diamonds'}

class Player:
    
    def __init__(self, number, id):
        self.__number = number
        self.__id = id
        self.__hand = []
        self.__suits = [[0,0],[0,0],[0,0],[0,0]]
        self.__declaration = None # [0,0] [suit, l_h]
    
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    # Here we sort the player's hand first by suit, then number.
    # Currently, 'Ace' with number 1, ranks highest. This is the
    # correct behavior, based on the game rules we are implementing.
    def sort_hand(self):
        self.__hand.sort(key=lambda x: (x.get_suit_number(), x.get_card_number()))
    
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------

    def get_number(self):
        return self.__number

    # ----------------------------------------------------------------
    # ----------------------------------------------------------------

    def get_id(self):
        return self.__id

    # ----------------------------------------------------------------
    # ----------------------------------------------------------------

    # Here a player can recieve a card. 
    def receive_card(self, card):

        if self.has_card(card):
            return

        self.__declaration = None

        suit = card.get_suit_number()
        l_h = card.get_low_or_high()

        suit_counter = self.__suits[suit - 1][l_h] + 1
        self.__suits[suit - 1][l_h] = suit_counter

        if suit_counter == 6:
            self.__declaration = [suit, l_h]
        
        self.__hand.append(card)
        self.sort_hand()
    
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------

    def lose_card(self, card):

        if not self.has_card(card):
            return

        self.__hand.remove(card)
        
        suit = card.get_suit_number()
        l_h = card.get_low_or_high()
        self.__suits[suit-1][l_h] -= 1

    # ----------------------------------------------------------------
    # ----------------------------------------------------------------

    def has_card(self, card):

        # print(card.get_card_info())
        # print(card in self.__hand)

        for pcard in self.__hand:
            if pcard == card:
                return True
        return False
    
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------

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
    # ----------------------------------------------------------------

    def can_declare(self):

        return self.__declaration is not None

    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def declare(self):

        declaration = copy.copy(self.__declaration)
        
        for card in self.__hand:
            if [card.get_suit_number(), card.get_low_or_high()] == self.__declaration:
                self.lose_card(card)

        return declaration

    # ----------------------------------------------------------------
    # ----------------------------------------------------------------

    def __get_declaration_str (self):
        
        if self.__declaration is None:
            return 'None'
        
        h_or_l = 'low' if self.__declaration[1] == 0 else 'high'

        return '%s %s' % (h_or_l, suits[self.__declaration[0]])