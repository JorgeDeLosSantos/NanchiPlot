# -*- coding: utf-8 -*-
import numpy as np
from skimage import io, color, filters

path_img = r"C:/Users/User/Pictures/ittg_logo.png"

def sobel(X):
    sbl = filters.sobel(X)
    return sbl

def prewitt(X):
    pw = filters.prewitt(X)
    return pw

def roberts(X):
    rb = filters.roberts(X)
    return rb

def rgb2gray(X):
    gray = color.rgb2gray(X)
    return gray

def binarize(X):
    th = 0.5
    bX = X > th
    return bX.astype('float')

if __name__ == '__main__':
    img = io.imread(path_img)
    img = rgb2gray(img)
    #img = sobel(img)
    bi = binarize(img)
    io.imshow(bi)
    io.show()
