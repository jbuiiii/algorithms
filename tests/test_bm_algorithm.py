import unittest
from src.bm_algorithm import bm

class TestBMAlgorithm(unittest.TestCase):

    # Standard Cases
    def test_exact_match(self):
        txt = "abcde"
        pat = "abcde"
        expected = [0]
        actual = bm(txt, pat)
        self.assertEqual(actual, expected, "Test - Exact Match: Expected value {expected}, does not match actual value {actual}")

    def test_single_match(self):
        txt = "abacadabra"
        pat = "cad"
        expected = [3]
        actual = bm(txt, pat)
        self.assertEqual(actual, expected, "Test - Single Match: Expected value {expected}, does not match actual value {actual}")

    def test_multiple_match(self):
        txt = "ABAAAABAACD"
        pat = "ABA"
        expected = [0, 5]
        actual = bm(txt, pat)
        self.assertEqual(actual, expected, "Test - Multiple Match: Expected value {expected}, does not match actual value {actual}")

    # Edge/Boundary Cases
    def test_start_match(self):
        txt = "abcdefg"
        pat = "abc"
        expected = [0]
        actual = bm(txt, pat)
        self.assertEqual(actual, expected, "Test - Start Match: Expected value {expected}, does not match actual value {actual}")

    def test_end_match(self):
        txt = "abcdefg"
        pat = "efg"
        expected = [4]
        actual = bm(txt, pat)
        self.assertEqual(actual, expected, "Test - End Match: Expected value {expected}, does not match actual value {actual}")

    def test_no_match(self):
        txt = "abcdefg"
        pat = "xyz"
        expected = []
        actual = bm(txt, pat)
        self.assertEqual(actual, expected, "Test - No Match: Expected value {expected}, does not match actual value {actual}")

    def test_pat_long(self):
        txt = "abc"
        pat = "abcd"
        expected = []
        actual = bm(txt, pat)
        self.assertEqual(actual, expected, "Test - Pattern Too Long: Expected value {expected}, does not match actual value {actual}")

    # Lab Examples
    