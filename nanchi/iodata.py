# -*- coding: utf-8 -*-
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def read_txt(filename,delimiter=None,dtype="float",**kwargs):
    dlms = [","," ","\t"]
    X = None
    if (delimiter is None):
        for dlm in dlms:
            try:
                X = np.loadtxt(filename,delimiter=dlm,dtype=dtype,**kwargs)
                return X
            except: pass
    else:
        try:
            X = np.loadtxt(filename,delimiter=delimiter,dtype=dtype,**kwargs)
        except: pass
    return X
    
def read_csv(filename,dtype="float"):
    X = np.loadtxt(filename, delimiter=",", dtype=dtype)
    return X

def write_txt(filename, array, delimiter=",", fmt="%0.4f"):
    np.savetxt(filename, array, delimiter=delimiter, fmt=fmt )

def write_csv():
    pass
        
def imread(filename):
    """
    For read image file, return a MxN array.
    """
    X = plt.imread(filename)
    if len(X.shape) == 3: # RGB
        X = rgb2gray(X)
    elif len(X.shape) == 2: # Gray
        # Nothing to do here, or ?
        pass
    else:
        # Not support for multidimensional arrays
        raise ValueError
    return X
    
    
def imsave(filename,array):
    plt.imsave(filename, array, cmap=plt.cm.gray)

    
def rgb2gray(rgb):
    """
    Convert rgb array image to grayscale
    """
    return np.dot(rgb[:,:,:3], [0.2125, 0.7154, 0.0721])

def gray2rgb(gray):
    pass

if __name__=='__main__':
    #X = read_txt("data/data_with_comments.txt",skiprows=3)
    X = read_csv("data/contour_data.txt")
    print X
