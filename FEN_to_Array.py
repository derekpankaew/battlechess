import asyncio
import time
import chess
import chess.engine
import requests
import traceback
from collections import defaultdict
import numpy as np
import pandas as pd
from numpy import array
from numpy import argmax
from keras.utils import to_categorical

# Encode individual pieces into numbers
# Black is lowercase, white is uppercase

def pieceToNumber(input):
    
    result = []
    
    for piece in input:
        
        piece = str(piece)
    
        if piece == "0":
            
            result.append(0)
        
        if piece == "r":
        
            result.append(1)
        
        if piece == "n":
        
            result.append(2)
        
        if piece == "b":
            
            result.append(3)
        
        if piece == "q":
            
            result.append(4)
        
        if piece == "k":
        
            result.append(5)
        
        if piece == "p":
        
            result.append(6)
        
        if piece == "R":
        
            result.append(7)
        
        if piece == "N":
        
            result.append(8)
        
        if piece == "B":
            
            result.append(9)
        
        if piece == "Q":
            
            result.append(10)
        
        if piece == "K":
        
            result.append(11)
        
        if piece == "P":
        
            result.append(12)
            
    return result

# Takes a value like "2P2Kp1" and returns:
# [0, 0, 'P', 0, 0, 'K', 'p', 0]

def ExpandIntToZeros(positions):
    
    result = []
    
    for piece in positions: # Examine every letter in the input
        
        try:
            
            piece = int(piece) # If it's a number, turn it into an Int
            
            # For each number, add a zero
            
            for number in range(piece):
                
                result.append(0)
        
        except:
            
            result.append(piece) # If it's not an int, just append it
            
    return result

def oneHotEncodedHack(input):
    
    result = []
    
    for piece in input:
        
        if piece == 0:
            
            result.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            
        if piece == 1:
            
            result.append([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            
        if piece == 2:
            
            result.append([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        
        if piece == 3:
            
            result.append([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            
        if piece == 4:
            
            result.append([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
            
        if piece == 5:
            
            result.append([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
        
        if piece == 6:
            
            result.append([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
            
        if piece == 7:
            
            result.append([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
            
        if piece == 8:
            
            result.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
        
        if piece == 9:
            
            result.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
            
        if piece == 10:
            
            result.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
            
        if piece == 11:
            
            result.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
                        
        if piece == 12:
            
            result.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
            
    return result

def stringToRow(FENString):
    
#    print("Digits Expanded for Zeros:")

    digitsToZero = ExpandIntToZeros(FENString) # Bursts numbers like 4 into that number of 0s
    
#    print(digitsToZero)
#    
#    print("Change Letters into Ints:")
    
    readyToEncode = pieceToNumber(digitsToZero) # Change letters like R into ints
    
#    print(readyToEncode)
#    
#    print("One Hot Encoded:")
#    
    final = oneHotEncodedHack(readyToEncode) # One hot encode, returns an array of arrays
    
#    print(final)
    
    # Transform array of arrays into 1 row
                
    oneRow = array(final)    
    oneRow = np.reshape(oneRow, oneRow.shape + (1,))
    oneRow = oneRow.reshape(13,1,8)
    
    return oneRow

def FENtoArray(FEN):
    
    splitRows = FEN.split("/")
    
    for x, str in enumerate(splitRows):
        
        if x == 0:
            
            result = stringToRow(str)
        
        else:
        
            result = np.concatenate((result, stringToRow(str)),axis=1)
    
    return result.flatten()