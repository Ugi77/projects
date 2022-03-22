# -*- coding: utf-8 -*-

"""
Author: Dima (Ugi77)
Description: testing components of the Pitch, Motif, and Dance classes
"""

import unittest
import winsound
from dance import Pitch
from dance import Motif
from dance import Dance


class PitchTests(unittest.TestCase):
    """
    Class: PitchTests
    Description: test cases for Class Pitch
    """
    def setUp(self):
        self.pitchy = Pitch("toot", 440.0)
        self.pitchy2 = Pitch("hmm", 256.0)
        
    def test_init(self):
        """pitchy should have a name, frequency, and increment position number"""
        self.assertEqual(self.pitchy.name, "toot")
        self.assertEqual(self.pitchy.freq, 440.0)
        self.assertEqual(self.pitchy.pos + 1, self.pitchy2.pos)
        
    def test_get_name(self):
        """get_name should return a Pitch object string (name)"""
        self.assertEqual(self.pitchy.get_name(), "toot")
        
    def test_get_pos(self):
        """get_pos should return a Pitch object integer (position)"""
        self.assertEqual(self.pitchy.pos, self.pitchy.get_pos())
        #self.assertEqual(self.pitchy2.get_pos(), -35)

    def test_get_freq(self):
        """get_freq should return a Pitch object float (frequency)"""
        self.assertEqual(self.pitchy.get_freq(), 440.0)   


class MotifTests(unittest.TestCase):
    """
    Class: MotifTests
    Description: test cases for Class Motif
    """
    def setUp(self):
        # self.motify = Motif()
        pass
        
    def test_init(self):
        """motify should have a motif_list attribute, which is an empty list"""
        #self.assertTrue(isinstance(self.motify, list))
        pass
        
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
        # self.dancy = Dance(self.motify, "twirl")
        pass

    def test_init(self):
        """dancy should have a Motif object and string"""
        pass
        
    def test_dance_it(self):
        """dance_it should """
        pass


if __name__ == "__main__":
    unittest.main()
