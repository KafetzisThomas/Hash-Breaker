import os
import unittest
from Scripts.hash_algorithms.sha_hash import crack_sha_hash


class TestCrackSHA512Hash(unittest.TestCase):
    """Tests for cracking sha512 hash"""

    def setUp(self):
        self.current_directory = os.getcwd()
        self.hash_type = "sha512"
        self.hash = "1f40fc92da241694750979ee6cf582f2d5d7d28e18335de05abc54d0560e0f5302860c652bf08d560252aa5e74210546f369fbbbce8c12cfc7957b2652fe9a75"
        self.password_length = 1
        self.expected_result = "a"

    def test_crack_sha512_hash_with_wordlist(self):
        """Test if provided hash is equal to one of the words in the wordlist"""
        wordlist = f"{self.current_directory}/tests/wordlist_example.txt"
        with_wordlist = True

        result = crack_sha_hash(
            self.hash_type, self.hash, wordlist, self.password_length, with_wordlist
        )

        self.assertEqual(result, self.expected_result)

    def test_crack_sha512_hash_without_wordlist(self):
        """Test if provided hash is equal to the expected value"""
        wordlist = None
        with_wordlist = False

        result = crack_sha_hash(
            self.hash_type, self.hash, wordlist, self.password_length, with_wordlist
        )

        self.assertEqual(result, self.expected_result)


if __name__ == "__main__":
    unittest.main()
