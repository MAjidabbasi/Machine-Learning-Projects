# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as mp
import pandas as pd
 dataset = pd.read_csv(Dara.csv)
 X = dataset.iloc[:, :-1].values
 Y = dataset.iloc[:, 3].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing=""NaN", strategy="mean",axis = 0) 
imputer.fit(X[:, 1:2])
