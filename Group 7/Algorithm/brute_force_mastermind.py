import itertools

def brute_force_mastermind(secret, colors=6, positions=4):
    attempts = 0
    
    # Generate all possible combinations
    for guess in itertools.product(range(1, colors + 1), repeat=positions):
        attempts += 1
        
        # Direct position-by-position comparison
        if list(guess) == secret:
            print("Secret found!")
            print("Guess:", guess)
            print("Attempts:", attempts)
            return attempts

    return -1


# Example usage
secret_code = [1, 3, 5, 2]
brute_force_mastermind(secret_code)
