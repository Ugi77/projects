# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 09:14:43 2022

@author: nari2
"""

# Function: buildNoteRepo
# Description: maps note names to frequencies (Hz)
# Parameters: 
#   note: a list of strings, representing the note name
#   freq: an integer, representing pitch (Hz)
# Returns: a dictionary
def buildNoteRepo(note, freq):
    noteRepo = {}
    octave = 1
    freq_increment = 2
    while octave <= 6:
        for i in range(len(noteList)):
            noteRepo[noteList[i] + str(octave)] = (freqList[i] * freq_increment)
        octave += 1
        freq_increment *= 2
    return noteRepo  

noteList = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
freqList = [16.35, 17.32, 18.35, 19.45, 20.60, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87]

noteRepo = (buildNoteRepo(noteList, freqList))


robotToggle = 0
if robotToggle == 1:
    from botcore import *
    from time import sleep

# Class: Note
# Description: represents a Note object with notes of n duration
class Note(object):

    # Method: __init__
    # Description: constructor
    # Parameters:
    #   name: a list of strings, representing note name
    #   dur: a float, representing time elapse of pitch
    # Precondition: the function buildNoteRepo has been run
    # Postcondition: the data attributes are initialized
    # Returns: a newly created object of type Note
    def __init__(self, name, freq, dur):
        # Data attributes: 
        #   name: a string, representing note name
        #   freq:  an float, representing pitch
        #   dur:  a float, representing time elapse of pitch     
        self.name = name
        self.freq = freq
        self.dur  = dur  
    
    # Method: getName
    # Description: retrieves a Note object's name (note and octave position)
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: a string        
    def getName(self):
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

    # Method: __str__
    # Description: Defines how to cast the objects of class Note into a string  
    # Parameters: none
    # Precondition: none
    # Postcondition: no change
    # Returns: a string    
    def __str__(self):
        return self.name + ': <' + str(self.freq) + '>'

## END OF CLASS NOTE ##


# Function: buildTune
# Description: builds a list of Note objects
# Parameters: 
#   motif: a string, of note names
# Preconditions: the function buildNoteRepo has been run 
# Postcondition: the Note class is instanciated
# Returns: a list      
def buildTune(notes):
    notesList = []

    for note in notes:
        try:
            noteObject = Note(note, noteRepo[note], 1.0)            
            notesList.append(noteObject)
        except KeyError:
            raise ValueError("Hey that's not a note!!")

    return notesList
      
# notes = ['A5', 'G5', 'A5', 'E5', 'C5', 'E5', 'A4']
# notesList = buildTune(notes)
# print(notesList[0].getFreq())
    
# Function: playMotif
# Description: plays the list of Note objects' frequencies, with Note object duration
# Parameters: 
#   notesList: a list of Note objects
# Preconditions: none 
# Postcondition: no change
# Returns: STUB emitted Hz of dur duration       
def playMotif(notesList):
    if robotToggle == 1:
        for note in notesList:
            spkr.pitch(round(note.getFreq()))
            sleep(note.dur)
            spkr.off()
              # articulation gap
            sleep(0.05)
#playMotif(notesList)



# create Rhythm class, that inherits from Note? includes tempo, dur
# dur will be a list of durs for each note
# tempo will be 1 num that alters all durs appropriately

# Then Dance class that inherits from Rhythm, instanciates dance moves
# Then Song function?


# Class: Rhythm
# Description: represents a collection of Note objects with notes of n duration
class Rhythm(Note):

    # Method: __init__
    # Description: constructor
    # Parameters:
    #   name:  a list of strings, representing note name
    #   dur:   a float, representing time elapse of pitch
    #   tempo: an integer, representing tempo
    # Precondition: STUB
    # Postcondition: the data attributes are initialized
    # Returns: a newly created object of type Rhythm
    def __init__(self, name, freq, dur, tempo):
        Note.__init__(self, name, freq, dur)
        # Data attributes: 
        #   name:  a string, representing note name
        #   freq:  an float, representing pitch
        #   dur:   a float, representing time elapse of pitch
        #   tempo: an integer, representing tempo      
        self.name = name
        self.freq = freq
        self.dur  = dur
        self.tempo = tempo

    # Method: getTempo
    # Description: retrieves a Note object's tempo 
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: a float        
    def getTempo(self):
        return self.tempo
    
    # Method: setDur
    # Description: resets a list of Note object's durations based on tempo
    #   (1 = default slow, 2 to 5 = increasingly faster)
    # Parameters: 
    #   tempo, an integer
    # Preconditions: STUB 
    # Postcondition: STUB
    # Returns: None      
    def setDur(self):
        self.dur = self.dur / self.getTempo()


## END OF CLASS RHYTHM##

# Function: buildMotif
# Description: builds a list of Note objects
# Parameters: 
#   motif: a string, of note names
# Preconditions: the function buildNoteRepo has been run 
# Postcondition: STUB
# Returns: a list, of Rhythm objects       
def buildMotif(notes, durs, tempo):
    motif = []
    counter = 0
    
    for note in notes:
        try:
            noteObject = Rhythm(note, noteRepo[note], durs[counter], tempo)            
            motif.append(noteObject)
            counter += 1
        except KeyError:
            raise ValueError("Hey that's not a note!!")

    return motif
      
notes = ['A5', 'G5', 'A5', 'E5', 'C5', 'E5', 'A4']
# list durs based upon approx to the first note!
durs  = [1, 1, 1, 1, 0.5, 1.5, 1.5]
tempo = 3
motif = buildMotif(notes, durs, tempo)

# Function: setTempo
# Description: applies desired tempo to list of Note objects
# Parameters: 
#   tempo: an number (float or int) 
# Preconditions: STUB
# Postcondition: STUB
# Returns:       
def setTempo(tempo):
    motifTempo = []
    if tempo != 1:
        for item in motif:
            item.setDur()
            motifTempo.append(item)
    return motifTempo
            
motifTempo = setTempo(tempo)  
print(motif[1].getDur())          
            
            
            
            
            
            
            
