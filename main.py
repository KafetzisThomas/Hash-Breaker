#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Bcrypt-Breaker (https://github.com/KafetzisThomas/Bcrypt-Breaker)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

# Import built-in modules
import platform, os, sys, time

# Import other (third-party) modules
import bcrypt, colorama
from art import text2art
from colorama import Fore as F, Back as B
colorama.init(autoreset=True)


chars = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6',
    '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '*',
    '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
    '@', '^', '_', '`', '{', '|', '}', '~', '[', '\\', ']',
    '(', ')'
]

def crack_bcrypt_hash(hash: str, password_length=1):
    """Find & return a matching password for a given bcrypt hash"""
    while True:  # Keep generating random passwords until a match is found
        # Generate all possible combinations of characters for the current length
        for i in range(len(chars) ** password_length):
            guess = ""
            for j in range(password_length):
                # Calculate the index for character selection within the character set,
                # taking into account the current position (j) and password length,
                # then retrieve and append the selected character to the guess
                guess += chars[i // (len(chars) ** (password_length - j - 1)) % len(chars)]
                print(guess)

            # Check if the generated password matches the hash
            if bcrypt.checkpw(guess.encode('utf-8'), hash.encode('utf-8')):
                return guess

        password_length += 1  # If no match is found, increase the password length


if __name__ == '__main__':
    # Check system platform to set correct console clear command
    clear_command = "cls" if platform.system() == "Windows" else "clear"
    os.system(clear_command)  # Clear console

    # Run check on python version, must be 3.6 or higher because of f strings
    if sys.version_info[0] < 3 or sys.version_info[1] < 6:
        print("Error Code U-2: This script requires running python 3.6 or higher! You are running" + str(sys.version_info[0]) + "." + str(sys.version_info[1]))
        sys.exit()

    print(text2art("Bcrypt-Breaker"))
    print(f"> Author: {F.LIGHTYELLOW_EX}KafetzisThomas")
    print("-------------------------")
    print(f"* Please remove {F.LIGHTBLUE_EX}b''{F.RESET} when you specify the hash.")
    print(f"* You can enter {F.LIGHTGREEN_EX}Ctrl+C{F.RESET} to stop the process.")

    try:
        hash = input("\nEnter Hash: ")
        start = time.time()
        password = crack_bcrypt_hash(hash)
        end = time.time()
    except ValueError as err:
        print(f"{F.LIGHTRED_EX}* Unidentifiable hash: {err}.")
        sys.exit()
    except KeyboardInterrupt:
        print(f"\n{F.LIGHTRED_EX}* Operation canceled.")
        sys.exit()

    time_elapsed = end - start
    print(f"Password Found: {B.LIGHTRED_EX}{F.LIGHTBLACK_EX} {password} ")
    print(f"Time elapsed: {time_elapsed:.1f}s")
