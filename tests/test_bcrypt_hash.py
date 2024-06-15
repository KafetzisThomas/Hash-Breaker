import os
import unittest
from Scripts.hash_algorithms.bcrypt import crack_bcrypt_hash


class TestCrackBcryptHash(unittest.TestCase):
    """Tests for cracking bcrypt hash"""

    def setUp(self):
        self.current_directory = os.getcwd()
        self.hash = "$2b$12$.pdcdWnjEA/2GOvHfEfMkupP/BXSsdJjLs5Sh63E0B/5JG/YeB9cu"
        self.password_length = 1
        self.expected_result = "a"

    def test_crack_bcrypt_hash_with_wordlist(self):
        """Test if provided hash is equal to one of the words in the wordlist"""
        wordlist = f"{self.current_directory}/tests/wordlist_example.txt"
        with_wordlist = True

        result = crack_bcrypt_hash(
            self.hash, wordlist, self.password_length, with_wordlist
        )

        self.assertEqual(result, self.expected_result)

    def test_crack_bcrypt_hash_without_wordlist(self):
        """Test if provided hash is equal to the expected value"""
        wordlist = None
        with_wordlist = False

        result = crack_bcrypt_hash(
            self.hash, wordlist, self.password_length, with_wordlist
        )

        self.assertEqual(result, self.expected_result)


if __name__ == "__main__":
    unittest.main()
