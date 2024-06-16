import os
import unittest
from unittest.mock import patch
from Scripts.hash_algorithms.sha_hash import crack_sha_hash


class TestCrackSHA1Hash(unittest.TestCase):
    """Tests for cracking sha1 hash"""

    def setUp(self):
        self.patcher = patch("builtins.print")
        self.mock_print = self.patcher.start()
        self.current_directory = os.getcwd()
        self.hash_type = "sha1"
        self.hash = "86f7e437faa5a7fce15d1ddcb9eaeaea377667b8"
        self.password_length = 1
        self.expected_result = "a"

    def tearDown(self):
        self.patcher.stop()

    def test_crack_sha1_hash_with_wordlist(self):
        """Test if provided hash is equal to one of the words in the wordlist"""
        wordlist = f"{self.current_directory}/tests/wordlist_example.txt"
        with_wordlist = True

        result, _ = crack_sha_hash(
            self.hash_type, self.hash, wordlist, self.password_length, with_wordlist
        )

        self.assertEqual(result, self.expected_result)

    def test_crack_sha1_hash_without_wordlist(self):
        """Test if provided hash is equal to the expected value"""
        wordlist = None
        with_wordlist = False

        result, _ = crack_sha_hash(
            self.hash_type, self.hash, wordlist, self.password_length, with_wordlist
        )

        self.assertEqual(result, self.expected_result)


if __name__ == "__main__":
    unittest.main()
