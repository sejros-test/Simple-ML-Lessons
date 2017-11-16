# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:13:31 2017

@author: mvkoroteev
"""

import scipy as sp
import pandas
import matplotlib.pyplot as plt



dj = pandas.read_csv("data/D&J-IND_101001_171001.txt")
gasp = pandas.read_csv("data/GAZP_101001_171001.txt")

print(dj.shape, gasp.shape)

dj = dj[:gasp.shape[0]]

x = gasp['<CLOSE>']
y = dj['<CLOSE>']

res = pandas.merge(dj, gasp, on='<DATE>', suffixes=['_DJ', '_GASP'])
x = res['<CLOSE>_DJ']
y = res['<CLOSE>_GASP']

x = (x - min(x)) / (max(x) - min(x))
y = (y - min(y)) / (max(y) - min(y))

plt.scatter(x, y)


class hypothesis(object):
    def __init__(self):
        self.theta = sp.array([0, 0])
    def apply(self, X):
        return self.theta[0] + self.theta[1] * X
    def error(self, X, Y):
        return sum((self.apply(X) - Y)**2) / (2 * len(Y))
    def gradient_descent(self, x, y):
        i = 0
        m = len(x)
        steps = []
        errors = []
        while(i < 150):
            y_ = hyp.apply(x)
            dJ0 = sum(y_ - y) / m
            dJ1 = sum((y_ - y)*x) / m
        #    print(dJ0, dJ1)
            
            alpha = 0.3
            theta0 = self.theta[0] - alpha * dJ0
            theta1 = self.theta[1] - alpha * dJ1
            self.theta = sp.array([theta0, theta1])
        #    print(hyp.theta)
            
            J = hyp.error(x, y)
        #    print(J)
            
            steps.append(i)
            errors.append(J)
            
            i += 1


hyp = hypothesis()

y_ = hyp.apply(x)
plt.plot(x, y_, color="red")

J = hyp.error(x, y)
print(J)

hyp.gradient_descent(x, y)

y_ = hyp.apply(x)
plt.plot(x, y_, color="green")
plt.show()

print(errors[-1])

plt.plot(steps, errors)
plt.show()