'''
card_deck.py

Author          : Jeremy Watson
Created on      : 2/21/18
Last modified   : 4/26/18

Description     : Holds the Deck and Card classes.
'''

from random import shuffle
import json

names = {2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five', 6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine', 10 : 'Ten', 11 : 'Jack', 12 : 'Queen', 13 : 'King', 14: 'Ace'}

suits = {1 : 'Clubs', 2 : 'Spades', 3 : 'Hearts', 4 : 'Diamonds'}

high_low_threshold = 9

class Deck:
    def __init__(self):

        self.__cards = []

        for i in range(3,15):
            self.__cards.append(Card(1, i))
            self.__cards.append(Card(2, i))
            self.__cards.append(Card(3, i))
            self.__cards.append(Card(4, i))

        shuffle(self.__cards)

    # ----------------------------------------------------------------

    # return the cards
    def get_cards(self):
        return self.__cards

# --------------------------------------------------------------------
# ---------------- end class Deck-------------------------------------
# --------------------------------------------------------------------

class Card:
    def __init__(self, suit_number, card_number):

        self.__suit_number = suit_number
        self.__card_number = card_number
        self.__id = (4 * card_number) - (4 - suit_number)
        self.__low_or_high = 0 if card_number < high_low_threshold else 1

    # ----------------------------------------------------------------

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__
    
    # ----------------------------------------------------------------

    # return the suit number
    def get_suit_number(self):
        return self.__suit_number

    # ----------------------------------------------------------------

    # return the card number
    def get_card_number(self):
        return self.__card_number

    # ----------------------------------------------------------------

    # return card's unique id (for easily finding the card's image)
    def get_id(self):
        return self.__id

    # ----------------------------------------------------------------

    # return wether card is low or high
    def get_low_or_high(self):
        return self.__low_or_high
    
    # ----------------------------------------------------------------

    # return card name
    def get_verbose_name(self):
        return '%s of %s' % (names[self.__card_number], suits[self.__suit_number])

    # ----------------------------------------------------------------

    # return the name of the card's image
    def get_img_name(self):
        return '%d.png' % self.__id
    
    # ----------------------------------------------------------------

    # return card info in dictionary for nice json conversion
    def get_card_info(self):
        return { 
            'number': self.__card_number,
            'suit': self.__suit_number,
            'imgName': self.get_img_name() ,
            'name' : self.get_verbose_name()
        }

# --------------------------------------------------------------------
# ---------------- end class Card ------------------------------------
# --------------------------------------------------------------------