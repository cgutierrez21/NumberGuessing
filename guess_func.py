import random
import os

def number_choice():
    print("I have chosen a number from 1 to 100.")
    return random.randint(1,100)

def life_total():
    print("What level of difficulty do you choose?")
    difficulty = int(input("Enter 1 for easy, and 2 for hard: "))

    if difficulty == 1:
        return 10

    elif difficulty == 2:
        return 5

    else:
        os.system("clear")
        print("Incorrect input, please type 1 or 2.")
        life_total()

def number_check(number_guessed, number_to_guess):

    if number_guessed == number_to_guess:
        return False

    elif number_guessed < number_to_guess:
        print("Too low.\n")

    else:
        print("Too high.\n")

    return True

def life_reduction(lives, still_guessing):
    if still_guessing:
        lives -= 1
        return lives
    else:
        return lives

def endgame_message(lives, number_to_guess):
    if lives == 0:
        print("You ran out of lives.")
        print(f"Better luck next time, but the number was {number_to_guess}.")
    else:
        print(f"\nCorrect! The answer was {number_to_guess}!\n")

def more_games(still_guessing, more_guessing):
    player_answer = input("Want to guess some more?\ny for yes and n for no: ").lower()

    if player_answer == "y" or player_answer == "yes":
        return True, True
    else:
        return False, False
