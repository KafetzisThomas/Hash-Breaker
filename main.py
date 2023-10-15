#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Hash-Breaker (https://github.com/KafetzisThomas/Hash-Breaker)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)
# License: GPLv3
# NOTE: By contributing to this project, you agree to the terms of the GPLv3 license, and agree to grant the project owner the right to also provide or sell this software, including your contribution, to anyone under any other license, with no compensation to you.

# Import built-in modules
import platform, os, sys

# Import module files
from Scripts.utils import get_user_input
from Scripts.utils import get_hash_input_and_crack

# Import other (third-party) modules
import colorama
from art import text2art
from colorama import Fore as F, Back as B
colorama.init(autoreset=True)

# Check system platform to set correct console clear command
clear_command = "cls" if platform.system() == "Windows" else "clear"
os.system(clear_command)  # Clear console

# Run check on python version, must be 3.6 or higher because of f strings
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    print("Error Code U-2: This script requires running python 3.6 or higher! You are running" + str(sys.version_info[0]) + "." + str(sys.version_info[1]))
    sys.exit()

print(text2art("Hash-Breaker"))
print(f"> Author: {F.LIGHTYELLOW_EX}KafetzisThomas")
print("-------------------------")
print(f"* You can enter {F.LIGHTMAGENTA_EX}Ctrl+C{F.RESET} to stop the process.")
print(f"\n1. Bcrypt   ({F.LIGHTGREEN_EX}STRONG{F.RESET})")
print(f"2. MD5      ({F.LIGHTRED_EX}WEAK{F.RESET})")
print(f"3. SHA-1    ({F.LIGHTYELLOW_EX}MODERATE{F.RESET})")
print(f"4. SHA-224  ({F.LIGHTYELLOW_EX}MODERATE{F.RESET})")
print(f"5. SHA-256  ({F.LIGHTYELLOW_EX}MODERATE{F.RESET})")
print(f"6. SHA-384  ({F.LIGHTYELLOW_EX}MODERATE{F.RESET})")
print(f"7. SHA-512  ({F.LIGHTYELLOW_EX}MODERATE{F.RESET})")

choice, with_wordlist, wordlist = get_user_input()
plain_text, time_elapsed = get_hash_input_and_crack(choice, with_wordlist, wordlist)

print(f"Password Found: {B.LIGHTRED_EX}{F.BLACK} {plain_text} ")
print(f"Time elapsed: {time_elapsed:.1f}s")
