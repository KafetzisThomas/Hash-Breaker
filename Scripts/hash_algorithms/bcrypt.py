#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import bcrypt
from Scripts.gen_pass import generate_passwords


def crack_bcrypt_hash(hash_str, wordlist, password_length=1, with_wordlist=False):
    """Find & return a matching password for a given bcrypt hash"""
    if not with_wordlist:
        while True:
            for guess in generate_passwords(password_length):
                # Check if the generated password matches the hash
                if bcrypt.checkpw(guess.encode("utf-8"), hash_str.encode("utf-8")):
                    return guess

            password_length += 1  # If no match is found, increase the password length
    else:
        wordlist_found = False
        try:
            with open(wordlist, "r") as file:
                for line in file.readlines():
                    if bcrypt.checkpw(
                        line.strip().encode("utf-8"), hash_str.encode("utf-8")
                    ):
                        wordlist_found = True
                        return line.strip()

            if not wordlist_found:
                print(f"[*] No matching password found in {wordlist}")
        except FileNotFoundError:
            print(f"[*] Wordlist file not found: {wordlist}")
