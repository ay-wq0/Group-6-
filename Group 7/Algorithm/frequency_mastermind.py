import itertools
from collections import Counter

def get_feedback(secret, guess):
    # Correct position
    correct_position = sum(s == g for s, g in zip(secret, guess))
    
    # Correct color (frequency-based)
    secret_count = Counter(secret)
    guess_count = Counter(guess)
    
    correct_color = sum(
        min(secret_count[c], guess_count[c]) for c in secret_count
    ) - correct_position
    
    return correct_position, correct_color


def frequency_based_mastermind(secret, colors=6, positions=4):
    possible_codes = list(itertools.product(range(1, colors + 1), repeat=positions))
    attempts = 0

    while possible_codes:
        guess = possible_codes[0]
        attempts += 1
        
        feedback = get_feedback(secret, guess)

        if list(guess) == secret:
            print("Secret found!")
            print("Guess:", guess)
            print("Attempts:", attempts)
            return attempts
        
        # Eliminate impossible guesses
        possible_codes = [
            code for code in possible_codes
            if get_feedback(code, guess) == feedback
        ]

    return -1


# Example usage
secret_code = [1, 3, 5, 2]
frequency_based_mastermind(secret_code)
