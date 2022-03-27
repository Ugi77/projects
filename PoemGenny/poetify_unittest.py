# -*- coding: utf-8 -*-

"""
Author: Dima (Ugi77)
Description: testing components of the StringMod class
"""

import unittest
from poetify import StringMod

class StringModTests(unittest.TestCase):
    """
    Class: StringModTests
    Description: test cases for Class StringMod
    """
    def setUp(self):
        self.stringy = StringMod("hello")

    def test_append_string(self):
        """append_string should return a string with the provided suffix and prefix"""
        test_string = self.stringy.append_string("why ", " there")
        self.assertIn("hello", test_string)
        self.assertEqual("why hello there", test_string)

    def test_reduce_string(self):
        """reduce_string should return a string with the
        provided character length removed at the beginning and end"""
        test_string = self.stringy.reduce_string(1)
        self.assertNotIn("hello", test_string)
        self.assertEqual("ell", test_string)

    def test_mirror_string(self):
        """mirror_string should return a mirror of a string"""
        test_string = self.stringy.mirror_string()
        self.assertEqual("olleh", test_string)

    def test_is_not_palindrome(self):
        """is_palindrome should return False if a string is not a palindrome"""
        test_string = self.stringy.is_palindrome()
        self.assertEqual(False, test_string)

    def test_is_palindrome(self):
        """is_palindrome should return True if a string is a palindrome"""
        self.stringy = StringMod("tacocat")
        test_string = self.stringy.is_palindrome()
        self.assertEqual(True, test_string)

    def test_get_string(self):
        """get_string should return a StringMod object string"""
        self.assertEqual(str(self.stringy), self.stringy.get_string())

if __name__ == "__main__":
    unittest.main()
