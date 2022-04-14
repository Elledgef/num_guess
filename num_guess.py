# Author: Faith Elleged
# Grithub username: Elledgef
# Date: 4/13
# Description: Code used to guess user inputted number
num = int(input("Enter the integer for the player to guess"))
# use C to store the variable
count=0
guess= int(input("Enter your guess"))
while(True):
    count=count+1
    if (guess>num):
        guess= int(input("Too High-try again"))
        continue
    elif(guess<num):
        guess=int(input("Too low- try again"))
        continue
    else:
       break

print("You guesses in "+str(count)+ " tries")




