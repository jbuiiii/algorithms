import unittest
from src.z_algorithm import z_algorithm

class TestZAlgorithm(unittest.TestCase):

    def test_basic_repeating(self) -> None:
        txt = "aaaaaa"
        expected = [0, 5, 4, 3, 2, 1]
        actual = z_algorithm(txt=txt)
        self.assertEqual(expected, actual, "Test - Basic Repeating: Expected value, {expected}, does not match {actual}.")

    def test_no_matches(self) -> None:
        txt = "abcdef"
        expected = [0, 0, 0, 0, 0, 0]
        actual = z_algorithm(txt=txt)
        self.assertEqual(expected, actual, "Test - No Matches: Expected value, {expected}, does not match {actual}.")

    def test_alternating_chars(self) -> None:
        txt = "ababab"
        expected = [0, 0, 4, 0, 2, 0]
        actual = z_algorithm(txt=txt)
        self.assertEqual(expected, actual, "Test - Alternating Characters: Expected value, {expected}, does not match {actual}.")

    def test_single_char(self) -> None:
        txt = "a"
        expected = [0]
        actual = z_algorithm(txt=txt)
        self.assertEqual(expected, actual, "Test - Single Character: Expected value, {expected}, does not match {actual}.")

    def test_lab_case(self) -> None:
        txt = "abbabcabbabbababc"
        expected = [0, 0, 0, 2, 0, 0, 5, 0, 0, 5, 0, 0, 2, 0, 2, 0, 0]
        actual = z_algorithm(txt=txt)
        self.assertEqual(expected, actual, "Test - Lab Case: Expected value, {expected}, does not match {actual}.")
