# -*- coding: utf-8 -*-
import wx
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np

K = 525
n = 0.2
e = np.linspace(0, 0.3, 100)
s = K*e**n;
X = np.array([e,s])
np.savetxt("data/steel_1008.txt", X.T, fmt="%0.4f", delimiter=",")
#~ plt.plot(e,s,'m')
#~ plt.xlabel(r"$\varepsilon$ (mm/mm)")
#~ plt.ylabel(r"$\sigma$ (MPa)")
#~ plt.title(r"Acero SAE 1008: $\sigma = K \varepsilon^n$")
#~ plt.show()
