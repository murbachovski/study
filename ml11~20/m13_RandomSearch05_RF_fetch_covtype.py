# 01. iris
# 02. cancer
# 03. dacon_diabets
# 04. wine

import numpy as np
from sklearn.datasets import fetch_covtype
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold,cross_val_score, StratifiedKFold
from sklearn.metrics import accuracy_score
from sklearn.utils import all_estimators
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
import time

# parameters = [
#     {'n_estimators' : [100, 200]},
#     {'max_depth' : [6, 8, 10, 12]},
#     {'min_samples_leaf': [3, 5, 7, 10]},
#     {'min_samples_split' : [2, 3, 5, 10]},
#     {'n_jobs' : [-1, 2, 4]},
# ]

parameters = [
    {'n_estimators': [100, 200], 'max_depth' : [6, 10, 12]}
]

# 1. 데이터
x,y = fetch_covtype(return_X_y=True)

x_train, x_test, y_train, y_test = train_test_split(
    x,y, shuffle=True, random_state=337, test_size=0.2, #stratify=y # stratify=y 사용함으로써 각 라벨값이 골고루 분배된다 
)    

n_splits = 2
kfold = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=337)


#2. MODEL # 대문자 = class
model = RandomizedSearchCV(RandomForestClassifier(), parameters, verbose=1, refit=True, n_jobs=-1, cv=2)

#3. COMPILE
start_time = time.time()
model.fit(x_train, y_train)
end_time = time.time()

print("최적의 매개변수 : ", model.best_estimator_) 

print("최적의 파라미터 : ", model.best_params_)

print("최적의 인덱스 : ", model.best_index_)

print("BEST SCORE : ", model.best_score_)
print("model 스코어 : ", model.score(x_test, y_test))


y_predict = model.predict(x_test)
print('ACC: ', accuracy_score(y_test, y_predict))

y_pred_best = model.best_estimator_.predict(x_test)
print('최적 튠ACC: ', accuracy_score(y_test, y_pred_best))

print('걸린 시간: ', round(end_time - start_time, 2),'초')


# GridSearchCV

# RandomizedSearchCV