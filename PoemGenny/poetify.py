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

    def append_string(self, prefix, suffix):
        """
        Method: append_string
        Description: appends a prefix and/or suffix to an existing StringMod object
        Parameters:
           prefix: a string
           suffix: a string
        Preconditions: none
        Postcondition: the StringMod object has been modified
        Returns: a string
        """
        self.chars = prefix + self.chars + suffix
        return self.chars

    def reduce_string(self, reduction):
        """
        Method: reduce_string
        Description: removes a substring from an existing StringMod object
        Parameters:
          reduction: a positive integer indicating character length to trim on both ends
        Preconditions: none
        Postcondition: the StringMod object has been modified
        Returns: a string
        """
        self.chars = self.chars[reduction:-reduction]
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

## END OF CLASS STRINGMOD ##

# test = StringMod('HazironYam')
# res = test.append_string('a', 'b')


import random
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"
# "https://www.rithmschool.com/blog"
# "http://quotes.toscrape.com"
# "http://books.toscrape.com"

def scrape(url):
    """
    Function: scrape
    Description: scrapes website, assembles text
    Parameters:
      url: a string, of a website address that can be safely scraped
    Returns: a list, of all text from a webpage
    """
    response     = requests.get(url)
    soup         = BeautifulSoup(response.text, 'html.parser')
    visible_text = soup.getText().lower()
    text         = visible_text.split()
    return text

text_list = scrape(url)


def clean(text_list):
    """
    Function: clean
    Description: tidies text scraped from a website, identifies types of words
    Parameters:
      text_list: a list of strings
    Returns: a tuple, containing 3 lists of StringMod objects:
        all webpage words
        potential adjectives (from all webpage words)
        potential verbs (from all webpage words)
        ...and the longest word (from all webpage words)
    """
    word_list = []
    adj_list  = []
    verb_list = []
    others_list = []    
    longest_word = "taco"
    
    for text_item in text_list:
        get_text = list([char for char in text_item if char.isalpha()])
        result   = "".join(get_text)
        if result not in word_list and len(result) != 0:
            word_list.append(result)

    for word in word_list:
        if len(word) > 3:            
            if word[-1] == "y":
                word_obj = StringMod(word)
                adj_list.append(word_obj)
            elif word[-2:] == "ed" or word[-3:] == "ing":
                word_obj = StringMod(word)
                verb_list.append(word_obj)
            elif len(word) > len(longest_word):
                  longest_word = word
            else:
                word_obj = StringMod(word)
                others_list.append(word_obj)
        else:
            word_obj = StringMod(word)
            others_list.append(word_obj)
       
    longest_word = StringMod(longest_word)
    return others_list, adj_list, verb_list, longest_word

(others_list, adj_list, verb_list, longest_word) = clean(text_list)

# print("Website text minus potential adjectives/verbs: ")
# for item in others_list:
#     print(item) 
# print("Potential adjectives: ")
# for item in adj_list:
#     print(item)
# print("Potential verbs: ")
# for item in verb_list:
#     print(item)
# print("Longest word: ", longest_word)


def modify_words(others_list, adj_list, verb_list, longest_word):
    """
    Function: build_poem
    Description: modifies words for use in poem
    Parameters:
      others_list:  a list, of StringMod objects
      adj_list:     a list, of StringMod objects ending in "y"
      verb_list:    a list, of StringMod objects ending in "ed" or "ing"
      longest_word: a StringMod object
    Returns: a list, of modified words
    """
    
    poem_depot = []
    words = random.sample(others_list, 3)
    adjs = random.sample(adj_list, 3)
    verbs = random.sample(verb_list, 3)
    counter = 1
    
    for word in words:
        word.append_string("", random.choice(["!", "?"]))
        poem_depot.append(word)
        
    for word in adjs:
        word.append_string("'", "'")
        poem_depot.append(word)
        
    for word in verbs:
        word.append_string(word.get_string()[0:3] + "-" + word.get_string()[0:4] + "-", "")
        poem_depot.append(word)

    while counter < len(longest_word.get_string()) + 3:
        res = StringMod(longest_word.reduce_string(1))
        res.append_string("...", "...")
        poem_depot.append(res)
        counter += 1
    
    return poem_depot
    
poem_depot = modify_words(others_list, adj_list, verb_list, longest_word)  
for item in poem_depot:
    print(item) 