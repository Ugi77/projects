# -*- coding: utf-8 -*-


import random

robot_toggle = 0
if robot_toggle == 0:
    import winsound
elif robot_toggle == 1:
    from botcore import *
    from time import sleep
else:
    print("Hey, set robot_toggle to 0 or 1!")
    print("    ")


# Class: Pitch
# Description: represents a Pitch object with specific frequency and 1 second duration
class Pitch(object):
    
    next_pos = -36
    
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
        self.pos  = Pitch.next_pos
        Pitch.next_pos += 1
    
    # Method: get_name
    # Description: retrieves a Pitch object's name (note and octave position)
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: a string        
    def get_name(self):
        return self.name

    # Method: get_pos
    # Description: retrieves a Pitch object's keyboard position, where 0 = middle C
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: an integer        
    def get_pos(self):
        return self.pos
    
    # Method: get_freq
    # Description: retrieves a Pitch object's frequency (Hz)
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: a float        
    def get_freq(self):
        return self.freq

    # Method: play_pitch
    # Description: plays a Pitch object's frequency at 1s duration
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: None       
    def play_pitch(self):
        if robot_toggle == 0:
            winsound.Beep(round(self.get_freq()), 1000)
        elif robot_toggle == 1:
            spkr.pitch(round(self.get_freq()))
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


# Function: build_keyboard 
# Description: assigns note names to their frequency (Hz), beginning at C1
# Parameters: none
# Returns: a list of Pitch objects
def build_keyboard():
    note_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    keyboard = []
    octave   = 1
    x        = 4 # This represents C1, or integer to initiate proper steps below A4
    while octave <= 6:
        for i in range(len(note_list)):
            # Calculate Hz (frequency), where (x - 49) is the number of notes away from A4
            # Example: (x - 49) = 45, the # steps C1 is from A4 
            # This is (C1 - A4) or using positions: (9 - -36) = 45
            hz_assmt = 440 * (2**((x - 49)/12))
            pitch_object = Pitch(note_list[i] + str(octave), hz_assmt)
            keyboard.append(pitch_object)
            # Increment 'x' to go to next piano key
            x += 1
        # Increment octave after each run through the note_list    
        octave += 1
    return keyboard

keyboard = build_keyboard()

# This outputs a handy keyboard reference for composing
for note in keyboard:
    print(note)


# Function: get_name_from_pos
# Description: retrieves a Pitch object's name (note and octave)
# Parameters: 
#   keyboard: a list, of Pitch objects
#   position: an integer, representing the Pitch object's keyboard position, where 0 = middle C
# Returns: a string        
def get_name_from_pos(keyboard, position):
    for note in keyboard:
        if note.get_pos() == position:
            return note.get_name()
 

# Class: Motif
# Description: represents a collection of Pitch objects, with notes of n duration
class Motif(object):
    
    # Method: __init__
    # Description: constructor
    # Parameters: none
    # Precondition: the function build_keyboard has been run
    # Postcondition: the data attributes are initialized
    # Returns: a newly created object of type Motif
    def __init__(self):
        # Data attributes: 
        #   motif_list: a list of Pitch objects
        self.motif_list = []
        
    # Method: build_motif
    # Description: add Pitch objects to build a motif
    # Parameters: 
    #   note_positions: a list of integers, representing keyboard note positions (e.g. 0 = C4, 12 = C5)
    #   keyboard:       a list, of Pitch objects
    #   durations:      a list of numbers (floats or ints) representing each note duration in seconds
    #   tempo:          a number (float or int), where 1 = 1s, 2 = 0.5s
    #   step:           an integer (positive or negative), default is 0 unless transposition wished

    # Precondition: the function build_keyboard has been run   
    # Postcondition: Pitch objects and their adjusted durations, transpositions are added
    # Returns: None
    def build_motif(self, note_positions, keyboard, durations, tempo, step = 0):
        # transpose if step is a parameter in the call
        if step != 0:
            note_positions_copy = note_positions[:]
            note_positions = list(map(lambda x: x + step, note_positions_copy))
        
        # adjust durations based on tempo
        tempo_durations = list(map(lambda x: x/tempo, durations))       
        counter = 0    
        for pos in note_positions:
                # get and append that Pitch object & its associated duration
                for note in keyboard:
                    if note.get_pos() == pos:             
                        self.motif_list.append([note, tempo_durations[counter]])
                        counter += 1
        
    # Method: get_names
    # Description: retrieves Pitch object's names from a motif
    # Parameters: none
    # Preconditions: none 
    # Postcondition: no change
    # Returns: a list, of strings        
    def get_names(self):
        note_names_list = [] 
        for note in self.motif_list:
            note_names_list.append(note[0].get_name())
        return note_names_list
    
    # Method: play_motif
    # Description: emits a Motif object's frequencies and durations
    # Parameters: none
    # Preconditions: the functions build_keyboard and build_motif have been run 
    # Postcondition: no change
    # Returns: None       
    def play_motif(self):
        if robot_toggle == 0:
            for note in self.motif_list:
                winsound.Beep(round(note[0].get_freq()), round(note[1] * 1000))
        elif robot_toggle == 1:
            for note in self.motif_list:
                spkr.pitch(round(note[0].get_freq()))
                sleep(note[1])
                spkr.off()
                 # articulation gap
                sleep(0.05)

