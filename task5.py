"""create a dictionary for an inventory of items in a game.  Ask the user for input, and if the item they
choose to 'get item', add that item to their inventory.  If they choose to drop item' remove that item from 
that inventory.  If they choose 'show inventory' give them a list of the items that they have. You will need 
to make use of the string.split() method in order to separate the item name from the action that precedes it."""

import math
import random


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
global items
items = ('food' ,'water','rope' ,'torch','sack' ,'wood' ,'iron' ,'steel','ginger','garlic','fish' ,'stone','wool')

def showInventory():
    print("You Have:")
    for i in inventory:
        if inventory[i]==0:
            pass
        else:
            print("",inventory[i], i)

def dropItem():
    x=input("Do you want to drop any items?")

def getItem():
    i = random.randint(0,12)
    print("You have found a piece of", items[i], "on the ground.\nDo you want to pick it up?")
    while True:
        x = input()
        if x=="yes":
            inventory[items[i]] += 1
            break
        elif x=="no":
            break
        elif x=="show inventory":
            showInventory()
        else:
            print("Invalid input, please try again")
    print("i did it maybe")



print('Welcome to The Real World \n\n Inputs: \n Use "get item" to add the item to your inventory\n Use "drop item" to drop the item from your inventory\n Use "show inventory" to show how many items you have in your inventory')


while True:
    getItem()
    x = input()
    if x=="get item":
        getItem()
    elif x=="drop item":
        dropItem()
    elif x=="show inventory":
        showInventory()
    else:
        for i in items:
            if x=="drop" + i:
                inventory[i] -= 1
                showInventory()

        print("Invalid input, please try again")