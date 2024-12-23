import numpy as np
from matplotlib import pyplot as plt
import cv2
import easyocr as ocr
import re

testImage = cv2.imread("Images/1.jpg")


reader = ocr.Reader(['sw','en']) # this needs to run only once to load the model into memory
result = reader.readtext(testImage, detail=0)

def clean_text(textInImage):
    wordList = []
    for line in textInImage:
        words = re.split(r'[^a-zA-Z0-9ÅÄÖåäö]', line)
        for word in words:
            if(word != ''):
                wordList.append(word)
    return wordList

def detect_ingredients():

    return

print(clean_text(result))

