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

try:
    if sys.argv[1] == "-bcrypt":
        hash_str = sys.argv[2]
        wordlist = None
        with_wordlist = False
        if "--with-wordlist" in sys.argv:
            wordlist = sys.argv[3]
            with_wordlist = True
        start = time.time()
        plain_text = crack_bcrypt_hash(hash_str=hash_str, wordlist=wordlist, with_wordlist=with_wordlist)
        end = time.time()
        time_elapsed = end - start
        if plain_text:
            print(f"Password Found: {B.LIGHTRED_EX}{F.BLACK} {plain_text} ")
            print(f"Time elapsed: {time_elapsed:.1f}s")
        sys.exit()
    elif sys.argv[1] == "-md5":
        hash_str = sys.argv[2]
        wordlist = None
        with_wordlist = False
        if "--with-wordlist" in sys.argv:
            wordlist = sys.argv[3]
            with_wordlist = True
        start = time.time()
        plain_text = crack_md5_hash(hash_str=hash_str, wordlist=wordlist, with_wordlist=with_wordlist)
        end = time.time()
        time_elapsed = end - start
        if plain_text:
            print(f"Password Found: {B.LIGHTRED_EX}{F.BLACK} {plain_text} ")
            print(f"Time elapsed: {time_elapsed:.1f}s")
        sys.exit()
    elif sys.argv[1] == "-sha1":
        hash_str = sys.argv[2]
        wordlist = None
        with_wordlist = False
        if "--with-wordlist" in sys.argv:
            wordlist = sys.argv[3]
            with_wordlist = True
        start = time.time()
        plain_text = crack_sha1_hash(hash_str=hash_str, wordlist=wordlist, with_wordlist=with_wordlist)
        end = time.time()
        time_elapsed = end - start
        if plain_text:
            print(f"Password Found: {B.LIGHTRED_EX}{F.BLACK} {plain_text} ")
            print(f"Time elapsed: {time_elapsed:.1f}s")
        sys.exit()
    elif sys.argv[1] == "-sha224":
        hash_str = sys.argv[2]
        wordlist = None
        with_wordlist = False
        if "--with-wordlist" in sys.argv:
            wordlist = sys.argv[3]
            with_wordlist = True
        start = time.time()
        plain_text = crack_sha224_hash(hash_str=hash_str, wordlist=wordlist, with_wordlist=with_wordlist)
        end = time.time()
        time_elapsed = end - start
        if plain_text:
            print(f"Password Found: {B.LIGHTRED_EX}{F.BLACK} {plain_text} ")
            print(f"Time elapsed: {time_elapsed:.1f}s")
        sys.exit()
    elif sys.argv[1] == "-sha256":
        hash_str = sys.argv[2]
        wordlist = None
        with_wordlist = False
        if "--with-wordlist" in sys.argv:
            wordlist = sys.argv[3]
            with_wordlist = True
        start = time.time()
        plain_text = crack_sha256_hash(hash_str=hash_str, wordlist=wordlist, with_wordlist=with_wordlist)
        end = time.time()
        time_elapsed = end - start
        if plain_text:
            print(f"Password Found: {B.LIGHTRED_EX}{F.BLACK} {plain_text} ")
            print(f"Time elapsed: {time_elapsed:.1f}s")
        sys.exit()
    elif sys.argv[1] == "-sha384":
        hash_str = sys.argv[2]
        wordlist = None
        with_wordlist = False
        if "--with-wordlist" in sys.argv:
            wordlist = sys.argv[3]
            with_wordlist = True
        start = time.time()
        plain_text = crack_sha384_hash(hash_str=hash_str, wordlist=wordlist, with_wordlist=with_wordlist)
        end = time.time()
        time_elapsed = end - start
        if plain_text:
            print(f"Password Found: {B.LIGHTRED_EX}{F.BLACK} {plain_text} ")
            print(f"Time elapsed: {time_elapsed:.1f}s")
        sys.exit()
    elif sys.argv[1] == "-sha512":
        hash_str = sys.argv[2]
        wordlist = None
        with_wordlist = False
        if "--with-wordlist" in sys.argv:
            wordlist = sys.argv[3]
            with_wordlist = True
        start = time.time()
        plain_text = crack_sha512_hash(hash_str=hash_str, wordlist=wordlist, with_wordlist=with_wordlist)
        end = time.time()
        time_elapsed = end - start
        if plain_text:
            print(f"Password Found: {B.LIGHTRED_EX}{F.BLACK} {plain_text} ")
            print(f"Time elapsed: {time_elapsed:.1f}s")
        sys.exit()
except IndexError:
    if len(sys.argv) > 1:
        print("Incorrect usage of command line arguments.")
        sys.exit()

print(text2art("Hash-Breaker"))
print(f"> Author: {F.LIGHTYELLOW_EX}KafetzisThomas")
print("-------------------------")
print(f"* You can enter {F.LIGHTMAGENTA_EX}Ctrl+C{F.RESET} to stop the process.")
print("\nMenu:")
print(f"  |- 1) Bcrypt  ({F.LIGHTGREEN_EX}STRONG{F.RESET})")
print(f"  |- 2) MD5     ({F.LIGHTRED_EX}WEAK{F.RESET})")
print(f"  |- 3) SHA-1   ({F.LIGHTYELLOW_EX}MODERATE{F.RESET})")
print(f"  |- 4) SHA-224 ({F.LIGHTYELLOW_EX}MODERATE{F.RESET})")
print(f"  |- 5) SHA-256 ({F.LIGHTYELLOW_EX}MODERATE{F.RESET})")
print(f"  |- 6) SHA-384 ({F.LIGHTYELLOW_EX}MODERATE{F.RESET})")
print(f"  |- 7) SHA-512 ({F.LIGHTYELLOW_EX}MODERATE{F.RESET})")

choice, with_wordlist, wordlist = get_user_input()
plain_text, time_elapsed = get_hash_input_and_crack(choice, with_wordlist, wordlist)

print(f"Password Found: {B.LIGHTRED_EX}{F.BLACK} {plain_text} ")
print(f"Time elapsed: {time_elapsed:.1f}s")
