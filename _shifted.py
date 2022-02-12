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

# Create four guests
guest_one = Guest(select_item(names), select_item(dishes), 1)
guest_two = Guest(select_item(names), select_item(dishes), 2)
guest_three = Guest(select_item(names), select_item(dishes), 3)
guest_four = Guest(select_item(names), select_item(dishes), 4)

# Create list with four guests
table = [guest_one, guest_two, guest_three, guest_four]

# Establish positional relationships with other guests
for guest in table:
    guest.right_neighbor = table[guest.place - 2]
    if (guest.place < 4):
        guest.left_neighbor = table[guest.place]
    elif (guest.place == 4):
        guest.left_neighbor = table[0]
    guest.neighbors = [guest.right_neighbor, guest.left_neighbor]
    guest.opposite = table[guest.place - 3]