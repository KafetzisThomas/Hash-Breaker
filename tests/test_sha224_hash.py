import os
import unittest
from Scripts.hash_algorithms.sha_hash import crack_sha_hash


class TestCrackSHA224Hash(unittest.TestCase):
    """Tests for cracking sha224 hash"""

    def setUp(self):
        self.current_directory = os.getcwd()
        self.hash_type = "sha224"
        self.hash = "abd37534c7d9a2efb9465de931cd7055ffdb8879563ae98078d6d6d5"
        self.password_length = 1
        self.expected_result = "a"

    def test_crack_sha224_hash_with_wordlist(self):
        """Test if provided hash is equal to one of the words in the wordlist"""
        wordlist = f"{self.current_directory}/tests/wordlist_example.txt"
        with_wordlist = True

        result = crack_sha_hash(
            self.hash_type, self.hash, wordlist, self.password_length, with_wordlist
        )

        self.assertEqual(result, self.expected_result)

    def test_crack_sha224_hash_without_wordlist(self):
        """Test if provided hash is equal to the expected value"""
        wordlist = None
        with_wordlist = False

        result = crack_sha_hash(
            self.hash_type, self.hash, wordlist, self.password_length, with_wordlist
        )

        self.assertEqual(result, self.expected_result)


if __name__ == "__main__":
    unittest.main()
