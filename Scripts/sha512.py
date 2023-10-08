import hashlib
from Scripts.chars import chars

def crack_sha512_hash(hash_str, password_length=1):
    """Find & return a matching password for a given sha512 hash"""
    while True:  # Keep generating random passwords until a match is found
        # Generate all possible combinations of characters for the current length
        for i in range(len(chars) ** password_length):
            guess = ""
            for j in range(password_length):
                # Calculate the index for character selection within the character set,
                # taking into account the current position (j) and password length,
                # then retrieve and append the selected character to the guess
                guess += chars[i // (len(chars) ** (password_length - j - 1)) % len(chars)]
                print(guess)

            # Check if the generated word matches the hash
            if hashlib.sha512(guess.encode('utf-8')).hexdigest() == hash_str:
                return guess

        password_length += 1  # If no match is found, increase the password length
