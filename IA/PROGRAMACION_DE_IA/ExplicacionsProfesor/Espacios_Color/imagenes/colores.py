
import numpy as np 
from matplotlib import pyplot as plt
import cv2 as cv 

image = cv.imread('que-ver-en-a-coruna-hercules.jpg')
cv.imshow('img',image)
cv.waitKey(0)