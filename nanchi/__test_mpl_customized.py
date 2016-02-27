# -*- coding: utf-8 -*-
import wx
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np

X = np.random.random((10,10))

plt.pcolor(X)

plt.show()
