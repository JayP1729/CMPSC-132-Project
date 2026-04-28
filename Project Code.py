#Number Guessing Game
#Computer generates a random number
#Player uses terminal to guess number in a certain number of attempts
#Game stops when player guesses number or runs out of attempts
#Extensions: Difficulty, limiting the number of attempts, allowing replay

import random

class GuessingGame:
    difficulty_setting = {
        "easy":   {"range": (1, 50),  "max_attempts": 10},
        "medium": {"range": (1, 100), "max_attempts": 7},
        "hard":   {"range": (1, 200), "max_attempts": 5},
    }

    def __init__(self, difficulty):
        """
        Sets up a new game round based on difficulty.
        Input: difficulty string
        Output: none
        """
        setting = self.difficulty_setting[difficulty]
        self.low = setting["range"]
        self.high = setting["range"]
        self.max_attempts = setting["max_attempts"]
        self.number = random.randint(self.low, self.high)
        self.attempts = 0
        self.won = False

    def check_guess(self, guess):
        """
        Compares guess to secret number and returns feedback string.
        Input: integer guess
        Output: "too_high", "too_low", or "correct"
        """
        self.attempts += 1
        if guess < self.number:
            return "too_low"
        if guess > self.number:
            return "too_high"
        self.won = True
        return "correct"
    
    def attempts_reminaing(self):
        """
        Returns how many guesses the player has left.
        Input: none
        Output: integer
        """
        return self.max_attempts - self.attempts
    
    def is_over(self):
        """
        Returns True if the player won or ran out of attempts.
        Input: none
        Output: bool
        """
        return self.won or (self.attempts >= self.max_attempts)

def get_difficulty():
    """
    Prompts the player to pick a difficulty and validates input.
    Input: none (reads from terminal)
    Output: difficulty string
    """
    valid = ["easy", "medium", "hard"]
    choice = input("Pick a difficulty level (easy / medium / hard): ").strip().lower()
    while choice not in valid:
        print("Please choose a valid option. Try easy, medium, or hard")
        choice = input("Pick a difficulty level (easy / medium / hard): ").strip().lower()
    return choice

def guess(low, high):
    """
    Prompts the player for a guess and validates it's an integer in range.
    Input: none (reads from terminal); low/high define valid range
    Output: integer guess
    """
    text = input(f"Your guess ({low}-{high}): ").strip()
    while not text.lstrip("-").isdigit() or not (low <= int(text) <= high):
        if not text.lstrip("-").isdigit():
            print("Please enter a number")
        else:
            print(f"Guess must be between {low} and {high}")
        text = input(f"Your guess ({low}-{high}): ").strip()
    return int(text)


