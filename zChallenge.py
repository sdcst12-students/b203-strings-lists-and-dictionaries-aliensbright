#!python3
# Explain what this code does

import random
x = []
for i in range(40): #return 40 random values
    if random.randint(0,1): #if value is 1, meaning true, append a random integer between one and ten
        x.append(random.randint(1,10))
    else: #if value is 0, meaning false, append a random decimal number that is achieved by adding an integer between 1 and ten
        #to decimal between 0.1 and 1.0
        x.append(random.randint(1,10) + random.randint(1,10)/10)

print(x) #print the completed list with 40 values


