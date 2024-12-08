import random

SUPER_CLOSE_MESSAGE = "SUPER CLOSE! But still too {0}"
SUPER_CLOSE_PROXIMITY = 10
CLOSE_MESSAGE = "Close, but still too {0}!"
CLOSE_PROXIMITY = 100
FAR_AWAY_MESSAGE = "Wayyy too {0}"


def print_proximity_based_message(msg: str, guess_proximity: int) -> None:
    print(msg.format("low" if guess_proximity < 0 else "high"))

def get_game_variables(min: int, max: int):
    return random.randint(min, max), 0

def this_is_really_the_end(number_to_guess, attempts) -> bool:
    print(f"Congrats!!! \nYou guessed '{number_to_guess}' in {attempts} attempts!")
    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again[0] == "n":
        print("\nThanks for playing!\n")
        return True
    return False

def handle_guess_proximity_message(guess_proximity: str) -> None:
    if abs(guess_proximity) <= SUPER_CLOSE_PROXIMITY:
        print_proximity_based_message(SUPER_CLOSE_MESSAGE, guess_proximity)
    elif abs(guess_proximity) <= CLOSE_PROXIMITY:
        print_proximity_based_message(CLOSE_MESSAGE, guess_proximity)
    else:
        print_proximity_based_message(FAR_AWAY_MESSAGE, guess_proximity)

def number_guessing_game(min: int, max: int) -> None:
    print("Welcome to the number game :)")
    print(f"Enter a number between {min} and {max}!")

    number_to_guess, attempts = get_game_variables(min, max)

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
            if this_is_really_the_end(number_to_guess, attempts):
                return
            number_to_guess, attempts = get_game_variables(min, max)
            continue

        handle_guess_proximity_message(guess_proximity)


#if user_guess != int:
#print("""Please enter a NUMBER. 
#Examples of numbers: 234, 401, 29, 1, 111, 197 
#Now don't f*ck this up. Enter NUMBER here: """)
#Could also put part of the print in the input :slight_smile:
#user_guess = int(input())

number_guessing_game(1, 500)