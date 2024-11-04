#!python3
# Explain what this code does

import random #importing the random module allows us to get random values
x = [] #x is an empty list
for i in range(40): #return 40 random values
    if random.randint(0,1): #if value is 1, meaning true, do the code below
        x.append(random.randint(1,10)) #append a random integer between one and ten to the list x
    else: #if value is 0, meaning false perform this code below
        x.append(random.randint(1,10) + random.randint(1,10)/10) #append a random decimal number to list x that is
        #achieved by adding an integer between 1 and ten to a decimal between 0.1 and 1.0

print(x) #print the completed list with 40 values


