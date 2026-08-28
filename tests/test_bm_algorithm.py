import unittest
from src.bm_algorithm import bm, create_bc_array, create_gs_array, create_mp_array

class TestBMAlgorithm(unittest.TestCase):

    # Smaller case tests
    def test_bc_array(self):
        pat = "yzzyzxyzzyz"
        expected = [
            [-1, -1, -1, -1, -1, 5, 5, 5, 5, 5, 5],
            [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9], 
            [-1, 1, 2, 2, 4, 4, 4, 7, 8, 8, 10]
        ]
        actual = create_bc_array(pat)
        self.assertEqual(expected, actual)

    def test_gs_array(self):
        pat = "abaaabacbaabaaab"
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 12, 2, 9, 15]
        actual = create_gs_array(pat)
        self.assertEqual(expected, actual)

    def test_mp_array(self):
        pat = "abaaabacbaabaaab"
        expected = [15, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 2, 0, 0]
        actual = create_mp_array(pat)
        self.assertEqual(expected, actual)

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
    