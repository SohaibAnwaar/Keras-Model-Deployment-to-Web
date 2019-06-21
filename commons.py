import io
import pickle
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn import ensemble
import os

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
# preprocessing of sequence which I have done with train data
def frequencyVec(seq):
    encoder = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W',
               'Y']
    fv = [0 for x in range(20)]
    i = 0
    for i in range(20):
        fv[i - 1] = seq.count(encoder[i])
    return fv


def get_model():
	model = pickle.load(open("model.sav", 'rb'))
	print("Model Loaded")
	return model
	
