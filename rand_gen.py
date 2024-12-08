import random


class NumberGuessingGame:

    __super_close_proximity = 10
    __close_proximity = 100

    def __init__(self, min: int, max: int):
        self.min, self.max = min, max
        self.__reset_game_variables()
    
    def play(self) -> None:
        print("Welcome to the number game :)")
        print(f"Enter a number between {self.min} and {self.max}!")

        while True:
            self.attempts += 1
            user_guess = input("Enter your guess:")

            if user_guess.isnumeric():
                user_guess = int(user_guess)
            else:
                print(f"Ooops, you entered {user_guess}, which is not a number. Try again.")
                continue
            
            guess_proximity = user_guess - self.number_to_guess
            if guess_proximity != 0:
                self.__handle_guess_proximity_message(guess_proximity)
                continue

            if self.__this_is_really_the_end():
                return
            
            self.__reset_game_variables()

    def __reset_game_variables(self):
        self.attempts = 0
        self.number_to_guess = random.randint(self.min, self.max)

    def __this_is_really_the_end(self) -> bool:
        print(f"Congrats!!! \nYou guessed '{self.number_to_guess}' in {self.attempts} attempts!")
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again[0] == "n":
            print("\nThanks for playing!\n")
            return True
        return False

    def __handle_guess_proximity_message(self, guess_proximity: str) -> None:
        high_or_low = "low" if guess_proximity < 0 else "high"
        if abs(guess_proximity) <= self.__super_close_proximity:
            print(f"SUPER CLOSE! But still too {high_or_low}")
        elif abs(guess_proximity) <= self.__close_proximity:
            print(f"Close, but still too {high_or_low}!")
        else:
            print(f"Wayyy too {high_or_low}")


if __name__ == "__main__":
    coolest_game_ever = NumberGuessingGame(1, 500)
    coolest_game_ever.play()
