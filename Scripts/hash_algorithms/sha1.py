#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import hashlib
from Scripts.gen_pass import generate_passwords

def crack_sha1_hash(hash_str, password_length=1):
    """Find & return a matching password for a given sha1 hash"""
    while True:
        for guess in generate_passwords(password_length):
            # Check if the generated password matches the hash
            if hashlib.sha1(guess.encode('utf-8')).hexdigest() == hash_str:
                return guess
            print(guess)

        password_length += 1  # If no match is found, increase the password length
