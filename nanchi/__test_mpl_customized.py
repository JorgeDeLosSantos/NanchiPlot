# -*- coding: utf-8 -*-
import wx
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,500)
y1 = np.sin(x)
y2 = x**2*np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y1, picker=5)	
ax.plot(x, y2, picker=5)
ax.text(1, 1, "Hola Mundo", picker=True)

def OnMotion(event):
	global p0, line, xdata0, ydata0
	cx = event.xdata
	cy = event.ydata
	deltax = cx - p0[0]
	deltay = cy - p0[1]
	if isinstance(line,plt.Text):
		line.set_position((cx,cy))
	else:
		line.set_xdata(xdata0 + deltax)
		line.set_ydata(ydata0 + deltay)
	fig.canvas.draw()
	
def OnRelease(event):
	global mot, rel
	fig.canvas.mpl_disconnect(mot)
	fig.canvas.mpl_disconnect(rel)
	ax.relim()
	ax.autoscale_view(True,True,True)
	fig.canvas.draw()

def OnPick(event):
	global mot, rel, p0, line, xdata0, ydata0
	line = event.artist	
	p0 = (event.mouseevent.xdata, event.mouseevent.ydata)
	if isinstance(line,plt.Text):
		pass
	else:
		xdata0 = line.get_xdata()
		ydata0 = line.get_ydata()
	mot = fig.canvas.mpl_connect("motion_notify_event", OnMotion)
	rel = fig.canvas.mpl_connect("button_release_event", OnRelease)

pick = fig.canvas.mpl_connect("pick_event", OnPick)
plt.show()
