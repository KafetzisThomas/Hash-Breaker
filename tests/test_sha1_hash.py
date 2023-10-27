import os
import unittest
from Scripts.hash_algorithms.sha1 import crack_sha1_hash

hash = "86f7e437faa5a7fce15d1ddcb9eaeaea377667b8"

class TestCrackSHA1Hash(unittest.TestCase):
    """Tests for crack_sha1_hash() function"""

    def test_crack_sha1_hash_with_wordlist(self):
        """Test if provided hash is equal to one of the words in the wordlist"""
        current_directory = os.getcwd()
        wordlist = f"{current_directory}/tests/wordlist_example.txt"
        password_length = 1
        with_wordlist = True

        result = crack_sha1_hash(hash, wordlist, password_length, with_wordlist)
        expected_result = "a"

        self.assertEqual(result, expected_result)

    def test_crack_sha1_hash_without_wordlist(self):
        """Test if provided hash is equal to the expected value"""
        wordlist = None
        password_length = 1
        with_wordlist = False

        result = crack_sha1_hash(hash, wordlist, password_length, with_wordlist)
        expected_result = "a"

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
