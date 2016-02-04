# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def read_txt(filename,delimiter=None,dtype="float"):
	X = np.loadtxt(filename,delimiter=delimiter,dtype=dtype)
	return X
	
def read_csv():
	pass

def write_txt():
	pass

def write_csv():
	pass
		
def imread(filename):
	X = plt.imread(filename)
	if len(X.shape) == 3: # RGB
		X = rgb2gray(X)
	elif len(X.shape) == 2: # Gray
		pass
	else:
		raise ValueError
	return X
	
	
def rgb2gray(rgb):
    return np.dot(rgb[:,:,:3], [0.299, 0.587, 0.114])

		
if __name__=='__main__':
	pass
	
