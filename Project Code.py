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
