# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.lines as lines
import numpy as np
import wx


class ZoomRectangle(object):
	def __init__(self,figure,axes,canvas):
		self.canvas = canvas
		self.figure = figure
		self.axes = axes
		self.cline = lines.Line2D([],[], color="#00ff00", ls="--")
	
	def connect(self):
		print "connect: ",self.canvas,self.figure,self.axes
		self.btpress = self.canvas.mpl_connect("button_press_event", self.on_press)
		self.btrelease = self.canvas.mpl_connect("button_release_event", self.on_release)
		print self.btpress, self.btrelease
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
		self.canvas.draw()
		
	def on_press(self,event):
		print "Press"
		self.x0 = event.xdata
		self.y0 = event.ydata
		self.motion = self.canvas.mpl_connect("motion_notify_event", self.on_motion)
		
	def on_release(self,event):
		"Release"
		self.canvas.mpl_disconnect(self.motion)
		self.canvas.mpl_disconnect(self.btpress)
		self.canvas.mpl_disconnect(self.btrelease)
		min_x = min([self.x0, self.x])
		max_x = max([self.x0, self.x])
		min_y = min([self.y0, self.y])
		max_y = max([self.y0, self.y])
		self.axes.set_xlim(min_x, max_x)
		self.axes.set_ylim(min_y, max_y)
		self.canvas.draw()



class FigureCanvas(FigureCanvasWxAgg):
	def __init__(self,parent,id,figure,**kwargs):
		FigureCanvasWxAgg.__init__(self,parent=parent, id=id, figure=figure,**kwargs)
		self.figure = figure
		self.axes = self.figure.get_axes()[0]
		
	def disconnect_all(self):
		try:
			self.mpl_disconnect(self.motion)
			self.mpl_disconnect(self.btpress)
			self.mpl_disconnect(self.btrelease)
		except:
			pass
		
	def zoomit(self):
		self.cline = lines.Line2D([],[], color="#ff00ff", ls="--", lw=2.0)
		self.btpress = self.mpl_connect("button_press_event", self.on_press)
		self.btrelease = self.mpl_connect("button_release_event", self.on_release)
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
		self.draw()
		
	def on_press(self,event):
		self.x0 = event.xdata
		self.y0 = event.ydata
		self.motion = self.mpl_connect("motion_notify_event", self.on_motion)
		
	def on_release(self,event):
		self.disconnect_all()
		try:
			self.cline.remove() # Delete box
		except:
			self.stop_event_loop()
		min_x = min([self.x0, self.x])
		max_x = max([self.x0, self.x])
		min_y = min([self.y0, self.y])
		max_y = max([self.y0, self.y])
		self.axes.set_xlim(min_x, max_x)
		self.axes.set_ylim(min_y, max_y)
		self.draw()
	
	

if __name__ == '__main__':
	plt.plot([1,2,3,12,1,3])
	fig = plt.gcf()
	ax = plt.gca()
	zr = ZoomRectangle(fig,ax,fig.canvas)
	zr.connect()
	plt.show()
