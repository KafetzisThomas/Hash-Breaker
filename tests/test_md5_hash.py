import os
import unittest
from Scripts.hash_algorithms.md5 import crack_md5_hash

hash = "0cc175b9c0f1b6a831c399e269772661"

class TestCrackMD5Hash(unittest.TestCase):
    """Tests for crack_md5_hash() function"""

    def test_crack_md5_hash_with_wordlist(self):
        """Test if provided hash is equal to one of the words in the wordlist"""
        current_directory = os.getcwd()
        wordlist = f"{current_directory}/tests/wordlist_example.txt"
        password_length = 1
        with_wordlist = True

        result = crack_md5_hash(hash, wordlist, password_length, with_wordlist)
        expected_result = "a"

        self.assertEqual(result, expected_result)

    def test_crack_md5_hash_without_wordlist(self):
        """Test if provided hash is equal to the expected value"""
        wordlist = None
        password_length = 1
        with_wordlist = False

        result = crack_md5_hash(hash, wordlist, password_length, with_wordlist)
        expected_result = "a"

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
