# -*- coding: utf-8 -*-
import wx
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,500)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y, picker=5)
is_draw = True

def onclick(event):
	app = wx.App()
	dlg = wx.MessageDialog(None, "Desea borrar",
	'A Message Box', wx.YES_NO | wx.ICON_QUESTION)
	if (dlg.ShowModal() == wx.ID_YES):
		event.artist.remove()
	else:
		pass
	dlg.Destroy()
	app.MainLoop()
	plt.draw()
	
def OnDrawData(event):
	line = event.artist
	xx = line.get_xdata()
	yy = line.get_ydata()
	array = zip(xx,yy)
	cx = event.mouseevent.xdata
	cy = event.mouseevent.ydata
	idx = nearest_point((cx,cy),array)
	ax.plot(xx[idx],yy[idx],'ro')
	plt.draw()
	
def nearest_point(point,array):
	xp = point[0]
	yp = point[1]
	d = []
	for x,y in array:
		d.append(np.sqrt((xp-x)**2 + (yp-y)**2))
	return np.argmin(d)


def OnPutText(event):
	cx = event.mouseevent.xdata
	cy = event.mouseevent.ydata
	app = wx.App()
	dialog = wx.TextEntryDialog(None,
	"What kind of text would you like to enter?",
	"Text Entry", "Default Value", style=wx.OK|wx.CANCEL)
	if dialog.ShowModal() == wx.ID_OK:
		plt.text(cx, cy, unicode(dialog.GetValue()))
	dialog.Destroy()
	app.MainLoop()
	plt.draw()


def OnZoom(event):
	global mot
	mot = fig.canvas.mpl_connect("motion_notify_event", OnMotion)
	

def OnMotion(event):pass
	
	
def OnRelease(event):
	global mot
	fig.canvas.mpl_disconnect(mot)


bp = fig.canvas.mpl_connect("button_press_event", OnZoom)
br = fig.canvas.mpl_connect("button_release_event", OnRelease)

plt.show()
