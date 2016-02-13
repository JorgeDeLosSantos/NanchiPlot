# -*- coding: utf-8 -*-
import wx
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np

x = np.linspace(0,10,500)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y, picker=5)

class ZoomRectangle(object):
	def __init__(self,figure,axes):
		self.figure = figure
		self.axes = axes
		self.cline = lines.Line2D([],[], color="#aacc00", ls="--")
	
	def connect(self):
		self.btpress = self.figure.canvas.mpl_connect("button_press_event", self.on_press)
		self.btrelease = self.figure.canvas.mpl_connect("button_release_event", self.on_release)
		self.axes.add_line(self.cline)
		
	def on_motion(self,event):
		self.cline.set_xdata([])
		self.cline.set_ydata([])
		# ---
		self.x = event.xdata
		self.y = event.ydata
		# ---
		xdata = [self.x0, self.x0, self.x, self.x, self.x0]
		ydata = [self.y0, self.y, self.y, self.y0, self.y0] 
		# ---
		self.cline.set_xdata(xdata)
		self.cline.set_ydata(ydata)
		# ---
		self.figure.canvas.draw()
		
	def on_press(self,event):
		self.x0 = event.xdata
		self.y0 = event.ydata
		self.motion = self.figure.canvas.mpl_connect("motion_notify_event", self.on_motion)
		
	def on_release(self,event):
		self.figure.canvas.mpl_disconnect(self.motion)
		min_x = min([self.x0, self.x])
		max_x = max([self.x0, self.x])
		min_y = min([self.y0, self.y])
		max_y = max([self.y0, self.y])
		self.axes.set_xlim(min_x, max_x)
		self.axes.set_ylim(min_y, max_y)
		self.figure.canvas.draw()


zr = ZoomRectangle(fig,ax)
zr.connect()
plt.show()
