import random

# Guest names (four will be chosen per game) 
names = ['Anna', 'Ari', 'Beau', 'Chris', 'Damon', 'Gabi', 'Hannah', 'Jamal', 'Jill', 'Javier', 'Kai', 'Kayla', 'Kim', 'Luke', 'Malik', 'Nina', 'Pasha', 'Talia', 'Trey', 'Wesley']

# List of dishes (six will appear on the menu, and one unique dish will be assigned to each of the four guests)
dishes = ['pizza', 'burger', 'salad', 'pasta', 'soup', 'sandwich', 'burrito', 'fish']

# Person class will be used for four guest objects
class Guest:
    def __init__(self, name, dish, place):
        self.name = name
        self.dish = dish
        self.place = place
    
    def __repr__(self):
        return self.name + ', ' + self.dish + ', place ' + str(self.place) + '\n'

# Select random item from a list, remove it from the list and return it
def select_item(my_list):
    item = random.choice(my_list)
    my_list.remove(item)
    return item

# These numbers will be used to track how many times the Person is referenced in a clue
direct_spatial_references = 0
direct_dish_references = 0

# Create four guests
guest_one = Guest(select_item(names), select_item(dishes), 1)
guest_two = Guest(select_item(names), select_item(dishes), 2)
guest_three = Guest(select_item(names), select_item(dishes), 3)
guest_four = Guest(select_item(names), select_item(dishes), 4)

# Create list with four guests
table = [guest_one, guest_two, guest_three, guest_four]

# Create separate alphabatized list of four guests
def get_name(guest):
    return guest.name
alpha_table = sorted(table, key=get_name)

# Create menu with six dishes, including four that guests have chosen. Then alphabatize menu
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
    guest.does_not_like = random.choice([dish for dish in menu if dish != guest.dish])

# Initialize Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turns_left = 8
        self.is_playing = True

    def __repr__(self):
        statement = 'name: ' + self.name + ', score: ' + str(self.score) + ', turns left: ' + str(self.turns_left) + ', is playing: ' + str(self.is_playing)
        return statement

# ======= START GAME =======

# Show welcome messsage, collect player name
player_name = input('\n_shifted\n\n.\n\n.\n\n.\n\nWelcome! What is your name? ')
player_one = Player(player_name)