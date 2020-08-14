# Made by Jan de Geest

# First Training exercise to learn myself Python. Also reason why I am not using functions in this script.
# Based on my outcome of Guessing Game Challenge:
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp.git / 02-Python Statements / 09-Guessing Game Challenge.ipynb
# -----------------------

# Import from module to generate random number
from random import randint

# Creating objects and assigning values

random_num = randint(1,100)
myloop = True #I choose to use this variable instead of working with things like 'break' in my loop.
guess_list = [0]

# Intro text
print("This is a guessing game. \n :)")

# Loop itself

while myloop == True:
    try: #Thanks STACK OVERFLOW for the 'try' statement.
        user_input = int(input("Guess the right number:"))
        print(user_input)

        if user_input < 1 or user_input > 100:
            print('ERROR! \n You have to type a number between 1 and 100.\n Try again.')

        else:
            if user_input == random_num:
                print(f"\n You won! \n You guessed the right number! \n You guessed it right in {len(guess_list)} time(s)!")
                myloop = False

            else:
                guess_list.append(user_input)

                if guess_list[-2]: #Check if user already tried a guess before.

                    if abs(user_input - random_num) < abs(guess_list[-2] - random_num):
                        print("You're getting warmer.")

                    else:
                        print("You're getting colder.")

                else:
                    if abs(user_input-random_num) < 11:
                        print("Nice first try, you're warm!")

                    else:
                        print("You're cold.")


    except ValueError:
        print('ERROR! \n You have to type a number between 1 and 100.\n Try again.')

