import os
import unittest
from Scripts.hash_algorithms.sha384 import crack_sha384_hash

hash = "54a59b9f22b0b80880d8427e548b7c23abd873486e1f035dce9cd697e85175033caa88e6d57bc35efae0b5afd3145f31"

class TestCrackSHA384Hash(unittest.TestCase):
    """Tests for crack_sha384_hash() function"""

    def test_crack_sha384_hash_with_wordlist(self):
        """Test if provided hash is equal to one of the words in the wordlist"""
        current_directory = os.getcwd()
        wordlist = f"{current_directory}/tests/wordlist_example.txt"
        password_length = 1
        with_wordlist = True

        result = crack_sha384_hash(hash, wordlist, password_length, with_wordlist)
        expected_result = "a"

        self.assertEqual(result, expected_result)

    def test_crack_sha384_hash_without_wordlist(self):
        """Test if provided hash is equal to the expected value"""
        wordlist = None
        password_length = 1
        with_wordlist = False

        result = crack_sha384_hash(hash, wordlist, password_length, with_wordlist)
        expected_result = "a"

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
