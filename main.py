#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Bcrypt-Breaker (https://github.com/KafetzisThomas/Bcrypt-Breaker)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

# Import built-in modules
import platform, os, sys, time

# Import module files
from Scripts.bcrypt import crack_bcrypt_hash

# Import other (third-party) modules
import colorama
from art import text2art
from colorama import Fore as F, Back as B
colorama.init(autoreset=True)


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
        hash_input = input("\nEnter Hash: ").strip()
        start = time.time()
        password = crack_bcrypt_hash(hash_input)
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
