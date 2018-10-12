# literature

(orignally hosted on Github)

This is an implementation of the card game, Literature. This was a project for my Object-Oriented Design class in college, the focus being on the object-oriented game logic. As such, the implementation is not actually designed for six different players to play the game, instead it is designed for one person to demo the game.

Looking back on it now, I would better redesign the portion written in Python to be easier to understand -- it's a bit clunky as is. I should've used git as intended but instead I used it to backup my code.

The following description was required for grading.
___

Literature Project
___
I used **Python** for my **object-oriented** language. These files are found in the "Literature" directory.
*  "app.py" starts up the server, getting everything going. The gui is displayed on "localhost:5000".
___
 I created the gui using HTML, CSS, and JS.
* The HTML files are found under "templates" and "templates/includes". These files are rendered as one by the Flask framework I'm using as a server.
* The CSS files are found under "static/css". I only wrote "style.css", not "w3.css", which is a free CSS library.
*  The JS files are found under "static/js". I only wrote "game.js". I used AngularJS is a way it was probably not meant to be used, but it works so whatever.
___
Since the gui isn't **object-oriented**, and is separate from the game logic, it is not commented heavily.
___
