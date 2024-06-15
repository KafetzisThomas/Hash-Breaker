#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Hash-Breaker (https://github.com/KafetzisThomas/Hash-Breaker)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)
# License: GPLv3
# NOTE: By contributing to this project, you agree to the terms of the GPLv3 license, and agree to grant the project owner the right to also provide or sell this software, including your contribution, to anyone under any other license, with no compensation to you.

import sys
import time
import colorama
from colorama import Fore as F, Back as B
from Scripts.hash_algorithms.bcrypt import crack_bcrypt_hash
from Scripts.hash_algorithms.md5 import crack_md5_hash
from Scripts.hash_algorithms.sha1 import crack_sha1_hash
from Scripts.hash_algorithms.sha224 import crack_sha224_hash
from Scripts.hash_algorithms.sha256 import crack_sha256_hash
from Scripts.hash_algorithms.sha384 import crack_sha384_hash
from Scripts.hash_algorithms.sha512 import crack_sha512_hash

# Initialize colorama for colored output
colorama.init(autoreset=True)

# Dictionary mapping hash algorithm names to their respective functions
hash_algorithms = {
    "bcrypt": crack_bcrypt_hash,
    "md5": crack_md5_hash,
    "sha1": crack_sha1_hash,
    "sha224": crack_sha224_hash,
    "sha256": crack_sha256_hash,
    "sha384": crack_sha384_hash,
    "sha512": crack_sha512_hash,
}


def crack_hash(hash_algorithm, hash_str, wordlist, with_wordlist):
    """Crack a given hash using the specified algorithm."""
    if hash_algorithm in hash_algorithms:
        start_time = time.time()
        plain_text = hash_algorithms[hash_algorithm](
            hash_str=hash_str,
            wordlist=wordlist,
            with_wordlist=with_wordlist,
        )
        end_time = time.time()
        time_elapsed = end_time - start_time

        if plain_text:
            print(
                f"Password Found: {B.LIGHTRED_EX}{F.BLACK} {plain_text} {F.RESET}{B.RESET}"
            )
            print(f"Time elapsed: {time_elapsed:.1f}s")
        else:
            print("Password not found.")
    else:
        print(f"[*] Unsupported hash algorithm: {hash_algorithm}")


def commandline_args():
    """Handle command-line arguments to crack hashes."""
    if 0 < len(sys.argv) < 6:
        hash_algorithm = sys.argv[1]
        hash_str = sys.argv[2]
        wordlist = None
        with_wordlist = False

        if "--with-wordlist" in sys.argv:
            wordlist = sys.argv[3]
            with_wordlist = True

        crack_hash(hash_algorithm, hash_str, wordlist, with_wordlist)
    else:
        print(
            "[*] Usage: python3 main.py <hash_algo> '<hash_to_crack>' ['<wordlist_path>' --with-wordlist]"
        )


if __name__ == "__main__":
    # Check Python version requirement
    if sys.version_info[:2] < (3, 6):
        print(
            "Error Code U-2: This script requires Python 3.6 or higher! You are running {}.{}".format(
                sys.version_info[0], sys.version_info[1]
            )
        )
        sys.exit()

    try:
        commandline_args()
    except IndexError:
        print(
            "[*] Usage: python3 main.py <hash_algo> '<hash_to_crack>' ['<wordlist_path>' --with-wordlist]"
        )
        sys.exit()
