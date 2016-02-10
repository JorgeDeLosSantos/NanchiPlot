# -*- coding: utf-8 -*-
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def read_txt(filename,delimiter=None,dtype="float"):
	if delimiter is None:
		delimiter = ","
		try:
			X = np.loadtxt(filename,delimiter=delimiter,dtype=dtype)
		except:
			delimiter = " "
			try:
				X = np.loadtxt(filename,delimiter=delimiter,dtype=dtype)
			except:
				X = None
	return X
	
def read_csv():
	pass

def write_txt():
	pass

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
	
	
def rgb2gray(rgb):
	"""
	Convert rgb array image to grayscale
	"""
	return np.dot(rgb[:,:,:3], [0.2125, 0.7154, 0.0721])

def gray2rgb(gray):
	pass

if __name__=='__main__':
	pass
