# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 09:14:43 2022

@author: nari2
"""

robotToggle = 0
if robotToggle == 0:
    import winsound
elif robotToggle == 1:
    from botcore import *
    from time import sleep


# Class: Pitch
# Description: represents a Pitch object with specific frequency and 1s duration
class Pitch(object):
    
    nextPos = -36
    
    # Method: __init__
    # Description: constructor
    # Parameters:
    #   name: a string, representing note name
    #   freq: a float, representing pitch (Hz)
    # Precondition: none
    # Postcondition: the data attributes are initialized
    # Returns: a newly created object of type Pitch
    def __init__(self, name, freq):
        # Data attributes: 
        #   name: a string, representing note name
        #   freq: an float, representing pitch (Hz)
        #   pos:  an integer, representing the Pitch object's keyboard position
        self.name = name
        self.freq = freq
        self.pos = Pitch.nextPos
        Pitch.nextPos += 1
    
    # Method: getName
    # Description: retrieves a Pitch object's name (note and octave position)
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: a string        
    def getName(self):
        return self.name

    # Method: getPos
    # Description: retrieves a Pitch object's keyboard position, where 0 = middle C
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: a string        
    def getPos(self):
        return self.pos
    
    # Method: getFreq
    # Description: retrieves a Pitch object's frequency (Hz)
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: a float        
    def getFreq(self):
        return self.freq

    # # Method: transposePitch
    # # Description: transpose a Pitch object
    # # Parameters: 
    # #   step: an integer (positive or negative)
    # # Precondition: STUB   
    # # Postcondition: STUB
    # # Returns: a Pitch object
    # def transposePitch(self, step):
    #     transposOn = (self.getPos() + step) + -36
    #     # shit now how do i retrieve the Pitch obj with just the position
    #     return keyboard[transposOn]
    
    # Method: playPitch
    # Description: plays a Pitch object's frequency at 1s duration
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: None       
    def playPitch(self):
        if robotToggle == 0:
            winsound.Beep(round(self.getFreq()), 1000)
        elif robotToggle == 1:
            spkr.pitch(round(self.getFreq()))
            sleep(1.0)
            spkr.off()

    # Method: __str__
    # Description: defines how to cast the objects of class Pitch into a string  
    # Parameters: none
    # Precondition: none
    # Postcondition: no change
    # Returns: a string    
    def __str__(self):
        return self.name + ': Hz = ' + str(self.freq) + ', Position = ' + str(self.pos)

## END OF CLASS PITCH ##


# Function: buildKeyboard 
# Description: assigns note names to their frequency (Hz)
# Parameters: 
#   scale: a list of strings, representing the note names of a scale
# Returns: a list of Pitch objects
def buildKeyboard(scale):
    keyboard = []
    octave = 1
    x = 4 # C1
    while octave <= 6:
        for i in range(len(noteList)):
            HzAssmt = 440 * (2**((x - 49)/12))
            PitchObject = Pitch(noteList[i] + str(octave), HzAssmt)
            keyboard.append(PitchObject)
            x += 1
        octave += 1
    return keyboard  

noteList = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
keyboard = buildKeyboard(noteList)
# keyboard[50].playPitch()
# print(keyboard[6])
for note in keyboard:
    print(note)

# Function: getNameFromPos
# Description: retrieves a Pitch object's name 
# Parameters: 
#   keyboard: a list, of Pitch objects
#   pos: an integer, representing the Pitch object's keyboard position, where 0 = middle C
# Returns: a string        
def getNameFromPos(keyboard, pos):
    for note in keyboard:
        if note.getPos() == pos:
            return note.getName()
# print(getNameFromPos(keyboard, 9))



# Class: Motif
# Description: represents a collection of Pitch objects, with notes of n duration
class Motif(object):
    
    # Method: __init__
    # Description: constructor
    # Parameters: none
    # Precondition: the function buildKeyboard has been run
    # Postcondition: the data attributes are initialized
    # Returns: a newly created object of type Motif
    def __init__(self):
        # Data attributes: 
        #   motifList: a list of Pitch objects
        self.motifList = []
        
    # Method: buildMotif
    # Description: add Pitch objects to build a motif
    # Parameters: 
    #   notePositions: a list of integers, representing keyboard note positions (e.g. 0 = C4, 12 = C5)
    #   durations:     a list of numbers (floats or ints) representing each note duration in seconds
    #   tempo:         a number (float or int), where 1 = 1s, 2 = 0.5s
    #   step:          an integer (positive or negative), default is 0 unless transposition wished
    # Precondition: the function buildKeyboard has been run   
    # Postcondition: Pitch objects and their adjusted durations, transpositions are added
    # Returns: None
    def buildMotif(self, notePositions, durations, tempo, step = 0):
        # transpose if step is a parameter in the call
        if step != 0:
            notePositionsCopy = notePositions[:]
            notePositions = list(map(lambda x: x+step, notePositionsCopy))
        
        # adjust durations based on tempo
        tempoDurations = list(map(lambda x: x/tempo, durations))       
        counter = 0    
        for pos in notePositions:
                # get and append that Pitch object & its associated duration
                for note in keyboard:
                    if note.getPos() == pos:             
                        self.motifList.append([note, tempoDurations[counter]])
                        counter += 1
        #return self.motifList
    
    # Method: getNames
    # Description: retrieves Pitch object's names from a motif
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: a list, of strings        
    def getNames(self):
        noteNameslist = [] 
        for note in self.motifList:
            noteNameslist.append(note[0].getName())
        return noteNameslist
    
    # Method: playMotif
    # Description: emits a Motif object's frequencies and durations
    # Parameters: none
    # Preconditions: the functions buildKeyboard and buildMotif have been run 
    # Postcondition: no change
    # Returns: None       
    def playMotif(self):
        if robotToggle == 0:
            for note in self.motifList:
                winsound.Beep(round(note[0].getFreq()), round(note[1] * 1000))
        elif robotToggle == 1:
            for note in self.motifList:
                spkr.pitch(round(note[0].getFreq()))
                sleep(note[1])
                spkr.off()
                 # articulation gap
                sleep(0.05)

    
motif1 = Motif()
motif1.buildMotif([9, 7, 9, 4, 0, 4, -3], [0.5, 0.5, 0.5, 0.5, 0.25, 1, 1], 3)
motif2 = Motif()
motif2.buildMotif([21, 19, 21, 16, 12, 16, 9], [0.5, 0.5, 0.5, 0.5, 0.25, 1, 1], 3, 7)
motif3 = Motif()
motif3.buildMotif([9, 11, 12, 11, 12, 12, 9, 11, 9, 11, 11, 7, 9, 7, 9, 9, 11, 12], 
            [0.5, 0.5, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 1], 4)
motif4 = Motif()
motif4.buildMotif([9, 11, 12, 11, 12, 12, 9, 11, 9, 11, 11, 7, 9, 7, 9, 9, 11, 12], 
            [0.5, 0.5, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 1], 4, 7)
motif5 = Motif()
motif5.buildMotif([-3, -3], [0.75, 1], 1)

#motif4.playMotif()
# print(motif4.getNames())
    

# Class: Dance
# Description: represents a Dance object with musical motifs and dance moves
class Dance(object):
  
    # Method: __init__
    # Description: constructor
    # Parameters:
    #   motif:     a Motif object
    #   danceMove: a string, chosen from 'catwalk', 'twirl', or 'twerk'
    # Precondition: buildMotif has been called
    # Postcondition: the data attributes are initialized
    # Returns: a newly created object of type Dance
    def __init__(self, motif, danceMove):
        # Data attributes: 
        #   motif:     a Motif object
        #   danceMove: a string, chosen from 'catwalk', 'twirl', or 'twerk'
        self.motif     = motif
        self.danceMove = danceMove     
        
    def danceIt(self):        
        if robotToggle == 0:
            if self.danceMove == 'catwalk':
                print('Imagine a robot doing an awesome catwalk')
                self.motif.playMotif()
                
            elif self.danceMove == 'twirl':
                print('Imagine a robot doing a delightful twirl')
                self.motif.playMotif()
            
            elif self.danceMove == 'twerk':
                print('Imagine a robot...twerking...')
                self.motif.playMotif()
                
        elif robotToggle == 1:
            if self.danceMove == 'catwalk':
                motors.enable(True)
                motors.run(LEFT, 40)
                motors.run(RIGHT, 40)
                self.motif.playMotif()
                motors.run(LEFT, 60)
                motors.run(RIGHT, -60)
                sleep(0.1)
                motors.run(LEFT, -60)
                motors.run(RIGHT, 60)
                sleep(0.1)
                motors.enable(False)
                
            elif self.danceMove == 'twirl':
                motors.enable(True)
                motors.run(LEFT, 60)
                motors.run(RIGHT, -60)
                self.motif.playMotif()
                motors.enable(False)
            
            elif self.danceMove == 'twerk':
                counter = 0
                while counter < 3:
                    motors.enable(True)
                    motors.run(LEFT, 70)
                    motors.run(RIGHT, 70)
                    sleep(0.15)
                    motors.run(LEFT, -70)
                    motors.run(RIGHT, -70)
                    sleep(0.15)
                    
                    motors.run(LEFT, 80)
                    motors.run(RIGHT, -80)
                    sleep(0.2)
                    motors.run(LEFT, -80)
                    motors.run(RIGHT, 80)
                    sleep(0.2)
                    counter += 1
                    motors.enable(False)
                leds.ls(0b11111)
                self.motif.playMotif()
        
# dance1 = Dance(motif1, 'catwalk')
# dance1.danceIt()

# Function: composer
# Description: performs a sequence of coordinated motifs and dance moves
# Parameters: none
# Preconditions: buildMotif has been called
# Postcondition: no change
# Returns: None       
def composer():
    dance1 = Dance(motif1, 'catwalk')
    dance2 = Dance(motif2, 'catwalk')
    dance3 = Dance(motif3, 'twirl')
    dance4 = Dance(motif4, 'twirl')
    dance5 = Dance(motif5, 'twerk')

    dance1.danceIt()
    dance1.danceIt()
    dance3.danceIt()    
    dance1.danceIt()
    dance1.danceIt()
    dance3.danceIt()
    
    dance2.danceIt()
    dance2.danceIt()
    dance4.danceIt()
    dance2.danceIt()
    dance2.danceIt()
    dance4.danceIt()
    dance5.danceIt()

# composer()



          