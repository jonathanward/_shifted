# ======= GAME SETUP =======

import random

# Guest names (four will be chosen per game) 
names = ["Anna", "Ari", "Beau", "Chris", "Damon", "Gabi", "Hannah", "Jamal", "Jill", "Javier", "Kai", "Kayla", "Kim", "Luke", "Malik", "Nina", "Pasha", "Talia", "Trey", "Wesley"]

# List of dishes (six will appear on the menu, and one unique dish will be assigned to each of the four guests)
dishes = ["pizza", "burger", "salad", "pasta", "soup", "sandwich", "burrito", "fish"]

# Person class will be used for four guest objects
class Guest:
    def __init__(self, name, dish, place):
        self.name = name
        self.dish = dish
        self.place = place
    
    def __repr__(self):
        return self.dish + " (" + self.name + ", place " + str(self.place) + ")"

# Select random item from a list, remove it from the list and return it
def select_item(my_list):
    item = random.choice(my_list)
    my_list.remove(item)
    return item

# Create four guests
guest_one = Guest(select_item(names), select_item(dishes), 1)
guest_two = Guest(select_item(names), select_item(dishes), 2)
guest_three = Guest(select_item(names), select_item(dishes), 3)
guest_four = Guest(select_item(names), select_item(dishes), 4)

# Create list with four guests
table = [guest_one, guest_two, guest_three, guest_four]

# Create separate alphabetized list of four guests
def get_name(guest):
    return guest.name
alpha_table = sorted(table, key=get_name)

# Create menu with six dishes, including four that guests have chosen. Then alphabetize menu
menu = [guest_one.dish, guest_two.dish, guest_three.dish, guest_four.dish, select_item(dishes), select_item(dishes)]
menu.sort()

# Establish positional relationships with other guests
for guest in table:
    guest.right_neighbor = table[guest.place - 2]
    if (guest.place < 4):
        guest.left_neighbor = table[guest.place]
    elif (guest.place == 4):
        guest.left_neighbor = table[0]
    guest.neighbors = [guest.right_neighbor, guest.left_neighbor]
    guest.opposite = table[guest.place - 3]
    guest.tablemates = [guest.right_neighbor, guest.opposite, guest.left_neighbor]
    guest.does_not_like = [dish for dish in menu if dish != guest.dish]

# Initialize Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turns_left = 8
        self.is_playing = True

    def __repr__(self):
        statement = "name: " + self.name + ", score: " + str(self.score) + ", turns left: " + str(self.turns_left) + ", is playing: " + str(self.is_playing)
        return statement

# ======= GAME FUNCTIONS ======

# Print out alphabetized list of guests and menu
def print_info():
    print("\nGuests (NOT listed in seated order):")
    [print("- " + guest.name) for guest in alpha_table]

    print("\nMenu:")
    [print("- " + dish) for dish in menu]

# Create four clues to help--and sometimes distract--the player
clue_a_person = random.choice(alpha_table)
clue_b_person = select_item(clue_a_person.tablemates)
clue_c_person = select_item(clue_b_person.tablemates)
clue_d_person = select_item(clue_c_person.tablemates)

def create_clue_a():
    clue = clue_a_person.name + " is not sitting next to " + clue_a_person.opposite.name + "."
    return clue

def create_clue_b():
    if (clue_b_person.dish == "soup" or clue_b_person.dish == "fish" or clue_b_person.dish == "pizza" or clue_b_person.dish == "pasta"):
        clue = clue_b_person.name + " ordered " + clue_b_person.dish + "."
    else:
        clue = clue_b_person.name + " ordered a " + clue_b_person.dish + "."
    return clue

def check_food_plurality(food):
    if (food == "burger" or food == "burrito"):
        return food + "s"
    elif (food == "sandwich"):
        return food + "es"
    else:
        return food

def create_clue_c():
    undesirable_food_one = select_item(clue_c_person.does_not_like)
    undesirable_food_two = select_item(clue_c_person.does_not_like)
    clue = clue_c_person.name + " does not like " + check_food_plurality(undesirable_food_one) + " or " + check_food_plurality(undesirable_food_two) + "."
    return clue

