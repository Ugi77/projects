# DanceItRobit

## Description
To increase my Python coding skills, I was gifted with a coding robot.  This little robot can be programmed for a variety of actions, including movement and sound.  As soon as I learned its basic capabilities, I wanted to challenge myself to create an advanced program that utilized the robot's full capabilities, my music background, and some rigorous OOP.  The result is this program, which inputs a user's musical motifs, pitch durations, and tempo.  Pitch build, keyboard build, and motif arrangement are abstracted from the user, culminating in a music structure with accompanying dance moves. 

The output is a robot's artistic expression through song and postmodern contact-improvisation industrial dance:  

https://user-images.githubusercontent.com/97997533/157977307-b7b175e4-75cd-48e1-baef-2c861e1e5930.mp4 
 
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
myMotif.buildMotif([17, 17, 17, 24], keyboard, [0.4, 0.1, 0.1, 0.8], 0.5)
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
When done, this can be commented out

**4) To add a dance move, create a Dance object, with dance move chosen from 'catwalk', 'twirl', or 'krump':**
```python
dance1 = Dance(myMotif, 'twirl')
dance1.danceIt()
```
When done, the call to danceIt can be commented out

**5) Put it all together!**
+ Create additional Motif objects
+ Comment out the existing call to the composer function
+ Call the composer function with list of motifs, and motif order (based on motif list index position)
```python
composer([myMotif], [0, 0])
```
