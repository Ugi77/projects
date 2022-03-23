# -*- coding: utf-8 -*-

"""
Author: Dima (Ugi77)
Description: a class to modify and store strings
"""


class StringMod:
    """
    Class: StringMod
    Description: represents a StringMod object and functionality to process, store strings
    """
    def __init__(self, chars):
        """
        Method: __init__
        Description: constructor
        Parameters:
           chars: a string
        Precondition: none
        Postcondition: the data attributes are initialized
        Returns: a newly created object of type StringMod
            Data attributes:
               chars: a string
        """
        self.chars = chars

    def append_string(self, addon):
        """
        Method: append_string
        Description: appends a new string to an existing StringMod object
        Parameters:
           addon: a string
        Preconditions: none
        Postcondition: the StringMod object has been modified
        Returns: a StringMod object
        """
        self.chars = self.chars + addon
        return self.chars

    def remove_string(self, reduce_start, reduce_end):
        """
        Method: remove_string
        Description: removes a substring from an existing StringMod object
        Parameters:
          reduce_start: a positive integer indicating starting index position
          reduce_end: a positive integer indicating ending index position
        Preconditions: none
        Postcondition: the StringMod object has been modified
        Returns: the remaining StringMod object
        """
        self.chars = self.chars[0:reduce_start] + self.chars[reduce_end:]
        return self.chars

    def mirror_string(self):
        """
        Method: mirror_string
        Description: mirrors a StringMod object
        Parameters: none
        Preconditions: none
        Postcondition: the StringMod object has been modified
        Returns: a StringMod object
        """
        self.chars = self.chars.lower()
        result = ''
        for char in self.chars:
            result = char + result
        self.chars = result
        return self.chars

    def is_palindrome(self):
        """
        Method: is_palindrome
        Description: verifies if a StringMod object is a palindrome
        Parameters: none
        Preconditions: none
        Postcondition: no change
        Returns: a Boolean, True if a StringMod object is a palindrome, False otherwise
        """
        if len(StringMod.get_string(self)) == 1:
            return True
        string1 = StringMod.get_string(self)
        StringMod.mirror_string(self)
        string2 = StringMod.get_string(self)
        if string1 == string2:
            return True
        return False

    def get_string(self):
        """
        Method: get_string
        Description: retrieves a StringMod object's string
        Parameters: none
        Preconditions: none
        Postcondition: no change
        Returns: a string
        """
        return self.chars

    def save_string(self, filename):
        """
        Method: save_string
        Description: saves string content to a text file
        Parameters:
          filename: a text file
        Preconditions: none
        Postcondition: no change
        Returns: None
        """
        with open(filename, 'a') as file:
            file.write(self.chars)

    def load_string(self, filename):
        """
        Method: load_string
        Description: loads string content from a file
        Parameters:
          filename: a text file
        Preconditions: none
        Postcondition: the StringMod object has been modified
        Returns: None
        """
        with open(filename) as file:
            self.chars = file.read()
            
    def __str__(self):
        """
        Method: __str__
        Description: defines how to cast StringMod objects into a string
        Parameters: none
        Precondition: none
        Postcondition: no change
        Returns: a string
        """
        return self.chars
