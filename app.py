'''
Author: Jeremy Watson 

Description:  Handles routing. This is the middleman
between the GUI and the game.
'''
from flask import Flask, render_template
from game import Game

app = Flask(__name__)
game = None

# home page
@app.route('/')
def index():
    global game
    game = None
    return render_template('home.html')

# about page
@app.route('/about')
def about():
    return render_template('about.html')

# start game, and get first player info
@app.route('/game/start',methods=['GET'])
def start_g():
    global game
    game = Game()
    return game.get_json()

@app.route('/game/json',methods=['GET'])
def turn_json():
    return game.get_json()

@app.route('/game/inquiry/<int:player>/<int:suit>/<int:number>')
def inquiry(player, suit, number):
    return game.player_inquiry(player, suit, number)

if __name__ == '__main__':
    app.run(debug=True)
