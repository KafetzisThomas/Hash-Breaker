#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import hashlib
from Scripts.gen_pass import generate_passwords

def crack_sha224_hash(hash_str, wordlist, password_length=1, with_wordlist=False):
    """Find & return a matching password for a given sha224 hash"""
    if not with_wordlist:
        while True:
            for guess in generate_passwords(password_length):
                # Check if the generated password matches the hash
                if hashlib.sha224(guess.encode('utf-8')).hexdigest() == hash_str:
                    return guess
                print(guess)

            password_length += 1  # If no match is found, increase the password length
    else:
        with open(wordlist, 'r') as file:
            for line in file.readlines():
                if hashlib.sha224(line.strip().encode('utf-8')).hexdigest() == hash_str:
                    return line.strip()
                print(line.strip())
