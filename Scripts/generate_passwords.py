import string
import itertools

def generate_passwords(password_length):
    """Generate all possible combinations of characters for a given length"""
    chars = string.ascii_letters + string.digits + string.punctuation
    all_combinations = itertools.product(chars, repeat=password_length)
    return (''.join(combination) for combination in all_combinations)
