# # Importing the random module for generating the random number
# import random

# # Creating a variable and using the randint funtion of random value which gonna generate a random number betwween 1 and 100
# randNumber = random.randint(1, 100)

# # Creating a variable for the user to guess the number and declaring it none so that it will not throw an error because we gonna use
# # it in the while loop 
# userGuess = None

# # Declaring another variable that is number of guesses user takes to win the match. Initially it will start from 0
# guesses = 0

# # Creating a while loop so that the loop continues until the user perfectly guess the game
# while(userGuess != randNumber):
#     # Taking input from the user
#     userGuess = int(input("Enter the Guess value:\n"))
#     # Incrementing the number of guesses
#     guesses += 1

#     # Making a loop which will tell the user about his/her guesses and give them the idea to win the game
#     if (userGuess == randNumber):
#         print("You guessed it Right!")

#     else:
#         if (userGuess>randNumber):
#             print("You guessed it wrong! Please enter a smaller value..")
#         else:
#             print("You guessed it wrong! Please enter a larger value..")

# #Printing the number of guesses that user takes to win the game
# print(f"You guessed the right number in {guesses} guesses")

# # Now we goona save the Perfect guess in a file
# with open("Hiscore.txt", 'r') as f:
#     # Changing the function into string because the value is a string
#      Hiscore = int(f.read(guesses))

# if (guesses<Hiscore):
#     print("You have just broken the high score!")
#     with open("Hiscore.txt", "w") as f:
#         # Changing into string because the guess is a integer value and the function writtens the string value
#         f.write(str(guesses))