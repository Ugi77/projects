# DanceItRobit

## Description
To increase my Python coding skills, I was gifted with a coding robot that can be programmed for a variety of actions, including movement and sound.  I wanted to challenge myself to create a program that utilized the robot's full capabilities, my music background, and some rigorous OOP.  

The result is this program, which inputs a user's musical motifs, pitch durations, and tempo.  Pitch build, keyboard build, and motif arrangement are abstracted from the user. 

The output is a robot's artistic expression through music and postmodern contact-improvisation industrial dance:  

https://user-images.githubusercontent.com/97997533/157977307-b7b175e4-75cd-48e1-baef-2c861e1e5930.mp4 
 
## Tech
+ Python3
+ Firia Labs CodeBot

## Usage
### Set robot_toggle to user preference

With standalone Python3, set robot_toggle variable to '0'.  

This serves as a rudimentary check and outputs very basic pitch representations (minus rhythm) and a printed description of dance moves.  

NOTE: the pitch output is not satisfactory with longer motifs and fast tempos.  I am working to utilize a better method.
```python
robot_toggle = 0
```

With Python3 and Codebot, set robot_toggle variable to '1'.    

This outputs all program aspects (pitch, tempo, rhythm, dance):
```python
robot_toggle = 1
```

### Create your own work!  Scrollscrollscroll all the way down, and within the `main` function:
 

**1) Comment out the Motif object calls, and calls to the `build_motif` method and `composer` function**

**2) Create a Motif object:**
```python
my_motif = Motif()
```

**3) Call `build_motif` with the following arguments:**
+ a list, of note_positions, representing keyboard note positions (e.g. 0 = C4, 12 = C5)
+ keyboard (this is a default list of Pitch objects)
+ a list, of floats, representing each note duration in seconds
+ a float, for tempo, representing overall speed (e.g. 1.0 = 1 second, 2 = 0.5 second)
+ Example:
```python
my_motif.build_motif([17, 17, 17, 24], keyboard, [0.4, 0.1, 0.1, 0.8], 0.5)
```
To aid in composition, a handy keyboard guide will print out pitch names, frequencies, and keyboard position:
```python
for note in keyboard:
    print(note)
```

**4) Put it all together!**
+ Create additional Motif objects and `build_motif` method calls if wished
+ Call the `composer` function with the following arguments:
  + a list, of Motif objects
  + a list, of integers, indicating motif order (based on the Motif object list index position)
```python
composer([my_motif], [0, 0])
```
