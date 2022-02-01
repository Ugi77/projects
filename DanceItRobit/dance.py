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
    #   n: a string, representing note name
    #   f: a float, representing pitch
    #   d: a float, representing time elapse of pitch
    #   t: an integer, representing tempo?
    # Precondition: none
    # Postcondition: the data attributes are initialized
    # Returns: a newly created object of type Note
    def __init__(self, n, f, d):
        # Data attributes: 
        #   n: a string, representing note name
        #   f:  an float, representing pitch
        #   d:  a float, representing time elapse of pitch
        #   t:       
        self.name = n
        self.freq = f
        self.dur = d
        #self.t = tempo

    # Method: getNote
    # Description: retrieves a Note object's name (note and octave position)
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: a string        
    def getNote(self):
        return self.name

    # Method: getFreq
    # Description: retrieves a Note object's frequency 
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: a float        
    def getFreq(self):
        return self.freq

    # Method: getDur
    # Description: retrieves a Note object's duration 
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: a float        
    def getDur(self):
        return self.dur
    
    # Method: playNote
    # Description: plays a Note object's frequency, with Note object duration
    # Parameters: 
    #   Note: a Note object
    # Preconditions: none 
    # Postcondition: no change
    # Returns: emitted Hz of dur duration       
    def playNote(self, Note):
        if robotToggle == 1:
            spkr.pitch(self.getFreq())
            sleep(self.dur)
            spkr.off()
              # articulation gap
            sleep(0.05)

    # # Method: playNotes
    # # Description: plays a list of Note objects' frequencies, with Note object duration
    # # Parameters: 
    # #   notes: a list of Note objects
    # # Preconditions: none 
    # # Postcondition: no change
    # # Returns: emitted Hz of dur duration       
    # def playNotes(self, notes):
    #     if robotToggle == 1:
    #         for note in notes:
    #             spkr.pitch(self.getFreq())
    #             sleep(self.dur)
    #             spkr.off()
    #               # articulation gap
    #             sleep(0.05)
            
    # Method: __str__
    # Description: Defines how to cast the objects of class Note into a string  
    # Parameters: none
    # Precondition: none
    # Postcondition: no change
    # Returns: a string    
    def __str__(self):
        return self.name + ': <' + str(self.freq) + '>'

# Function: buildScaleNames
# Description: generates a list of note names
# Parameters: 
#   note: a list of strings, representing the note name
# Returns: a list of strings
def buildScaleNames(protoScale):
    scaleNames = []
    counter = 1
    while counter <= 6:
        for element in protoScale:
           scaleNames.append(element + str(counter))
        counter += 1
    return scaleNames
    

# # Function: buildScale 
# # Description: takes in 2 lists of the same length, and generates a list of Note objects
# # Parameters: 
# #   note: a list of strings, representing the note name
# #   freq: an integer, representing pitch (Hz)
# #   dur: a float, representing note duration (default of 1.0 second)
# # Returns: a list of Note objects
# def buildScale(note, freq, dur):
#     counter = 0
#     notes = []
#     octave = 1
#     freq_increment = 2
#     while octave <= 6:
#         for i in range(len(protoScale)):
#             # create a Note object with a list element from note, freq at iterated index position
#             scaleNames[counter] = Note(protoScale[i] + str(octave), (freq_list[i] * freq_increment), dur)
#             print(scaleNames[counter])
#             # add each Note object to the notes list
#             # notes.append(scaleNames[counter])
#         octave += 1
#         freq_increment *= 2
#         counter += 1
#     return notes  
# buildScale(protoScale, freq_list, dur)

protoScale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
scaleNames = buildScaleNames(protoScale)

freq_list = [16.35, 17.32, 18.35, 19.45, 20.60, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87]
dur = 1.0
counter = 0
notes = []
octave = 1
freq_increment = 2
for i in range(len(protoScale)):
    # create a Note object with a list element from note, freq at iterated index position
    scaleNames[counter] = Note(protoScale[i] + str(octave), (freq_list[i] * freq_increment), dur)
    print(scaleNames[counter])
    # add each Note object to the notes list
    # notes.append(scaleNames[counter])
octave += 1
freq_increment *= 2
counter += 1
print(scaleNames[counter].getFreq()) 

# Function: playScale
# Description: plays the list of Note objects' frequencies, with Note object duration
# Parameters: 
#   notes: a list of Note objects
# Preconditions: none 
# Postcondition: no change
# Returns: emitted Hz of dur duration       
def playScale(notes):
    if robotToggle == 1:
        for note in notes:
            spkr.pitch(round(note.getFreq()))
            sleep(note.dur)
            spkr.off()
              # articulation gap
            sleep(0.05)
#playScale(notes)
# motif = [notes[30], notes[32], notes[20]]
# playScale(motif)

# # Function: buildMotif
# # Description: builds a list of Note objects
# # Parameters: 
# #   motif: a string, of note names
# # Preconditions: the function buildScale has been run 
# # Postcondition: no change
# # Returns: none       
# def buildMotif(motif):
#     motif_obj = []
#     counter = 0
#     #if robotToggle == 1:
#     while counter < len(motif):
#         for note in notes:
#             if note.getNote() == motif[counter]:
#                 motif_obj.append(note)
#             else:
#                 continue
#         counter += 1
# motif = ['C4', 'G5']
# print(buildMotif(motif))

# Function: playMotif
# Description: plays a list of Note objects
# Parameters: 
#   motif: a list of Note objects
# Preconditions: the function buildScale has been run 
# Postcondition: no change
# Returns: emitted Hz of dur duration 
        # for note in motif_obj:
        #     spkr.pitch(round(note.getFreq()))
        #     sleep(note.dur)
        #     spkr.off()
        #       # articulation gap
        #     sleep(0.05)
        

# for note in notes:
#     print(note.getNote())
#     print(note.getFreq())

# noteObj = Note('F', 349, 1.0)
# print(noteObj.getFreq()) 
# noteObj.playNote()


# notes = []
# octave = 1
# freq_increment = 2
# while octave < 6:
#     for i in range(len(note_list)):
#         # create a Note object with a list element from note, freq at the iterated index position
#         note = [note_list[i] + str(octave), (freq_list[i] * freq_increment)]
#         # add each item to the notes list
#         notes.append(note)
#     octave += 1
#     freq_increment *= 2

# print(notes)



