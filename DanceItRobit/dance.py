# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 09:14:43 2022

@author: nari2
"""


robotToggle = 0

if robotToggle == 1:
    from botcore import *
    from time import sleep

# Class: Note
# Description: represents a note with fixed pitch (100-3000 Hz) of n duration
class Note(object):

    # Method: __init__
    # Description: constructor
    # Parameters:
    #   name: a string
    # Precondition: none
    # Postcondition: the data attributes are initialized
    # Returns: a newly created object of type Note
    def __init__(self, name):
        # Data attributes: 
        #   name: a string 
        self.name = name

    # Method: getName
    # Description: retrieves the Note name
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: a string 
    def getName(self):
        return self.name

    # Method: __str__
    # Description: method to define how to cast a Note object into a string
    # Parameters: none
    # Precondition: none
    # Postcondition: no change
    # Returns: a string whose value is the Note name    
    def __str__(self):
        return self.name 

    
# Class: Scale
# Description: maps connections between notes and their frequencies
class Scale(object):

    # Method: __init__
    # Description: constructor
    # Parameters: none
    # Precondition: none
    # Postcondition: The data attributes are initialized
    # Returns: A newly created object of type Scale
    def __init__(self):
        # Data attribute:
        #   notes: a dictionary, whose keys are objects of type Note, & whose values are frequencies
        self.notes = {}

    # Method: addNote
    # Description: add a note
    # Parameters:
    #   Note: a Note object
    # Precondition:
    #   This note hasn't already been added previously
    # Postcondition:
    #   The Note object has been added 
    # Returns: None
    def addNote(self, Note):   
        # add an instance of type Note as dictionary key, with empty list as value
        if Note in self.notes:
            raise ValueError('Duplicate note')
        else:
            self.notes[Note] = [] 

    # Method: __str__
    # Description: Defines how to cast an object of class Scale into a string
    # Parameters: none
    # Precondition: none
    # Postcondition: no change
    # Returns: a string        
    def __str__(self):
        result = ''
        # iterate through each source object key in the notes dictionary
        for note in self.notes:
            result = result + note.getName() + '\n'
        # slice to omit final newline
        return result[:-1]
            
# Function: buildNotes 
# Description: generates Note objects
# Parameters: 
#   NoteType: a class type 
#   freq: an integer, representing pitch (Hz)
#   dur: a float, representing note duration (default of 1.0 second)
# Returns: a list of Note objects
def buildNotes(NoteType):
    # initialize nt to a new instance of class NoteType
    nt = NoteType()
    # for each string in this tuple...
    for name in ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']:   
        # create a Note object
        noteObject = Note(name) 
        # call method addNote (belonging to nt) passing each note object as argument
        nt.addNote(noteObject)    
    return nt
            
notes = (buildNotes(Scale))
print(notes)


# note_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
# freq_list = [16.35, 17.32, 18.35, 19.45, 20.60, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87]
# dur = 1.0




# Function: playNotes
# Description: plays a list of Note objects' frequencies, with Note object duration
# Parameters: 
#   notes: a list of Note objects
# Preconditions: none 
# Postcondition: no change
# Returns: emitted Hz of dur duration       
def playNotes(notes):
    if robotToggle == 1:
        for note in notes:
            spkr.pitch(round(note.getFreq()))
            sleep(note.dur)
            spkr.off()
              # articulation gap
            sleep(0.05)
#playNotes(notes)
# motif = [notes[30], notes[32], notes[20]]
# playNotes(motif)


# for note in notes:
#     print(note.getNote())
#     print(note.getFreq())

# noteObj = Note('F', 349, 1.0)
# print(noteObj.getFreq()) 
# noteObj.playNote()


