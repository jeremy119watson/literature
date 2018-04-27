'''
Author          : Jeremy Watson
Created on      : 2/21/18
Last modified   : 4/26/18

Description:  Handles routing. This is the middleman between 
                the zombie GUI and the brains of the game.

              Running this file gets the server going.
'''

from flask import Flask, render_template
from game import Game
import json

app = Flask(__name__)
game = None

# home page
@app.route('/')
def index():
    global game
    game = None
    return render_template('home.html')

# ----------------------------------------------------------------

# start game, and get first player info
@app.route('/game/start',methods=['GET'])
def start_g():
    global game
    game = Game()
    return game.get_json()

# ----------------------------------------------------------------

# get current game info
@app.route('/game/json',methods=['GET'])
def turn_json():
    return game.get_json()

# ----------------------------------------------------------------

# ask for a card
@app.route('/game/inquiry/<int:player>/<int:suit>/<int:number>')
def inquiry(player, suit, number):
    return game.player_inquiry(player, suit, number)

# ----------------------------------------------------------------

# peek at a player's hand
@app.route('/game/peek/<int:player>')
def peek(player):
    return json.dumps(game.get_player(player).get_info())

# ----------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
