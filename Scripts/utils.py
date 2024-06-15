#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Import built-in modules
import os
import time
import sys

# Import module files
from Scripts.hash_algorithms.bcrypt import crack_bcrypt_hash
from Scripts.hash_algorithms.md5 import crack_md5_hash
from Scripts.hash_algorithms.sha1 import crack_sha1_hash
from Scripts.hash_algorithms.sha224 import crack_sha224_hash
from Scripts.hash_algorithms.sha256 import crack_sha256_hash
from Scripts.hash_algorithms.sha384 import crack_sha384_hash
from Scripts.hash_algorithms.sha512 import crack_sha512_hash

# Import other (third-party) modules
import colorama
from colorama import Fore as F

colorama.init(autoreset=True)


def get_user_input():
    try:
        choice = int(input("\nEnter your choice (1-7): "))
        wordlist = input("Type path for wordlist [Enter] to skip this step\n")
        if wordlist:
            with_wordlist = True
        else:
            with_wordlist = False
    except ValueError:
        print(f"{F.LIGHTRED_EX}[*] Undefined choice.")
        sys.exit()
    except KeyboardInterrupt:
        print(f"\n{F.LIGHTCYAN_EX}[*] Exiting...")
        sys.exit()

    return choice, with_wordlist, wordlist


def get_hash_input_and_crack(choice, with_wordlist, wordlist):
    try:
        hash_input = input(f"[*] Enter {F.LIGHTBLUE_EX}Hash{F.RESET}: ").strip()
        start = time.time()

        if hash_input:
            if choice == 1:
                plain_text = crack_bcrypt_hash(
                    hash_input, with_wordlist=with_wordlist, wordlist=wordlist
                )
            elif choice == 2 and len(hash_input) == 32:
                plain_text = crack_md5_hash(
                    hash_input, with_wordlist=with_wordlist, wordlist=wordlist
                )
            elif choice == 3 and len(hash_input) == 40:
                plain_text = crack_sha1_hash(
                    hash_input, with_wordlist=with_wordlist, wordlist=wordlist
                )
            elif choice == 4 and len(hash_input) == 56:
                plain_text = crack_sha224_hash(
                    hash_input, with_wordlist=with_wordlist, wordlist=wordlist
                )
            elif choice == 5 and len(hash_input) == 64:
                plain_text = crack_sha256_hash(
                    hash_input, with_wordlist=with_wordlist, wordlist=wordlist
                )
            elif choice == 6 and len(hash_input) == 96:
                plain_text = crack_sha384_hash(
                    hash_input, with_wordlist=with_wordlist, wordlist=wordlist
                )
            elif choice == 7 and len(hash_input) == 128:
                plain_text = crack_sha512_hash(
                    hash_input, with_wordlist=with_wordlist, wordlist=wordlist
                )
            else:
                print(f"{F.LIGHTRED_EX}[*] Unidentifiable hash.")
                sys.exit()
        else:
            print(f"{F.LIGHTRED_EX}[*] Error: Invalid hash input.")
            sys.exit()

        end = time.time()
        time_elapsed = end - start
    except KeyboardInterrupt:
        print(f"n{F.LIGHTRED_EX}[*] Operation canceled.")
        sys.exit()

    return plain_text, time_elapsed
