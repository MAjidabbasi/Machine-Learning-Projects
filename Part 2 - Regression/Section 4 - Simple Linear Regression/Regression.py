# -*- coding: utf-8 -*-
"""
Created on Sun May 26 04:53:02 2019

@author: Majid-PC
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('Salary_Data.csv')
X = data.iloc[: , :-1].values
Y = data.iloc[: , 1].values

#Splitting the data
from sklearn.cross_validation import train_test_split
data