motif1 = Motif()
motif1.build_motif([9, 7, 9, 4, 0, 4, -3], keyboard, [0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 1], 3)

# motif2 = Motif()
# motif2.build_motif([16, 14, 16, 11, 7, 11, 4], keyboard, [0.5, 0.5, 0.5, 0.5, 0.25, 0.75, 1], 3)

# motif3 = Motif()
# motif3.build_motif([9, 11, 12, 11, 12, 12, 9, 11, 9, 11, 11, 7, 9, 7, 9, 9, 11, 12], keyboard,
#             [0.5, 0.5, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 1], 3)
# motif4 = Motif()
# motif4.build_motif([9, 11, 12, 11, 12, 12, 9, 11, 9, 11, 11, 7, 9, 7, 9, 9, 11, 12], keyboard,
#             [0.5, 0.5, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 1], 3, 7)
# motif5 = Motif()
# motif5.build_motif([-3, -3], keyboard, [0.75, 1], 1)
    
    
# Class: Dance
# Description: represents a Dance object with musical motifs and dance moves
class Dance(object):
  
    # Method: __init__
    # Description: constructor
    # Parameters:
    #   motif:     a Motif object
    #   dance_move: a string, chosen from 'catwalk', 'twirl', or 'krump'
    # Precondition: build_motif has been called
    # Postcondition: the data attributes are initialized
    # Returns: a newly created object of type Dance
    def __init__(self, motif, dance_move):
        # Data attributes: 
        #   motif:      a Motif object
        #   dance_move: a string, chosen from 'catwalk', 'twirl', or 'krump'
        self.motif      = motif
        self.dance_move = dance_move     

    # Method: dance_it
    # Description: coordinates a Dance object's motif with sound and dance_move with motion
    # Parameters: none
    # Preconditions: the functions build_keyboard and build_motif have been run 
    # Postcondition: no change
    # Returns: None           
    def dance_it(self):        
        if robot_toggle == 0:
            if self.dance_move == 'catwalk':
                print('Imagine a robot doing an awesome catwalk')
                self.motif.play_motif()
                
            elif self.dance_move == 'twirl':
                print('Imagine a robot doing a delightful twirl')
                self.motif.play_motif()
            
            elif self.dance_move == 'krump':
                print('Imagine a robot...krumping...')
                self.motif.play_motif()
                
        elif robot_toggle == 1:
            if self.dance_move == 'catwalk':
                motors.enable(True)
                motors.run(LEFT, 30)
                motors.run(RIGHT, 30)
                self.motif.play_motif()
                motors.run(LEFT, 60)
                motors.run(RIGHT, -60)
                sleep(0.1)
                motors.run(LEFT, -60)
                motors.run(RIGHT, 60)
                sleep(0.1)
                motors.enable(False)
                
            elif self.dance_move == 'twirl':
                motors.enable(True)
                motors.run(LEFT, -45)
                motors.run(RIGHT, 45)
                self.motif.play_motif()
                motors.enable(False)
            
            elif self.dance_move == 'krump':
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
                self.motif.play_motif()
        
## END OF CLASS DANCE ##


# Function: composer
# Description: coordinates & performs a sequence of motifs and dance moves
# Parameters: 
#   motifs: a list, of Motif objects
#   motif_order: a list, of desired Motif object order (by index position) & repetition
# Preconditions: build_motif has been called
# Postcondition: Dance objects are created
# Returns: None       
def composer(motifs, motif_order): 
    dance_list = []
    
    for motif in motifs[0:-1]:
        dance_obj = Dance(motif, random.choice(['catwalk', 'twirl']))
        dance_list.append(dance_obj)
    # make that last move really special                     
    dance_end = Dance(motifs[-1], 'krump')
    dance_list.append(dance_end)
    
    for num in motif_order: 
        dance_list[num].dance_it()

# composer([motif1, motif2, motif3, motif4, motif5], [0, 0, 2, 0, 0, 2, 1, 1, 3, 1, 1, 3, 4])


