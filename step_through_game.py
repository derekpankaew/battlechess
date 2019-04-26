import time
import chess
import chess.engine
import pandas as pd
import numpy as np
from pandas import DataFrame
from FEN_to_Array import FENtoArray

board = chess.Board()

class dataFrameCreator():
    
    def __init__(self):
        
        self.result = 0

    def addToDataFrame(self,input,winner):
        
        # First time running
        
        if type(self.result) is int:
            
            data = input.tolist() # Turn into list
            data.append(winner) # Last column is result column
            data = [data] # Make it an array
            self.result = DataFrame.from_records(data) # Turn into DataFrame
    
        else:
            
            data = input.tolist() # Turn into list
            data.append(winner) # Last column is result column
            data = [data]
            self.result = self.result.append(data)

recordKeeper = dataFrameCreator()

def addGameToRecord(input,winner): # White is 1, Black is 0
    
    input = input.split(" ")

    print(input)
    
    for move in input:
    
        print("Making move %s" %(move))
    
        board.push_san(move)
    
        print("Board position is now:")
    
        print(board)
    
        print("The FEN is now:")
        
        FEN = board.fen()
        FEN = FEN.split(" ")
        FEN = FEN[0]
    
        print(FEN)
        
        dataToAdd = FENtoArray(FEN)
        
        recordKeeper.addToDataFrame(dataToAdd,winner) 
        
# Iterate through game data, adding it to dataframe

gameData = pd.read_csv("./readyfortraining2.csv")

for game in range(1000):
    
    moves = gameData.iloc[0,0]
    winner = gameData.iloc[0,1]
    gameData.drop(gameData.head(1).index, inplace=True) # Drop the top row
    
    if winner == "white":
    
        winner = 1
        
    elif winner == "black":
    
        winner = 0
        
    addGameToRecord(moves,winner)
    
    board.reset()


#addGameToRecord("Nf3 d5 c3 g6 d4 f6 h3 Bg7 e3 e5 c4 e4 Nfd2 f5 c5 c6 f3 b6 g3 bxc5 dxc5 Na6 Nb3 Nc7 Nd4 Ne7 b4 Ba6 Bxa6 Nxa6 a3 Rb8 Qe2 Bxd4 exd4 Nc7 Bg5 h6 Bf6 Rf8 Be5 Rb5 Nc3 Rb7 O-O Nb5 Nxb5 cxb5 Bd6 a6 fxe4 dxe4 Qe3 g5 Qb3 f4 Rae1 Nf5 Rxe4+ Kd7 Qe6+ Kc6 Bc7+ Kxc7 Qxa6 Nxg3 Qa5+ Kb8 Qxd8+ Rxd8 Re5 Ra7 Rf3 Rxd4 Re8+ Kb7 Re7+ Ka6 Re6+ Kb7 Rb6+ Kc7 Rxh6 Rd1+ Kg2 Nf5 Rh7+ Kb8 Rh8+ Kb7 Rc3 Ne3+ Kf3 Rf1+ Ke4 Kc6 Rh6+ Kb7 Rb6+ Kc7 Rxb5 Kc6 Rb6+ Kc7 Rg6 Nd1 Rb3 Nf2+ Kf5 Nxh3 Rxh3 f3 Rh7+ Kb8 Rg8#")
#
result = recordKeeper.result
#                
print(recordKeeper.result)

recordKeeper.result.to_pickle("./ready_to_train.pickle")