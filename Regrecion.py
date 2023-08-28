# -*- coding: utf-8 -*-
"""
Created on Sat May 7 00:13:12 2023

@author: LoboM
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

x1 = np.array([1, 2, 3, 4, 5])
x2 = np.array([2, 4, 6, 8, 10])
y = np.array([5, 10, 15, 20, 25])

df = pd.DataFrame({'x1': x1, 'x2': x2, 'y': y})

modelo = LinearRegression().fit(df[['x1', 'x2']], df['y'])

print('Coeficientes: ', modelo.coef_)

nuevos_valores = pd.DataFrame({'x1': [6], 'x2': [12]})
prediccion = modelo.predict(nuevos_valores)
print('Predicción: ', prediccion)