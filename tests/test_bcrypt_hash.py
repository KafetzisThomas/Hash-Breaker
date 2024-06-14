import os
import unittest
from Scripts.hash_algorithms.bcrypt import crack_bcrypt_hash

hash = "$2b$12$.pdcdWnjEA/2GOvHfEfMkupP/BXSsdJjLs5Sh63E0B/5JG/YeB9cu"


class TestCrackBcryptHash(unittest.TestCase):
    """Tests for crack_bcrypt_hash() function"""

    def test_crack_bcrypt_hash_with_wordlist(self):
        """Test if provided hash is equal to one of the words in the wordlist"""
        current_directory = os.getcwd()
        wordlist = f"{current_directory}/tests/wordlist_example.txt"
        password_length = 1
        with_wordlist = True

        result = crack_bcrypt_hash(hash, wordlist, password_length, with_wordlist)
        expected_result = "a"

        self.assertEqual(result, expected_result)

    def test_crack_bcrypt_hash_without_wordlist(self):
        """Test if provided hash is equal to the expected value"""
        wordlist = None
        password_length = 1
        with_wordlist = False

        result = crack_bcrypt_hash(hash, wordlist, password_length, with_wordlist)
        expected_result = "a"

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
