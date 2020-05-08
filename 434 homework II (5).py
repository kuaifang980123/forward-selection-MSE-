import numpy as np
import pandas as pd
from pandas import concat
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error



boston = datasets.load_boston()
X = pd.DataFrame(boston.data, columns=boston.feature_names)
y = boston.target
y = y.reshape(506, 1)


def m_selection(X, y, m):
    included = []
    current_mse = float("inf")
    model_best = linear_model.LinearRegression()
    for i in range(m):
        excluded = list(set(X.columns) - set(included))
        for new_column in excluded:
            model = linear_model.LinearRegression()
            model.fit(X[included + [new_column]], y)
            mse = mean_squared_error(y, model.predict(X[included + [new_column]]))
            if mse < current_mse:
                current_mse = mse
                col_min = new_column
                model_best = model
        included.append(col_min)
    return model_best, included

def forward_selection(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    m = 13
    MSE = []
    for i in range(1,14):
        n,p=m_selection(X_train,y_train,i)
        y_predict = n.predict(X_test[p])
        MSE.append(mean_squared_error(y_test, y_predict))
    MSE = np.array(MSE)
    best_MSE = MSE.argmin()+1
    best_index = m_selection(X, y, best_MSE)[1]
    return best_MSE, best_index

forward_selection(X,y)































