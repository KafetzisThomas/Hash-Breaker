#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Hash-Breaker (https://github.com/KafetzisThomas/Hash-Breaker)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)
# License: GPLv3
# NOTE: By contributing to this project, you agree to the terms of the GPLv3 license, and agree to grant the project owner the right to also provide or sell this software, including your contribution, to anyone under any other license, with no compensation to you.

# Import built-in modules
import platform, os, sys, time

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
print(f"* You can enter {F.LIGHTGREEN_EX}Ctrl+C{F.RESET} to stop the process.")
print(f"\n1. Bcrypt")
print(f"2. MD5")
print(f"3. SHA-1")
print(f"4. SHA-224")
print(f"5. SHA-256")
print(f"6. SHA-384")
print(f"7. SHA-512")

try:
    choice = int(input("\nChoice (1-7): "))
    wordlist = input("Type path for wordlist [Enter] to skip this step\n")
    if wordlist and os.path.exists(os.path.dirname(wordlist)):
        with_wordlist = True
    else:
        with_wordlist = False
except ValueError:
    print(f"{F.LIGHTRED_EX}* Undefined choice.")
    sys.exit()
except KeyboardInterrupt:
    print(f"\n{F.LIGHTCYAN_EX}* Exiting...")
    sys.exit()

if choice == 1:
    try:
        print(f"* Please, remove {F.LIGHTBLUE_EX}b''{F.RESET} when you specify the hash.\n")
        hash_input = input("Enter Hash: ").strip()
        start = time.time()
        plain_text = crack_bcrypt_hash(hash_input)
        end = time.time()
        time_elapsed = end - start
    except ValueError as err:
        print(f"{F.LIGHTRED_EX}* Unidentifiable hash: {err}.")
        sys.exit()
    except KeyboardInterrupt:
        print(f"{F.LIGHTRED_EX}* Operation canceled.")
        sys.exit()
elif choice == 2:
    try:
        print(f"* Make sure your {F.LIGHTBLUE_EX}hash{F.RESET} is MD5, otherwise there will be an infinite loop.\n")
        hash_input = input("Enter Hash: ").strip()
        start = time.time()
        plain_text = crack_md5_hash(hash_input, with_wordlist=with_wordlist, wordlist=wordlist)
        end = time.time()
        time_elapsed = end - start
    except KeyboardInterrupt:
        print(f"{F.LIGHTRED_EX}* Operation canceled.")
        sys.exit()
elif choice == 3:
    try:
        print(f"* Make sure your {F.LIGHTBLUE_EX}hash{F.RESET} is SHA-1, otherwise there will be an infinite loop.\n")
        hash_input = input("Enter Hash: ").strip()
        start = time.time()
        plain_text = crack_sha1_hash(hash_input, with_wordlist=with_wordlist, wordlist=wordlist)
        end = time.time()
        time_elapsed = end - start
    except KeyboardInterrupt:
        print(f"{F.LIGHTRED_EX}* Operation canceled.")
        sys.exit()
elif choice == 4:
    try:
        print(f"* Make sure your {F.LIGHTBLUE_EX}hash{F.RESET} is SHA-224, otherwise there will be an infinite loop.\n")
        hash_input = input("Enter Hash: ").strip()
        start = time.time()
        plain_text = crack_sha224_hash(hash_input, with_wordlist=with_wordlist, wordlist=wordlist)
        end = time.time()
        time_elapsed = end - start
    except KeyboardInterrupt:
        print(f"{F.LIGHTRED_EX}* Operation canceled.")
        sys.exit()
elif choice == 5:
    try:
        print(f"* Make sure your {F.LIGHTBLUE_EX}hash{F.RESET} is SHA-256, otherwise there will be an infinite loop.\n")
        hash_input = input("Enter Hash: ").strip()
        start = time.time()
        plain_text = crack_sha256_hash(hash_input, with_wordlist=with_wordlist, wordlist=wordlist)
        end = time.time()
        time_elapsed = end - start
    except KeyboardInterrupt:
        print(f"{F.LIGHTRED_EX}* Operation canceled.")
        sys.exit()
elif choice == 6:
    try:
        print(f"* Make sure your {F.LIGHTBLUE_EX}hash{F.RESET} is SHA-384, otherwise there will be an infinite loop.\n")
        hash_input = input("Enter Hash: ").strip()
        start = time.time()
        plain_text = crack_sha384_hash(hash_input, with_wordlist=with_wordlist, wordlist=wordlist)
        end = time.time()
        time_elapsed = end - start
    except KeyboardInterrupt:
        print(f"{F.LIGHTRED_EX}* Operation canceled.")
        sys.exit()
elif choice == 7:
    try:
        print(f"* Make sure your {F.LIGHTBLUE_EX}hash{F.RESET} is SHA-512, otherwise there will be an infinite loop.\n")
        hash_input = input("Enter Hash: ").strip()
        start = time.time()
        plain_text = crack_sha512_hash(hash_input, with_wordlist=with_wordlist, wordlist=wordlist)
        end = time.time()
        time_elapsed = end - start
    except KeyboardInterrupt:
        print(f"{F.LIGHTRED_EX}* Operation canceled.")
        sys.exit()
else:
    print(f"\n{F.LIGHTRED_EX}* Undefined choice.")
    sys.exit()


print(f"Password Found: {B.LIGHTRED_EX}{F.BLACK} {plain_text} ")
print(f"Time elapsed: {time_elapsed:.1f}s")
