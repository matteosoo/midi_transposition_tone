#!/usr/bin/env python
# coding: utf-8

# In[22]:


#converts all midi files in the current folder

import glob
import os
import music21

# every semitones between -5~0~6

# converting everything into the key of C major or A minor
majors = dict([("A-", 4),("A", 3),("B-", 2),("B", 1),("C", 0),("D-", -1),("D", -2),("E-", -3),("E", -4),("F", -5),("G-", 6),("G", 5)])
# minors = dict([("A-", 1),("A", 0),("B-", -1),("B", -2),("C", -3),("D-", -4),("D", -5),("E-", 6),("E", 5),("F", 4),("G-", 3),("G", 2)])

# converting everything into the key of G major or E minor
majors = dict([("A-", -1),("A", -2),("B-", -3),("B", -4),("C", -5),("D-", 6),("D", 5),("E-", 4),("E", 3),("F", 2),("G-", 1),("G", 0)])
# minors = dict([("A-", -4),("A", -5),("B-", 6),("B", 5),("C", 4),("D-", 3),("D", 2),("E-", 1),("E", 0),("F", -1),("G-", -2),("G", -3)])

# os.chdir("./")
for file in glob.glob("*.mid"):
    score = music21.converter.parse(file)
    key = score.analyze('key')
    print('Original key: ', key.tonic.name, key.mode)
    
    #  halfStep: semitone range
    if key.mode == "major":
        halfSteps = majors[key.tonic.name]
        print(halfSteps)
        
    elif key.mode == "minor":
        halfSteps = minors[key.tonic.name]
    
    newscore = score.transpose(halfSteps)
    key = newscore.analyze('key')
    print('Target key: ', key.tonic.name, key.mode)
    newFileName = "New_" + file
    newscore.write('midi',newFileName)


# In[ ]:




