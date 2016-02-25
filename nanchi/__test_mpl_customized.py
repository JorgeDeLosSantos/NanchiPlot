# -*- coding: utf-8 -*-
import wx
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np


def OnPick(event):
	event.artist.set_linewidth(2)
	event.artist.set_ls("--")
	fig.canvas.draw()

X = np.random.random((10,5))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(X, picker=5)

pick = fig.canvas.mpl_connect("pick_event", OnPick)

plt.show()
