import random


def number_guessing_game(min: int, max: int):
    print("Welcome to the number game :)")
    print(f"Enter a number between {min} and {max}!")

    # Define game constants
    number_to_guess = random.randint(min, max)
    super_close_message = "SUPER CLOSE! But still too {0}"
    close_message = "Close, but still too {0}!"
    far_away_message = "Wayyy too {0}"

    attempts = 0
    while True:
        attempts += 1
        user_guess = input("Enter your guess:")

        try:
            user_guess = int(user_guess)
        except ValueError:
            print(f"Ooops, you entered {user_guess}, which is not a number. Try again.")
            continue
        
        guess_proximity = abs(user_guess - number_to_guess)
        if guess_proximity == 0:
            print(f"Congrats!!! \nYou guessed '{number_to_guess}' in {attempts} attempts!")
            break
        elif guess_proximity <= 10:
            if user_guess < number_to_guess:
                print(super_close_message.format("low"))
            else:
                print(super_close_message.format("high"))
        elif guess_proximity <= 100:
            if user_guess < number_to_guess:
                print(close_message.format("low"))
            else:
                print(close_message.format("high"))
        else:
            if user_guess < number_to_guess:
                print(far_away_message.format("low"))
            else:
                print(far_away_message.format("high"))

    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again[0] == "n":
        print("\nThanks for playing!\n")


#if user_guess != int:
#print("""Please enter a NUMBER. 
#Examples of numbers: 234, 401, 29, 1, 111, 197 
#Now don't f*ck this up. Enter NUMBER here: """)
#Could also put part of the print in the input :slight_smile:
#user_guess = int(input())

number_guessing_game(1, 500)