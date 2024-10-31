"""create a dictionary for an inventory of items in a game.  Ask the user for input, and if the item they
choose to 'get item', add that item to their inventory.  If they choose to drop item' remove that item from 
that inventory.  If they choose 'show inventory' give them a list of the items that they have. You will need 
to make use of the string.split() method in order to separate the item name from the action that precedes it."""

import math

inventory = { # Quantity : Item
    'food'  :4,
    'water' :2,
    'rope'  :1,
    'torch' :3,
    'sack'  :1,
    'wood'  :0,
    'iron'  :1,
    'steel' :0,
    'ginger':1,
    'garlic':0,
    'fish'  :1,
    'stone' :14,
    'wool'  :1,

    }

def showInventory():
    pass

def getItem():
    pass

def dropItem():
    pass

print('Welcome to The Real World \n\n Inputs: \n Use "get item" to add the item to your inventory\n Use "drop item" to drop the item from your inventory\n Use "show inventory" to show how many items you have in your inventory')
    

while True:
    x = input()
    if x=="get item":
        pass
    elif x=="drop item":
        pass
    elif x=="show inventory":
        print("You Have:")
        for i in inventory:
            if inventory[i]==0:
                pass
            else:
                print("",inventory[i], i)
    else:
        print("Invalid input, please try again")