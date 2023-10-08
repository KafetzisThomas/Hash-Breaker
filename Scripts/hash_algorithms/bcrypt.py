#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import bcrypt
from Scripts.generate_passwords import generate_passwords

def crack_bcrypt_hash(hash_str, password_length=1):
    """Find & return a matching password for a given bcrypt hash"""
    while True:
        for guess in generate_passwords(password_length):
            # Check if the generated password matches the hash
            if bcrypt.checkpw(guess.encode('utf-8'), hash_str.encode('utf-8')):
                return guess
            print(guess)

        password_length += 1  # If no match is found, increase the password length
