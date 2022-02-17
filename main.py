#Guessing Game!
import random
#Ask the player their name.
name = input("Welcome! What is your name? ")
print("Hello,", name)
#Ask the player if they would like Easy, Normal, or Hard.
difficulty = input("Okay. Please pick either Easy, Medium, or Hard. ")
if difficulty == "Easy":
  print("{} it is!".format(difficulty))
elif difficulty == "Medium":
  print("{} it is!".format(difficulty))
elif difficulty == "Hard":
  print("{} it is!".format(difficulty))
else:
  print("Sorry, that is not a difficulty.")
#Add random number generator for each difficulty.
if difficulty == "Easy":
  easy = (random.randint(1, 10))
  print(easy)
elif difficulty == "Medium":
  medium = (random.randint(1, 50))
  print(medium)
elif difficulty == "Hard":
  hard = (random.randint(1, 100))
  print(hard)
#Add variable for lives.
#Start the game.
#Higher or lower.
#Show guessed numbers.
#You won!
#You lost..
#Play again.

#Make the game look nicer?