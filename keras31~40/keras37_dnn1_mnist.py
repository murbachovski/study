from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.utils import to_categorical

# [실습] 맹그러
# 목표는 cnn성능보다 좋게 맹그러!

#1. DATA
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#reshape
x_train = x_train.reshape(60000, 28*28)
x_test = x_test.reshape(10000, 28*28)

#2. MODEL
model = Sequential()
model.add(Dense(32, input_shape=(784,))) # == model.add(Dense(64, input_shape=(28*28,)))
model.add(Dropout(0.7))
model.add(Dense(16, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(8, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(4, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(1, activation='softmax'))


#3. COMPILE
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
es = EarlyStopping(
    monitor='val_loss',
    mode='auto',
    patience=30,
    restore_best_weights=True
)
model.fit(x_train, y_train, epochs=200, batch_size=1000, validation_split=0.025)

#4. EVALUATE
results = model.evaluate(x_test, y_test)
print('loss: ', results[0], 'acc: ', results[1])