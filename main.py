import guess_func as gf
import os

more_guessing = True
still_guessing = True

os.system("clear")
print("Welcome to the Number Guessing Game!\n\n")

while more_guessing:
    lives_left = gf.life_total()
    number_to_guess = gf.number_choice()

    while still_guessing and lives_left > 0:
        print(f"You have {lives_left} lives left.")
        player_guess = int(input("Make your choice: "))
        still_guessing = gf.number_check(player_guess, number_to_guess)
        lives_left =gf.life_reduction(lives_left, still_guessing)

    gf.endgame_message(lives_left, number_to_guess)

    still_guessing, more_guessing = gf.more_games(still_guessing, more_guessing)
    os.system("clear")