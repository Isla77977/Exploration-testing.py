#Guessing Game!
#Ask the player their name.
name = input("Welcome! What is your name? ")
print("Hello ", name)
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
#Start the game.
#You won!
#You lost..