def create_clue_d():
    undesirable_food_one = select_item(clue_d_person.does_not_like)
    undesirable_food_two = select_item(clue_d_person.does_not_like)
    clue = "One person next to " + clue_d_person.name + " does not like " + check_food_plurality(undesirable_food_one) + " or " + check_food_plurality(undesirable_food_two) + "."
    return clue

# Shuffle clues so they don't always appear in the same order
official_clues = [create_clue_a(), create_clue_b(), create_clue_c(), create_clue_d()]
random.shuffle(official_clues)

def print_clues():
    for clue in official_clues:
        print("- " + clue)

# Check whether a word should be plural based on if a condition is true. If it is, add an s to the word. If not, return the word
def check_plurality(word, condition):
    if (condition):
        return word + "s"
    else:
        return word

# Check answer after each submission. If it is correct, end the game and give the score. If not, reduce the number of turns and tell the player how many dishes, if any, were placed in the correct spot
def check_answer(answer):
    
    # Clean answer if it contains commas
    cleaned_answer = answer.replace(",", " ")

    # Remove extra spaces
    answer_with_single_spaces = " ".join(cleaned_answer.split())

    # Split answer into a list of words
    answer_split = answer_with_single_spaces.split(" ")

    # If the list doesn't contain four words, return an error message
    if (len(answer_split) != 4):
        return "\n=====\n\nERROR: Please enter four dishes separated by one space.\n\nExample: burger salad fish burrito\n\n=====\n"

    # If the list doesn't contain four valid words, return an error message
    for item in answer_split:
        if item not in menu:
            return "\n=====\n\nERROR: Please enter four valid dishes from the menu separated by one space.\n\nExample: burger salad fish burrito\n\n=====\n"

    # Tally the number of correctly placed dishes. Even if a dish belongs at the table but is not placed correctly, it will not show up in the tally
    answer_count = 0
    for i in range(4):
        if answer_split[i] == table[i].dish:
            answer_count += 1

    # If the player guesses the correct order, end the game and show the score
    if answer_count == 4:
        player_one.is_playing = False
        player_one.turns_left -= 1
        player_one.score = player_one.turns_left * 100 + 100
        return "\nYou win! You solved the problem in " + str(8 - player_one.turns_left) + " " + check_plurality("turn", ((8 - player_one.turns_left) != 1)) + ". Score: " + str(player_one.score) + "\n\n"
    # If the player does not guess the correct order, show them how many dishes were place in the correct score. If they're out of turns, call the game_over function
    else:
        player_one.turns_left -= 1
        if (player_one.turns_left == 0):
            game_over(answer_count)
        else:
            statement = "\n" + str(answer_count) + " food " + check_plurality("item", answer_count != 1) + " placed correctly. " + str(player_one.turns_left) + " " + check_plurality("turn", (player_one.turns_left != 1)) + " remaining.\n\n=====\n"
            return statement

# End the game and print the correct answer
def game_over(answer_count):
    player_one.is_playing = False
    print("\n\n{} {} placed correctly.\n".format(answer_count, check_plurality("item", answer_count != 1)))
    def give_answer():
        statement = ''
        for guest in table:
            statement += "\n- " + str(guest)
        return statement
    print("\nThe correct answer was:", give_answer())
    print("\nYou're out of time. Better luck next time!\n\nGAME OVER\n\n")

# ======= START GAME =======

# Show welcome messsage, collect player name
player_name = input("\n_shifted\n\n.\n\n.\n\n.\n\nWelcome! What is your name? ")
player_one = Player(player_name)

print("\nHello, " + player_one.name + "!\n\nYou work at Chuck's, an esteemed local restaurant. It's a busy Friday night, and your head waiter suddenly had to leave work while waiting a table of four guests. Your friend has asked you to cover their shift.\n\nYour task is to determine the correct placement of the guests' dishes based on clues, as well as trial and error. You will have eight tries.")

print_info()

print("\nClues:\n- The guests are seated at a round table.\n- You can assume each person ordered one unique item from the menu.\n- " + guest_one.name + " is sitting at seat 1.")
print_clues()
print("\n")

# Allow the user to guess. Check if answer is correct and respond accordingly
while (player_one.is_playing == True):
    answer = input("Make your guess! Enter the correct list of dishes starting at seat 1.\n\n")
    print(check_answer(answer.lower()))