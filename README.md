<div align="center">
  <h1>:pizza: _shifted :pizza:</h1>
</div>
<br>

## What is _shifted?

_shifted is a terminal-based game that challenges the user to place four dishes at a round table based on clues, as well as trial and error.

## How does it work?

### Gameplay

_shifted is a one-player game. 

The player is given an unordered list of the names of four guests seated at a round table. The player is also given a menu that lists the six dishes the restaurant is serving that night. Finally, the player is given several clues related to where the guests are sitting and what dishes they are eating.

The player can assume each guest chose one unique dish from the menu. Consequently, two of the six menu items are not present at the table.

On each turn, the player guesses the order of dishes (starting at place 1). The player has eight guesses.

### Clues

The clues given at the beginning of each game tell the user information about the dishes and guests. Below are example clues for guests Beau (place 1, pasta), Anna (place 2, burrito), Trey (place 3, soup) and Pasha (place 4, burger):

- Beau is sitting at seat 1.
- Pasha is not sitting next to Anna.
- Trey ordered soup.
- One person ordered a burger.
- Pasha does not like burritos or pasta.

### Guessing

The player will type the order of dishes starting in place 1. If they guess correctly, they win the game! If the guess is not correct, they will be told how many dishes, if any, are in the correct place.

A guess can look like any of the following:

burrito soup burger pasta
burrito,soup,burger,pasta
burrito, soup, burger, pasta

Example response: 0 dishes placed correctly.

The player will not know if the dish belongs on the table unless it is in the correct place.

### Scoring

The player's score will be based on the number of turns it takes the player to correctly guess the placement of dishes.

### Python Features

_shifted relies on the input() function for gameplay. Two classes are used: Players and Guests. The Player class includes the player's name, game status and score information. The Guest class includes attributes of name, dish, place, neighbors, tablemates, opposite and does_not_like (which comprises the foods the player didn’t order).

When each game is initialized, Guest names, menu items, Guest places and clues are shuffled. Positional relationships are also established.

The objects will reference other objects, so if Anna is Jamal’s neighbor, the Jamal object (guestOne, for example) will reference Anna’s attributes when guestOne.neighbors or guestOne.tablemates are accessed.

The game will print out the same kinds of clues every time; however, because the spatial relationships are always changing, the clues vary in their helpfulness. This creates different game situations with minimal and maximal values of clue helpfulness.

## Additional Notes

### Web Version

Inspired by Wordle and its many popular derivatives—-and after learning how to use event listeners in Codecademy’s web development course-—I decided to create <a href="https://jonathanward.github.io/_shifted-web-version/">a web-based version of _shifted.</a>

### Inspirations

While seeking to strengthen my problem-solving and analytical skills, I’ve been on the hunt for fun logic puzzles, which can play an important role in exercising our critical thinking skills. I was inspired to develop this game based on my experiences with the following:

- Einstein’s Logic Puzzle
- Logical Journey of the Zoombinis (Pizza Pass level)
- Mastermind
