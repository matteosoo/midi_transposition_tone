#!/usr/bin/env python
# coding: utf-8

# converts all midi files in the current folder

import glob
import os
import music21

# every semitones between -5~0~6
majors = {
    'C': {'A-': 4, 'A': 3, 'B-': 2, 'B': 1, 'C': 0, 'D-': -1, 'D': -2, 'E-': -3, 'E': -4, 'F': -5, 'G-': 6, 'G': 5},
    'D-': {'A-':5, 'A': 4, 'B-': 3, 'B': 2, 'C': 1, 'D-': 0, 'D': -1, 'E-': -2, 'E': -3, 'F': -4, 'G-': -5, 'G': 6},
    'D': {'A-': 6, 'A': 5, 'B-': 4, 'B': 3, 'C': 2, 'D-': 1, 'D': 0, 'E-': -1, 'E': -2, 'F': -3, 'G-': -4, 'G': -5},
    'E-': {'A-': -5, 'A': 6, 'B-': 5, 'B': 4, 'C': 3, 'D-': 2, 'D': 1, 'E-': 0, 'E': -1, 'F': -2, 'G-':-3, 'G': -4},
    'E': {'A-': -4, 'A': -5, 'B-': 6, 'B': 5, 'C': 4, 'D-': 3, 'D': 2, 'E-': 1, 'E': 0, 'F': -1, 'G-': -2, 'G': -3},
    'F': {'A-': -3, 'A': -4, 'B-': -5, 'B': 6, 'C': 5, 'D-': 4, 'D': 3, 'E-': 2, 'E': 1, 'F': 0, 'G-': -1, 'G': -2},
    'G-': {'A-': -2, 'A': -3, 'B-': -4, 'B': -5, 'C': 6, 'D-': 5, 'D': 4, 'E-': 3, 'E': 2, 'F': 1, 'G-': 0, 'G': -1},
    'G': {'A-': -1, 'A': -2, 'B-': -3, 'B': -4, 'C': -5, 'D-': 6, 'D': 5, 'E-': 4, 'E': 3, 'F': 2, 'G-': 1, 'G': 0},
    'A-': {'A-': 0, 'A': -1, 'B-': -2, 'B': -3, 'C': -4, 'D-': -5, 'D': 6, 'E-': 5, 'E': 4, 'F': 3, 'G-': 2, 'G': 1},
    'A': {'A-': 1, 'A': 0, 'B-': -1, 'B': -2, 'C': -3, 'D-': -4, 'D': -5, 'E-': 6, 'E': 5, 'F': 4, 'G-': 3, 'G': 2},
    'B-': {'A-': 2, 'A': 1, 'B-': 0, 'B': -1, 'C': -2, 'D-': -3, 'D': -4, 'E-': -5, 'E': 6, 'F': 5, 'G-': 4, 'G': 3},
    'B': {'A-': 3, 'A': 2, 'B-': 1, 'B': 0, 'C': -1, 'D-': -2, 'D': -3, 'E-': -4, 'E': -5, 'F': 6, 'G-': 5, 'G': 4},
}

'''
# same method in minors
# A minors
 minors = {
    'A': {'A-': 1, 'A': 0, 'B-': -1, 'B': -2, 'C': -3, 'D-': -4, 'D': -5, 'E-': 6, 'E': 5, 'F': 4, 'G-': 3, 'G': 2},
 }
 '''
 
# os.chdir("./")
target = input('Type your target key: (ex: C, D-, D, E-, E ...)')

for file in glob.glob("*.mid"):
    score = music21.converter.parse(file)
    key = score.analyze('key')
    print('Original key: ', key.tonic.name, key.mode)
    
    #  halfStep: semitone range
    if key.mode == "major":
        halfSteps = majors[target][key.tonic.name]
        # print(halfSteps)
        
    elif key.mode == "minor":
        halfSteps = minors[target][key.tonic.name]
    
    newscore = score.transpose(halfSteps)
    key = newscore.analyze('key')
    print('Target key: ', key.tonic.name, key.mode)
    newFileName = "New_" + file
    newscore.write('midi',newFileName)
