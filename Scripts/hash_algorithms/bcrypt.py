#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import bcrypt
from Scripts.gen_pass import generate_passwords

def crack_bcrypt_hash(hash_str, wordlist, password_length=1, with_wordlist=False):
    """Find & return a matching password for a given bcrypt hash"""
    if not with_wordlist:
        while True:
            for guess in generate_passwords(password_length):
                # Check if the generated password matches the hash
                if bcrypt.checkpw(guess.encode('utf-8'), hash_str.encode('utf-8')):
                    return guess
                print(guess)

            password_length += 1  # If no match is found, increase the password length
    else:
        with open(wordlist, 'r') as file:
            for line in file.readlines():
                if bcrypt.checkpw(line.encode('utf-8'), hash_str.encode('utf-8')):
                    return line.strip()
                print(line.strip())
