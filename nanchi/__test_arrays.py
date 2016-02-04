# -*- coding: utf-8 -*-
import numpy as np
		
def test_01():
	X = np.linspace(0,10)
	Y = np.cos(X)
	M = np.transpose([X,Y])
	np.savetxt("data/test_01.txt",M,fmt="%0.4f")

def test_02():
	X = np.linspace(0,10)
	Y = np.cos(X)
	Z = np.sin(X)
	W = 0.2*X**2 - 2*X
	M = np.transpose([X,Y,Z,W])
	np.savetxt("data/test_02.txt",M,fmt="%0.4f")
	
		
if __name__=='__main__':
	test_01()
	test_02()
