import json
from commons import get_model,frequencyVec
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy
from PIL import Image
import cv2
from scipy import misc
import os




model = get_model()

def get_Prediction(processed_text):
    processed_text=frequencyVec(processed_text)
    processed_text=np.asarray(processed_text)
    processed_text=processed_text.reshape(1,20)
    outputs=model.predict(processed_text)
    print(outputs)
    return  outputs