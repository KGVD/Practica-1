
"""
Created on Tue May  18 00:06:41 2023

@author: LoboM
"""

import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=100):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None
    
    def train(self, X, y):
        self.weights = np.zeros(X.shape[1])
        self.bias = 0
        
        for epoch in range(self.epochs):
            for i in range(X.shape[0]):
                net_input = np.dot(X[i], self.weights) + self.bias
            
                y_pred = self.activation(net_input)
                
                update = self.learning_rate * (y[i] - y_pred)
                self.weights += update * X[i]
                self.bias += update
    
    def predict(self, X):
        net_input = np.dot(X, self.weights) + self.bias
        y_pred = self.activation(net_input)
        return y_pred
    
    def activation(self, net_input):
        return np.where(net_input >= 0, 1, 0)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

p = Perceptron()
p.train(X, y)

X_new = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_pred = p.predict(X_new)

print(y_pred)