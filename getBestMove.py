import chess
import random
from FEN_to_Array import FENtoArray
import keras
from keras.models import model_from_json
import pandas as pd
from pandas import DataFrame

board = chess.Board()

import time

maxMovesToAnalyze = 4

class predictor():
    
    def __init__(self):
        
        # Load neural network model
    
        self.model_name = "trained_models/ready_to_deploy"
        
        json_file = open(self.model_name + '.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        self.loaded_model.load_weights(self.model_name + ".h5")
    #    print("Loaded model from disk")
        
        # Load model
        
        self.loaded_model.compile(optimizer = "adam", loss = "binary_crossentropy", metrics = ["accuracy"])
    
    def makePrediction(self,data):
    
        X_test = data.tolist() # Turn into list
        X_test = [X_test] # Make it an array
        X_test = DataFrame.from_records(X_test) # Turn into DataFrame
        
#        print(X_test)
        
        # Run prediction using the neural network
        
        y_pred = self.loaded_model.predict(X_test) # returns the probability of each entry
        
#        print(y_pred)
        
        last = len(y_pred) - 1
        result = y_pred[last]
        
        return(result)

predictor = predictor()

start = time.time()

#print (result)


def getBestMove(board):
    
    possibleMoves = list(board.legal_moves)
    random.shuffle(possibleMoves)
    
    moveList = possibleMoves # Store it for later, to pick the winning move from
    
#    print("Possible Moves:\n%s"%(possibleMoves))
      
    winningChance = []
    
    index = 0
  
    for move in possibleMoves:
        
#        print("Stepping forward ...")
        
        nextMove = possibleMoves[0]
#        print("Next move:")
#        print(nextMove)
        possibleMoves.pop(0)
        
        board.push(nextMove)
        
#        print(board)
        
        nextString = board.fen()
        FEN = nextString.split(" ")
        FEN = FEN[0]
        
        arr = FENtoArray(FEN)
        prediction = predictor.makePrediction(arr)
  
        winningChance.append(prediction)
        
        board.pop()
        
        index += 1
        
        if index >= maxMovesToAnalyze:
            
#            print("BREAKING")
            
            break
    
#    print("Moves by win chance:")
    
#    print("winner is:")
    
    winner = winningChance.index(max(winningChance))
    
#    print (winner)
    
#    print (winningChance)
#    print (moveList)
    
    winningMove = moveList[winner]
    
#    print("Returning:\n%s" %(winningMove))
    
    end = time.time()
#    print(end - start)
    
    return winningMove
