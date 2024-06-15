#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import hashlib
from Scripts.gen_pass import generate_passwords


def crack_sha_hash(
    hash_type, hash_str, wordlist=None, password_length=1, with_wordlist=False
):
    """Find & return a matching password for a given sha type of hash (sha1, sha224, etc.)."""
    hash_func = getattr(hashlib, hash_type)

    if not with_wordlist:
        while True:
            for guess in generate_passwords(password_length):
                if hash_func(guess.encode("utf-8")).hexdigest() == hash_str:
                    return guess
            password_length += 1  # If no match is found, increase the password length
    else:
        wordlist_found = False
        try:
            with open(wordlist, "r") as file:
                for line in file.readlines():
                    if hash_func(line.strip().encode("utf-8")).hexdigest() == hash_str:
                        wordlist_found = True
                        return line.strip()
            if not wordlist_found:
                print(f"[*] No matching password found in {wordlist}")
        except FileNotFoundError:
            print(f"[*] Wordlist file not found: {wordlist}")
