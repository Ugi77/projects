# DanceItRobit

## Description
To increase my Python coding skills, I was gifted with a coding robot.  This little robot can be programmed for a variety of actions, including movement and sound.  As soon as I learned its basic capabilities, I wanted to challenge myself to create an advanced program that utilized the robot's full capabilities, my music background, and some rigorous OOP.  The result is this program, which inputs a user's musical motifs, pitch durations, and tempo.  Pitch build, keyboard build, and motif arrangement are abstracted from the user, culminating in a music structure with accompanying dance moves.  The output is a robot's artistic expression through song and postmodern contact-improvisation industrial dance.
 
## Tech
+ Python3
+ Firia Labs CodeBot

## Usage
### Set robotToggle to user preference

With standalone Python3, set robotToggle variable to '0'.  

This serves as a rudimentary check and outputs very basic pitch representations (minus rhythm) and a printed description of dance moves.  

NOTE: the pitch output is not satisfactory with longer motifs and fast tempos.  I am working to utilize a better method.
```python
robotToggle = 0
```

With Python3 and Codebot, set robotToggle variable to '1'.    

This outputs all program aspects (pitch, tempo, rhythm, dance):
```python
robotToggle = 1
```

### Create your own work!
The existing motif calls can be commented out:
```python
motif1 = Motif()
motif1.buildMotif([9, 7, 9, 4, 0, 4, -3], keyboard, [0.5, 0.5, 0.5, 0.5, 0.25, 1, 1], 3.5)
motif2 = Motif()
motif2.buildMotif([21, 19, 21, 16, 12, 16, 9], keyboard, [0.5, 0.5, 0.5, 0.5, 0.25, 1, 1], 3.5, 7)
motif3 = Motif()
motif3.buildMotif([9, 11, 12, 11, 12, 12, 9, 11, 9, 11, 11, 7, 9, 7, 9, 9, 11, 12], keyboard,
            [0.5, 0.5, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 1], 3.5)
motif4 = Motif()
motif4.buildMotif([9, 11, 12, 11, 12, 12, 9, 11, 9, 11, 11, 7, 9, 7, 9, 9, 11, 12], keyboard,
            [0.5, 0.5, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 0.5, 0.25, 0.5, 0.5, 0.25, 1], 3.5, 7)
motif5 = Motif()
motif5.buildMotif([-3, -3], keyboard, [0.75, 1], 1)
```

...and users may implement their own as follows:

**1) Create a Motif object**
```python
myMotif = Motif()
```

**2) Call buildMotif with desired notePositions, durations, tempo**
+ notePositions represent keyboard note positions (e.g. 0 = C4, 12 = C5)
+ durations represent each note duration in seconds
+ tempo represents overall speed (e.g. 1 = 1 second, 2 = 0.5 second)
+ Example:
```python
myMotif.buildMotif([17, 17, 17, 24], keyboard, [0.4, 0.1, 0.1, 0.8], 1)
```
To aid in composition, a handy keyboard guide will print out pitch names, frequencies, and keyboard position:
```python
for note in keyboard:
    print(note)
```

**3) Try out the motif:**
```python
myMotif.playMotif()
```

**4) To add a dance move, create a Dance object, with dance move chosen from 'catwalk', 'twirl', or 'krump':**
```python
dance1 = Dance(myMotif, 'catwalk')
dance1.danceIt()
```

**5) Put it all together!**
+ Create additional Motif objects
+ Call the composer function with list of motifs, and motif order (based on motif list index position)
```python
composer([myMotif], [0, 0, 0])
```
