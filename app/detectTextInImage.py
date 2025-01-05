import numpy as np
from matplotlib import pyplot as plt
import cv2
import easyocr as ocr
import re

def clean_text(textInImage):
    wordList = []
    for line in textInImage:
        words = re.split(r'[^a-zA-Z0-9ÅÄÖåäö]', line)
        for word in words:
            if(word != ''):
                wordList.append(word)
    return wordList

def readImage(imageLocation):

    reader = ocr.Reader(['sw','en']) # this needs to run only once to load the model into memory
    image = cv2.imread(imageLocation)
    result = reader.readtext(image, detail=0)
    wordList = clean_text(result)
    return wordList
