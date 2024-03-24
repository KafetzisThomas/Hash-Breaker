#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys, time

from Scripts.hash_algorithms.bcrypt import crack_bcrypt_hash
from Scripts.hash_algorithms.md5 import crack_md5_hash
from Scripts.hash_algorithms.sha1 import crack_sha1_hash
from Scripts.hash_algorithms.sha224 import crack_sha224_hash
from Scripts.hash_algorithms.sha256 import crack_sha256_hash
from Scripts.hash_algorithms.sha384 import crack_sha384_hash
from Scripts.hash_algorithms.sha512 import crack_sha512_hash
from colorama import Fore as F, Back as B

def command_line_arguments(hash_algorithm):
    hash_algorithms = {
        "bcrypt": crack_bcrypt_hash,
        "md5": crack_md5_hash,
        "sha1": crack_sha1_hash,
        "sha224": crack_sha224_hash,
        "sha256": crack_sha256_hash,
        "sha384": crack_sha384_hash,
        "sha512": crack_sha512_hash
    }

    try:
        if sys.argv[1] == hash_algorithm:
            hash_str = sys.argv[2]
            wordlist = None
            with_wordlist = False
            if "--with-wordlist" in sys.argv:
                wordlist = sys.argv[3]
                with_wordlist = True
            start = time.time()
            plain_text = hash_algorithms[hash_algorithm](hash_str=hash_str, wordlist=wordlist, with_wordlist=with_wordlist)
            end = time.time()
            time_elapsed = end - start
            if plain_text:
                print(f"Password Found: {B.LIGHTRED_EX}{F.BLACK} {plain_text} {F.RESET}{B.RESET}")
                print(f"Time elapsed: {time_elapsed:.1f}s")
            sys.exit()
    except IndexError:
        pass
