import asyncio
import time
import chess
import chess.engine
import requests
import traceback
#from collections import defaultdict
#import numpy as np
#import pandas as pd
#from numpy import array
##from numpy import argmax
#from sklearn.preprocessing import LabelEncoder
#from sklearn.preprocessing import OneHotEncoder
#from joblib import dump, load # For saving OneHotEncoder
# define example



board = chess.Board()

input = "Nf3 d5 c3 g6 d4 f6 h3 Bg7 e3 e5 c4 e4 Nfd2 f5 c5 c6 f3 b6 g3 bxc5 dxc5 Na6 Nb3 Nc7 Nd4 Ne7 b4 Ba6 Bxa6 Nxa6 a3 Rb8 Qe2 Bxd4 exd4 Nc7 Bg5 h6 Bf6 Rf8 Be5 Rb5 Nc3 Rb7 O-O Nb5 Nxb5 cxb5 Bd6 a6 fxe4 dxe4 Qe3 g5 Qb3 f4 Rae1 Nf5 Rxe4+ Kd7 Qe6+ Kc6 Bc7+ Kxc7 Qxa6 Nxg3 Qa5+ Kb8 Qxd8+ Rxd8 Re5 Ra7 Rf3 Rxd4 Re8+ Kb7 Re7+ Ka6 Re6+ Kb7 Rb6+ Kc7 Rxh6 Rd1+ Kg2 Nf5 Rh7+ Kb8 Rh8+ Kb7 Rc3 Ne3+ Kf3 Rf1+ Ke4 Kc6 Rh6+ Kb7 Rb6+ Kc7 Rxb5 Kc6 Rb6+ Kc7 Rg6 Nd1 Rb3 Nf2+ Kf5 Nxh3 Rxh3 f3 Rh7+ Kb8 Rg8#"

input = input.split(" ")

print(input)

for move in input:

    print("Making move %s" %(move))

    board.push_san(move)

    print("Board position is now:")

    print(board)

    print("The FEN is now:")

    print(board.fen())
    
    print("Legal Moves:")
    
    print(board.legal_moves)

#newData = []
#
#for item in data:
#    
#    valueToAppend = pieceToNumber(item)
#    
#    newData.append(valueToAppend)
#    
#print("NewData is:" )
#print(newData)

#
## define example
#data = ["0", "r", "1", "k", "0", "0", "0", "0", "R"]
#values = array(data)
#print(values)
#
## binary encode
#onehot_encoder = OneHotEncoder(sparse=False)
#arr = array(newData)
#arr_reshaped = arr.reshape(len(arr), 1)
#onehot_encoded = onehot_encoder.fit_transform(arr_reshaped)
#print("Binary Encoded:")
#print(onehot_encoded)
#
#dump(onehot_encoder, './OHE.joblib') 