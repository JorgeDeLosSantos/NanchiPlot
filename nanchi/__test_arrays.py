# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = y = np.linspace(0,5)
X,Y = np.meshgrid(x,y)
Z = np.cos(X) + np.sin(Y)

np.savetxt("data/contour_data.txt",Z,fmt="%0.4f",delimiter=",")
