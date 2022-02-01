# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 09:14:43 2022

@author: nari2
"""

robotToggle = 0
if robotToggle == 1:
    from botcore import *
    from time import sleep
    
# Function: buildNoteRepo
# Description: maps note names to frequencies (Hz)
# Parameters: 
#   noteList: a list of strings, representing the note name
#   freqList: a float, representing pitch (Hz)
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


# Class: Note
# Description: represents a Note object with notes of n duration
class Note(object):
    # Method: __init__
    # Description: constructor
    # Parameters:
    #   name:  a list of strings, representing note name
    #   freq:  a float, representing pitch (Hz)
    #   dur:   a float, representing time elapse of pitch
    #   tempo: a number (float or int)
    # Precondition: the function buildNoteRepo has been run
    # Postcondition: the data attributes are initialized
    # Returns: a newly created object of type Note
    def __init__(self, name, freq, dur, tempo):
        # Data attributes: 
        #   name: a string, representing note name
        #   freq:  an float, representing pitch
        #   dur:  a float, representing time elapse of pitch
        #   tempo: a number (float or int)
        self.name = name
        self.freq = freq
        self.dur  = dur 
        self.tempo = tempo
    
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

    # Method: __str__
    # Description: Defines how to cast the objects of class Note into a string  
    # Parameters: none
    # Precondition: none
    # Postcondition: no change
    # Returns: a string    
    def __str__(self):
        return self.name + ': <' + str(self.freq) + '>'

## END OF CLASS NOTE ##


# Function: buildMotif
# Description: builds a list of Note objects with note duration and tempo
# Parameters: 
#   notes: a string, of note names
#   durs:  a list, of numbers (floats or ints)
#   tempo: a number (float or int) 
# Preconditions: the function buildNoteRepo has been run 
# Postcondition: Note objects are created
# Returns: a list, of Note objects       
def buildMotif(notes, durs, tempo):
    motif = []
    counter = 0    
    for note in notes:
        try:
            noteObject = Note(note, noteRepo[note], (durs[counter]/tempo), tempo)            
            motif.append(noteObject)
            counter += 1
        except KeyError:
            raise ValueError("Hey that's not a note!!")
    return motif
      
notes = ['A5', 'G5', 'A5', 'E5', 'C5', 'E5', 'A4']
durs  = [1, 1, 1, 1, 0.5, 1.5, 1.5]
tempo = 2
step = 5
motif = buildMotif(notes, durs, tempo)   

# Function: buildTransposedMotif
# Description: builds a list of Note objects with note duration, tempo, & transposition
# Parameters: 
#   motif: a string, of note names
#   durs:  a list, of numbers (floats or ints)
#   tempo: a number (float or int)
#   step:  an integer (positive or negative) 
# Preconditions: the function buildNoteRepo has been run 
# Postcondition: Note objects are created
# Returns: a list, of Note objects       
def buildTransposedMotif(notes, durs, tempo, step):
    transponsedNotes = []
    for note in notes:
        # take first part of notes string (e.g. 'A') & obtain index position
        position = noteList.index(note[0])
        # add or subtract steps
        transposition = position + step
        newPosition = transposition % 12
        # get relevant index, add octave back in (-1 if crosses over C, +1 if crosses over B)  
        # add to transponsedNotes list       
        if transposition // 12 == 0:
            transponsedNotes.append(noteList[newPosition] + (note[1]))
        else:
            transposOn = int(note[1]) + (transposition // 12)
            transponsedNotes.append(noteList[newPosition] + str(transposOn))            
    motif = buildMotif(transponsedNotes, durs, tempo)
    return motif
      
# motif = buildTransposedMotif(notes, durs, tempo, step)
# print(motif[0].getName())
# print(motif[0].getFreq())
# print(motif[0].getDur())
   

# Function: playMotif
# Description: plays the list of Note objects' frequencies
# Parameters: 
#   motif: a list of Note objects
# Preconditions: the robotToggle must be set to '1' 
# Postcondition: no change
# Returns: emitted Hz of dur duration       
def playMotif(motif):
    if robotToggle == 1:
        for note in motif:
            spkr.pitch(round(note.getFreq()))
            sleep(note.dur)
            spkr.off()
             # articulation gap
            sleep(0.05)
#playMotif(motif)


theme1 = (['A5', 'G5', 'A5', 'E5', 'C5', 'E5', 'A4'], [0.75, 1, 0.75, 1, 0.5, 1, 1], 5)
theme2 = (['A5', 'B5', 'C6', 'A5', 'C6', 'C6', 'A5', 'B5', 'A5', 'B5', 'B5', 'G5', 'A5', 'G5', 'A5', 'A5', 'B5', 'C6'], 
            [0.5, 0.5, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 1], 3)
theme3 = (['A3', 'A3'], [0.75, 1], 1)    

motif1 = buildMotif(theme1[0], theme1[1], theme1[2])
motif2 = buildMotif(theme2[0], theme2[1], theme2[2])
motif3 = buildMotif(theme3[0], theme3[1], theme3[2])
transpMotif1 = buildTransposedMotif(theme1[0], theme1[1], theme1[2], 7)
transpMotif2 = buildTransposedMotif(theme2[0], theme2[1], theme2[2], 7)

# Function: dance
# Description: perform sequence of dance moves
# Parameters: 
#   danceMove: a string, chosen from 'catwalk', 'twirl', or 'twerk'
#   motif:     a list, of Note objects
# Preconditions: the function buildMotif has been run, robotToggle is set to '1'
# Postcondition: no change
# Returns: None       
def dance(danceMove, motif):
    if robotToggle == 1:
        if danceMove == 'catwalk':
            motors.enable(True)
            motors.run(LEFT, 40)
            motors.run(RIGHT, 40)
            playMotif(motif)
            motors.run(LEFT, 60)
            motors.run(RIGHT, -60)
            sleep(0.1)
            motors.run(LEFT, -60)
            motors.run(RIGHT, 60)
            sleep(0.1)
            motors.enable(False)
                
        elif danceMove == 'twirl':
            motors.enable(True)
            motors.run(LEFT, 60)
            motors.run(RIGHT, -60)
            playMotif(motif)
            motors.enable(False)
            
        elif danceMove == 'twerk':
            counter = 0
            while counter <= 1.2:
                motors.enable(True)
                motors.run(LEFT, 70)
                motors.run(RIGHT, 70)
                sleep(0.15)
                motors.run(LEFT, -70)
                motors.run(RIGHT, -70)
                sleep(0.15)
                counter += 0.3
                motors.enable(False)
            leds.ls(0b11111)
            playMotif(motif)
            
themes = [motif1, motif2, transpMotif1, transpMotif2, motif3]

# Function: composer
# Description: perform sequence of coordinated motifs and dance moves
# Parameters: 
#   themes: a list, of motifs
# Preconditions: robotToggle is set to '1'
# Postcondition: no change
# Returns: None       
def composer(themes):
    if robotToggle == 1:
        dance('catwalk', themes[0])
        dance('catwalk', themes[0])
        dance('twirl', themes[1])
        dance('catwalk', themes[0])
        dance('catwalk', themes[0])
                
        dance('catwalk', themes[2])
        dance('catwalk', themes[2])
        dance('twirl', themes[3])
        dance('catwalk', themes[2])
        dance('catwalk', themes[2])
        dance('twirl', themes[3])
        
        dance('twerk', themes[4]) 

#composer(themes) 

# set toggle for sim environment so all calls produce test output in Spyder
# create additional parameter for Note obj to include index #, of keyboard, for easy abstracted calls
# make a motif class, could print display of motif (e.g. notes, nums) or play motif
# Note class could have transpose method (vs function) to build transposed Note obj
# fix Hz
# find python library to play pitches (to play in sim mode)
# separate files into infrastructure & then main program to play stuff
          