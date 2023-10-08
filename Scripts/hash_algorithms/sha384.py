import hashlib
from Scripts.generate_passwords import generate_passwords

def crack_sha384_hash(hash_str, password_length=1):
    """Find & return a matching password for a given sha384 hash"""
    while True:
        for guess in generate_passwords(password_length):
            # Check if the generated password matches the hash
            if hashlib.sha384(guess.encode('utf-8')).hexdigest() == hash_str:
                return guess
            print(guess)

        password_length += 1  # If no match is found, increase the password length
