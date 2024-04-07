import random
import math

#Taking inputs
lower = int(input("Enter Lower Bound: "))
upper = int(input("Enter Upper Bound: "))

#generating random numbers between bounds
x = random.randint(lower,upper)
print("\n\t You've only got",round(math.log(upper-lower+1,2)),"chances to guess the interger!\n")

#initializing number of guesses
count = 0

#Calculating minimum number of guesses depnds upon range
while count <= math.log(upper - lower + 1, 2):
    count += 1

    #takes user guess
    guess = int(input("Guess a number "))

    #condition testing
    if x == guess:
        print("Congrats you did it in", count, "tries")
        #Once guessed, loop will break 
        break
    elif x > guess:
        print("You guess is too low")
    elif x < guess:
        print("You guess is too high")

if count > math.log(upper - lower +1,2):
    print("\n Ran out of guesses, The number is %d" % x)