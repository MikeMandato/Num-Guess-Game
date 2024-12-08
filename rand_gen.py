import random

min = int
max = int

def NumGame(min, max):
    print("Welcome to the number game :)")
    print(f"Enter a number between {min} and {max}!")

    GameInt = random.randint(1,500) ## How do I set this so that i only have to declare the numbers when I call the function?
    attempts = 0

    while True:
        try:
            UserGuess = int(input("Enter your guess:"))
            # What would attempts start at if it was not stated above on line 11?  
            attempts += 1
            if UserGuess == GameInt:
                print(f"Congrats!!! \nYou guessed '{GameInt}' in {attempts} attempts!")
                break
            elif abs(UserGuess - GameInt) <= 10:
                if UserGuess < GameInt:
                    print("SUPER CLOSE! But still too low")
                else:
                    print("SUPER CLOSE! But still too high")
            elif abs(UserGuess - GameInt) <= 100:
                if UserGuess < GameInt:
                    print("Close, but still too low!")
                else:
                    print("Close, but still too high")
            else:
                if UserGuess < GameInt:
                    print("Wayyy too low")
                else:
                    print("Wayyy too high")
        except ValueError:
            print("Ooops. Wrong input, try again.")
    PlayAgain = input("Would you like to play again? (y/n): ").lower()
    if PlayAgain[0] == "n":
        print("\nThanks for playing!\n")

# Need to fix the problem of a int or incorrect string breaking the loop!

#if UserGuess != int:
#print("""Please enter a NUMBER. 
#Examples of numbers: 234, 401, 29, 1, 111, 197 
#Now don't f*ck this up. Enter NUMBER here: """)
#Could also put part of the print in the input :slight_smile:
#UserGuess = int(input())

NumGame(1, 500)