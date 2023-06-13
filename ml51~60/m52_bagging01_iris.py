import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. DATA
x, y = load_iris(return_X_y=True)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=1253, train_size=0.8, shuffle=True, stratify=y
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# 2. MODEL
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.tree import DecisionTreeClassifier


model = BaggingClassifier(DecisionTreeClassifier(),
                          n_estimators=10,
                          n_jobs=-1,
                          random_state=1253,
                        #   bootstrap=True
                          )

# 3. COMPILE
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(model)
print('model_score:', model.score(x_test, y_test))
print('ACC:', accuracy_score(y_test, y_pred))

# BaggingClassifier(estimator=DecisionTreeClassifier(), n_jobs=-1,
#                   random_state=1253)
# model_score: 0.9666666666666667
# ACC: 0.9666666666666667