import random


def print_proximity_based_message(msg: str, guess_proximity: int):
    print(msg.format("low" if guess_proximity < 0 else "high"))

def get_game_variables(min: int, max: int):
    return random.randint(min, max), 0

def number_guessing_game(min: int, max: int):
    print("Welcome to the number game :)")
    print(f"Enter a number between {min} and {max}!")

    number_to_guess, attempts = get_game_variables(min, max)

    # Define game constants
    super_close_message, super_close_proximity = "SUPER CLOSE! But still too {0}", 10
    close_message, close_proximity = "Close, but still too {0}!", 100
    far_away_message = "Wayyy too {0}"

    while True:
        attempts += 1
        user_guess = input("Enter your guess:")

        if user_guess.isnumeric():
            user_guess = int(user_guess)
        else:
            print(f"Ooops, you entered {user_guess}, which is not a number. Try again.")
            continue
        
        guess_proximity = user_guess - number_to_guess
        if guess_proximity == 0:
            print(f"Congrats!!! \nYou guessed '{number_to_guess}' in {attempts} attempts!")
            play_again = input("Would you like to play again? (y/n): ").lower()
            if play_again[0] == "n":
                print("\nThanks for playing!\n")
                return
            number_to_guess, attempts = get_game_variables(min, max)
            continue
        
        if abs(guess_proximity) <= super_close_proximity:
            print_proximity_based_message(super_close_message, guess_proximity)
        elif abs(guess_proximity) <= close_proximity:
            print_proximity_based_message(close_message, guess_proximity)
        else:
            print_proximity_based_message(far_away_message, guess_proximity)


#if user_guess != int:
#print("""Please enter a NUMBER. 
#Examples of numbers: 234, 401, 29, 1, 111, 197 
#Now don't f*ck this up. Enter NUMBER here: """)
#Could also put part of the print in the input :slight_smile:
#user_guess = int(input())

number_guessing_game(1, 500)