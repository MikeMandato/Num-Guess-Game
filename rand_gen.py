import random

min = int
max = int

def number_guessing_game(min, max):
    print("Welcome to the number game :)")
    print(f"Enter a number between {min} and {max}!")

    number_to_guess = random.randint(1,500) ## How do I set this so that i only have to declare the numbers when I call the function?
    attempts = 0

    while True:
        attempts += 1
        try:
            user_guess = int(input("Enter your guess:"))
        except ValueError:
            print(f"Ooops, you entered {user_guess}, which is not a number. Try again.")
            continue
        # What would attempts start at if it was not stated above on line 11?  
        if user_guess == number_to_guess:
            print(f"Congrats!!! \nYou guessed '{number_to_guess}' in {attempts} attempts!")
            break
        elif abs(user_guess - number_to_guess) <= 10:
            if user_guess < number_to_guess:
                print("SUPER CLOSE! But still too low")
            else:
                print("SUPER CLOSE! But still too high")
        elif abs(user_guess - number_to_guess) <= 100:
            if user_guess < number_to_guess:
                print("Close, but still too low!")
            else:
                print("Close, but still too high")
        else:
            if user_guess < number_to_guess:
                print("Wayyy too low")
            else:
                print("Wayyy too high")

    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again[0] == "n":
        print("\nThanks for playing!\n")

# Need to fix the problem of a int or incorrect string breaking the loop!

#if user_guess != int:
#print("""Please enter a NUMBER. 
#Examples of numbers: 234, 401, 29, 1, 111, 197 
#Now don't f*ck this up. Enter NUMBER here: """)
#Could also put part of the print in the input :slight_smile:
#user_guess = int(input())

number_guessing_game(1, 500)