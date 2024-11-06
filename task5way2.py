#!python3

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

def dropItem(a):
    test=0
    for i in items:
        if a==i and inventory[i]>0:
            inventory[i] -= 1
            showInventory()
            test=1
    if test==0:
        print("You were unable to drop that item.")



def getItem(i):
    try:
        inventory[i] += 1
        print("You got a piece of", i)
    except:
        print("Invalid Input.")


print('Welcome to The Real World \n\nInputs: \n Use "get" + any item to add an item to your inventory\n Use "drop" + any item to drop the item from your inventory\n Use "show inventory" to show how many items you have in your inventory\n')

y=1

while True:
    x = input(f"Input {y}:")
    if x=="show inventory":
        showInventory()
    else: 
        x=x.split()
        if x[0]=="get":
            getItem(x[1])
        elif x[0]=="drop":
            dropItem(x[1])
        else:
            print("Invalid input, please try again.")
    print('\nInputs:\n "get" + item\n "drop" + item\n "show inventory"\n')
    y += 1