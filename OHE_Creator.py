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
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from joblib import dump, load # For saving OneHotEncoder

# Encode individual pieces into numbers
# Black is lowercase, white is uppercase

possibleResults = [0,1,2,3,4,5,6,7,8,9,10,11,12]

# binary encode
onehot_encoder = OneHotEncoder(sparse=False)
arr = array(possibleResults)
arr_reshaped = arr.reshape(len(arr), 1)
onehot_encoded = onehot_encoder.fit_transform(arr_reshaped)
print("Binary Encoded:")
print(onehot_encoded)



dump(onehot_encoder, './OHE.joblib') 