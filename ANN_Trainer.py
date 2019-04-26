import pandas as pd #importing and managing datasets
import numpy as np #mathematical functions
import matplotlib as plt #for plotting things on graphsfrom sklearn.preprocessing import Imputer #Lets you fill in missing data with mean
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
import keras
from keras.models import Sequential
from keras.layers import Dense

testSize = 0.15
numOfEpochs = 50
batchSize = 25

# Importing the Dataset
# Set your working directory first, by going to file explorer

dataset = pd.read_pickle("./ready_to_train.pickle")
X_test = dataset
saveAsName = "./trained_models/ready_to_deploy_2"

# Next, we separate the independent variables and the dependent variables
# In other words, the inputs and outputs

# Start selection all the way on the left, end on the right minus one

numberOfRows = dataset.shape[1] - 1

X = dataset.iloc[:, 0:numberOfRows].values #independent variables
Y = dataset.iloc[:,numberOfRows].values #dependent variables

# Then, split data into training data and testing data

 # X train is the training set for X, etc.

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = testSize, random_state = 0)

# Initializing the neural network

classifier = Sequential()

numberOfNodes = numberOfRows + 1

if numberOfNodes % 2 != 0:
    numberOfNodes = numberOfNodes + 1 # Make sure number of nodes is even

classifier.add(Dense(units = numberOfNodes, kernel_initializer = "uniform", activation = 'relu', input_dim = numberOfRows))

# Add a hidden layer. Same as before, except without input_dim

classifier.add(Dense(units = 100, kernel_initializer = "uniform", activation = 'relu')) #1

classifier.add(Dense(units = 1, kernel_initializer = "uniform", activation = 'sigmoid'))

classifier.compile(optimizer = "adam", loss = "binary_crossentropy", metrics = ["accuracy"])

# This actually trains the model! Epochs should display in the terminal

classifier.fit(X_train,Y_train,epochs=numOfEpochs,batch_size = batchSize)

# Save the model when finished

# serialize model to JSON
model_json = classifier.to_json()
with open(saveAsName + ".json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
classifier.save_weights(saveAsName + ".h5")
print("Saved model to disk")

# Predict against the test set

y_pred = classifier.predict(X_test) # returns the probability of each entry
y_pred = (y_pred > 0.5) # returns true if > 0.5, else returns false

# Uses a matrix to determine if the results matched
# If the two columns match, that means they're accurate
# Can use to determine false positive vs false negative

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_pred)
correct = cm[1][1]
incorrect = cm[0,1]
print(cm)
winRate = "{0:.0%}".format(correct / (correct + incorrect))
print ("Predicted %s trades correctly, and %s trades incorrectly, for a win rate of %s" %(correct, incorrect, winRate))
