import random

class NumberGuessingGame:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.target_number = random.randint(self.low, self.high)
        self.attempts = 0

    def play(self):
        print(f"Welcome to the Number Guessing Game! Guess a number between {self.low} and {self.high}.")

        while True:
            guess = int(input("Enter your guess: "))
            self.attempts += 1

            if guess < self.target_number:
                print("Too low! Try again.")
            elif guess > self.target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {self.target_number} in {self.attempts} attempts.")
                break

if __name__ == "__main__":
    game = NumberGuessingGame(1, 100)
    game.play()