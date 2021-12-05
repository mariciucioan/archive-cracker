import unittest

from sample.cracker import brute_force_attack_multi_thread, dictionary_attack
from sample.utils import get_test

brute_1 = 'test pwd (a).zip'
brute_2 = 'test pwd (1B).zip'
dictionary_1 = 'test pwd (fireball).zip'
dictionary_2 = 'test pwd (japoniaaaa).zip'
dictionary = 'test_dictionary.txt'

class TestCrack(unittest.TestCase):
    def test1_brute(self):
        test_file = get_test(brute_1)
        self.assertEqual(brute_force_attack_multi_thread(test_file), 'a', "Password should be 'a'")

    def test2_brute(self):
        test_file = get_test(brute_2)
        self.assertEqual(brute_force_attack_multi_thread(test_file), '1B', "Password should be '1B'")

    def test1_dictionary(self):
        test_file = get_test(dictionary_1)
        test_dictionary = get_test(dictionary)
        self.assertEqual(dictionary_attack(test_file, test_dictionary), 'fireball', "Password should be 'fireball'")

    def test2_dictionary(self):
        test_file = get_test(dictionary_2)
        test_dictionary = get_test(dictionary)
        self.assertEqual(dictionary_attack(test_file, test_dictionary), None, "Password should return None")

if __name__ == '__main__':
    unittest.main()

# Ran 4 tests in 53.510s
#
# OK