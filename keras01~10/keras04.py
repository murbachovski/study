import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense  

# 1. Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 5, 4])

# 2. Model
model = Sequential()
model.add(Dense(3, input_dim=1)) # first hidden layout
model.add(Dense(4, input_dim=3))
model.add(Dense(5))
model.add(Dense(3))
model.add(Dense(1))

# 3. Compile, 훈련
model.compile(loss= 'mse', optimizer = 'adam')
model.fit(x, y, epochs=400)

# 4. evaluate
loss = model.evaluate(x, y)
print("loss:", loss)

result = model.predict([6])
print("[6]의 예측값:", result)