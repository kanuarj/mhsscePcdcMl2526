import numpy as np
from sklearn import linear_model

class LinearRegression:
    def __init__(self):
        self.b_0 = 0
        self.b_1 = 0

    def fit (self, X, y):
        X_mean = np.mean (X)
        y_mean = np.mean (y)
        ssxy, ssx = 0, 0
        for _ in range (len (X)):
            ssxy += (X[_] - X_mean)*(y[_] - y_mean)
            ssx += (X[_] - X_mean)**2

        self.b_1 = ssxy / ssx
        self.b_0 = y_mean - (self.b_1 * X_mean)
        return self.b_0, self.b_1
    
    def predict (self, X):
        y_hat = self.b_0 + (self.b_1 * X)
        return y_hat
    
if __name__ == '__main__':
    X = np.array ([[173, 182, 165, 154, 170]]).reshape(5, 1)
    y = np.array ([68, 79, 65, 57, 64])
    model = LinearRegression ()
    b0, b1 = model.fit (X, y)
    print (f'The b0 is {b0} and b1 is {b1}')
    y_pred = model.predict ([176])
    print (f'The raw implementation : {y_pred}')

    libModel = linear_model.LinearRegression ()
    libModel.fit (X, y)
    lib_pred = libModel.predict ([[176]])
    print (f'The library implementation : {lib_pred}')