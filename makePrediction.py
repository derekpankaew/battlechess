import pandas as pd #importing and managing datasets
import numpy as np #mathematical functions
import matplotlib as plt #for plotting things on graphs
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
import keras
from keras.models import model_from_json
import time
from datetime import datetime

def makePrediction(gameState):
    # Setup the data and indicators

    dataset = pd.DataFrame(gameState)
    
    # Load neural network model
    
    # load json and create model
    
    model_name = "trained_models/model"
    
    json_file = open(model_name + '.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(model_name + ".h5")
#    print("Loaded model from disk")
    
    # Load model
    
    loaded_model.compile(optimizer = "adam", loss = "binary_crossentropy", metrics = ["accuracy"])
    
    # Run prediction using the neural network
    
    y_pred = loaded_model.predict(X_test) # returns the probability of each entry
    #y_pred = (y_pred > 0.5) # returns true if > 0.5, else returns false
    
    last = len(y_pred) - 1
    result = y_pred[last]
    
#    print(result)
    return(result)
