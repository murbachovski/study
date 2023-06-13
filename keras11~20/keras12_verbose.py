from sklearn.datasets import load_boston

#1. DATA
dataset = load_boston()
x = dataset.data
y = dataset.target

# print(x)
# print(y)

print(dataset)
print(dataset.feature_names)

print(dataset.DESCR)

print(x.shape, y.shape) # (506, 13) (506, ) # Vactor = 1

#2. MODEL
import numpy as np
import tensorflow as tf     
from tensorflow.keras.models import Sequential   
from tensorflow.keras.layers import Dense    

model = Sequential()
model.add(Dense(516, input_dim = 13))
model.add(Dense(256))
model.add(Dense(128))
model.add(Dense(64))
model.add(Dense(32))
model.add(Dense(16))
model.add(Dense(1))


#3. COMPILE
from sklearn.model_selection import train_test_split


x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    train_size= 0.7,
    random_state=190
)
model.compile(loss = 'mse', optimizer = 'adam')
model.fit(x_train, y_train, epochs = 10, batch_size = 2, verbose="auto")

# #4. EVALUATE, PREDICT
# loss = model.evaluate(x_test, y_test)
# print("loss:", loss)

y_predict = model.predict(x_test)
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_predict) # GOOD, Y = wX + b, 보조지표
print("R2_SCORE: ", r2)

