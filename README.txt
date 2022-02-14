=====================

_shifted

=====================

Created by Jonathan Ward

======= ABOUT THE GAME =======

_shifted is a terminal-based game that challenges the user to determine the placement of four dishes at a round table based on clues.

======= GAMEPLAY =======

This is a one-player game. 

The player is given an unordered list of the names of four guests seated at a round table. The player is also given a menu that lists the six dishes the restaurant is serving. Finally, the player is given several clues related to the guests and their dishes.

The player can assume each guest chose one unique dish from the menu. Consequently, two of the menu items are not present at the table.

On each turn, the player guesses the order of dishes (starting at place 1).

======= CLUES =======

The clues given at the beginning of each game tell the user information about the dishes and guests. Below are example clues for guests Beau (place 1, pasta), Anna (place 2, burrito), Trey (place 3, soup) and Pasha (place 4, burger):

- Beau is sitting at seat 1.
- Pasha is not sitting next to Anna.
- Trey ordered soup.
- One person next to Beau does not like burgers or fish.
- Pasha does not like burritos or pasta.

======= GUESSING =======

The player will type the order of dishes starting in place 1. If they guess correctly, they win the game! If the guess is not correct, they will be told how many dishes, if any, are in the correct place.

A guess can look like any of the following:

burrito soup burger pasta
burrito,soup,burger,pasta
burrito, soup, burger, pasta

Example response: 0 dishes are in the correct place.

The player will not know if the dish belongs on the table unless it is in the correct place.

======= SCORING =======

Score will be based on the number of turns it takes the player to correctly guess the placement of dishes.

======= HOW IT WORKS IN PYTHON =======

_shifted will rely on the input() function for gameplay. There will be two classes: Players and Guests. The Player class will include the player's name, game status and score information. The Guest class will include attributes of name, dish and place. When each game is initialized, Guest names, menu items, Guest places and clues are shuffled. 