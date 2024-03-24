<h1 align="center">Hash-Breaker</h1>

__What Is This?__ - Allows you to crack hashes with or without wordlist.

__How to Download__: Open the terminal on your machine and type the following command:

```
git clone https://github.com/KafetzisThomas/Hash-Breaker.git
```

Use [pip](https://pip.pypa.io/en/stable) to install the required packages:

```
pip install -r requirements.txt
```

## Features

* Supports: Bcrypt, MD5, SHA1, SHA224, SHA256, SHA384, SHA512
* Dynamic password generation: Generate all possible combinations of characters until a match is found
* Dictionary support
* Command-Line Arguments

## Usage Notes - READ THIS

1. To use this script, run the ```main.py``` file in your console and that's it!

   __Windows:__
   ``` python main.py ```
   __Mac/Linux:__
   ``` ./main.py ```
   * __For Mac/Linux:__ Make sure you make it executable with the following command:
      ``` chmod +x main.py ```

# Command-Line Arguments

When running the script with command-line arguments, ensure that you use the following supported options:

``` python3 main.py <hash_algorithm> '<hash_str>' '<wordlist_path>' --with-wordlist ```

Supported Arguments:
* `<hash_algorithm>`: Specify the hash algorithm to use for cracking. Choose from Bcrypt, MD5, SHA1, SHA224, SHA256, SHA384, or SHA512.
* `<hash_str>`: Provide the hash string that you want to crack using the selected hash algorithm.
* `<wordlist_path>`: (Optional) Specify the path to a custom wordlist file for dictionary-based cracking.
* `--with-wordlist`: (Optional) Include this flag to enable dictionary-based cracking using the provided wordlist.

**Note**: The arguments `<wordlist_path>` and `--with-wordlist` are optional. You can choose to use them based on your specific cracking requirements.

# Run Tests

Navigate to the **root directory** of the repository where the testing files are stored and run the following command to run all tests at once:

``` python3 -m unittest discover tests ```

# Disclaimer: Educational Use Only

**Hash-Breaker** is an educational tool designed for learning and understanding cryptographic concepts related to hash functions and password security. It is NOT intended for malicious activities, unauthorized access, or any form of unethical use.

By accessing and using Hash-Breaker, you acknowledge and agree to the terms outlined in this disclaimer. The repository owner and contributors are not responsible for any misuse, damage, or legal consequences resulting from the use of this tool.

Please use Hash-Breaker responsibly and for educational purposes only.
