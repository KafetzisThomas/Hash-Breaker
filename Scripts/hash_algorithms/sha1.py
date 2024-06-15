#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import hashlib
from Scripts.gen_pass import generate_passwords


def crack_sha1_hash(hash_str, wordlist, password_length=1, with_wordlist=False):
    """Find & return a matching password for a given sha1 hash"""
    if not with_wordlist:
        while True:
            for guess in generate_passwords(password_length):
                # Check if the generated password matches the hash
                if hashlib.sha1(guess.encode("utf-8")).hexdigest() == hash_str:
                    return guess

            password_length += 1  # If no match is found, increase the password length
    else:
        try:
            with open(wordlist, "r") as file:
                for line in file.readlines():
                    if (
                        hashlib.sha1(line.strip().encode("utf-8")).hexdigest()
                        == hash_str
                    ):
                        return line.strip()
        except FileNotFoundError:
            print(f"[!] Wordlist file not found: {wordlist}")
