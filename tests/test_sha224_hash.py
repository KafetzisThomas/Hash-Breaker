import os
import unittest
from Scripts.hash_algorithms.sha224 import crack_sha224_hash

hash = "abd37534c7d9a2efb9465de931cd7055ffdb8879563ae98078d6d6d5"

class TestCrackSHA224Hash(unittest.TestCase):
    """Tests for crack_sha224_hash() function"""

    def test_crack_sha224_hash_with_wordlist(self):
        """Test if provided hash is equal to one of the words in the wordlist"""
        current_directory = os.getcwd()
        wordlist = f"{current_directory}/tests/wordlist_example.txt"
        password_length = 1
        with_wordlist = True

        result = crack_sha224_hash(hash, wordlist, password_length, with_wordlist)
        expected_result = "a"

        self.assertEqual(result, expected_result)

    def test_crack_sha224_hash_without_wordlist(self):
        """Test if provided hash is equal to the expected value"""
        wordlist = None
        password_length = 1
        with_wordlist = False

        result = crack_sha224_hash(hash, wordlist, password_length, with_wordlist)
        expected_result = "a"

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
