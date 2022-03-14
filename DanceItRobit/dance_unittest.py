# -*- coding: utf-8 -*-

"""
Author: Dima (Ugi77)
Description: testing components of the Pitch, Motif, and Dance classes
"""

import unittest
from dance import Pitch
from dance import Motif
from dance import Dance

class PitchTests(unittest.TestCase):
    """
    Class: PitchTests
    Description: test cases for Class Pitch
    """
    def set_up(self):
        self.pitchy = Pitch("testNote", 440.0)

    def test_get_name(self):
        """get_name should return a Pitch object string (name)"""
        self.assertEqual(str(self.pitchy), self.pitchy.get_name())

    def test_get_pos(self):
        """get_pos should return a Pitch object string (position)"""
        pass

    def test_get_freq(self):
        """get_freq should return a Pitch object float (frequency)"""
        pass
    
    def test_play_pitch(self):
        """play_pitch should emit a Pitch object frequency"""
        pass


class MotifTests(unittest.TestCase):
    """
    Class: MotifTests
    Description: test cases for Class Motif
    """
    def setUp(self):
        self.motify = Motif()

    def test_init(self):
        """motify should have a motif_list attribute, which is an empty list"""
        self.assertTrue(isinstance(self.motify, list))
        
    def test_build_motif(self):
        """build_motif should build a motif"""
        pass

    def test_get_names(self):
        """get_names should return Pitch object names in a Motif """
        pass

    def test_play_motif(self):
        """play_motif should emit a Motif object frequencies/durations"""
        pass
    
class DanceTests(unittest.TestCase):
    """
    Class: DanceTests
    Description: test cases for Class Dance
    """
    def setUp(self):
        self.dancy = Dance(self.motify, "twirl")

    def test_init(self):
        """dancy should have a Motif object and string"""
        pass
        
    def test_dance_it(self):
        """dance_it should """
        pass


if __name__ == "__main__":
    unittest.main()
