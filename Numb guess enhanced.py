import random

min = int
max = int

def NumGame(min, max):
    print("Welcome to the number game :)")
    print(f"Enter a number between {min} and {max}!")

## IS IT TO 1 - 499????? DOES IT NEED TO BE 501????
    GameInt = random.randint(1,500) ## How do I set this so that i only have to declare the numbers when I call the function?
    ## Was testing and needed a quick way to test (y/n)
    # GameInt = 250
    attempts = 0

    while True:
        try:
            UserGuess = int(input("Enter your guess:"))
            # What would attempts start at if it was not stated above on line 11?  
            attempts += 1
            if UserGuess == GameInt:
                print(f"Congrats!!! \nYou guessed '{GameInt}' in {attempts} attempts!")
                
                ## Do I need another 'Try, except' statement for this input. How does it work for string?
                PlayAgain = input("Would you like to play again? (y/n): ").lower()
                if PlayAgain[0] == "n":
                    print("\nThanks for playing!\n")
                    break
                else:
                    print("\nGet ready\n")
                    continue
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


## Can I put this in the 'if UserGuess == GameInt' loop?
# PlayAgain = input("Would you like to play again? (y/n): ").lower()
# if PlayAgain[0] == "n":
#     print("\nThanks for playing!\n")
    

# Need to fix the problem of a int or incorrect string breaking the loop!

#if UserGuess != int:
#print("""Please enter a NUMBER. 
#Examples of numbers: 234, 401, 29, 1, 111, 197 
#Now don't f*ck this up. Enter NUMBER here: """)
#Could also put part of the print in the input :)
#UserGuess = int(input())

NumGame(1, 500)