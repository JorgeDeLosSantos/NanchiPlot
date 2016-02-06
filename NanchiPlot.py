# -*- coding: utf-8 -*-
# 
# Author: Jorge De Los Santos
# Version: 0.1.0

import wx
import os
import numpy as np
import matplotlib.cm as cm
import nanchi.iodata as io
import nanchi.uibase as ui
import nanchi.uiaux as aux
from nanchi._const_ import *


class NanchiPlot(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__(self,parent,title=NANCHI_MAIN_CAPTION,size=(800,600))
		self.initMenu()
		self.initCtrls()
		self.initToolBar()
		self.initSizers()
		self.initEvents()
		
		# Icon
		self.icon = wx.Icon("nanchi/img/nanchi_logo.png")
		self.SetIcon(self.icon)
		
		self.Centre(True)
		self.Show()
		
	def initMenu(self):
		m_archivo = wx.Menu()
		guardar = m_archivo.Append(-1, "Guardar")
		importar = m_archivo.Append(-1, "Importar datos...")
		salir = m_archivo.Append(-1, "Salir")
		
		m_ayuda = wx.Menu()
		ayuda = m_ayuda.Append(-1, "Ayuda")
		acerca_de = m_ayuda.Append(-1, "Acerca de...")
		
		menu_bar = wx.MenuBar()
		menu_bar.Append(m_archivo, "Archivo")
		menu_bar.Append(m_ayuda, "Ayuda")
		self.SetMenuBar(menu_bar)
		
		self.Bind(wx.EVT_MENU, self.OnAbout, acerca_de)
		
	def initSizers(self):
		self.mainsz = wx.BoxSizer(wx.VERTICAL)
		self.panelsz = wx.BoxSizer(wx.HORIZONTAL)
		self.mainsz.Add(self.toolbar, 0, wx.EXPAND)
		self.panelsz.Add(self.data_panel, 1, wx.EXPAND|wx.ALL, 2)
		self.panelsz.Add(self.graph_panel, 4, wx.EXPAND|wx.ALL, 2)
		self.mainsz.Add(self.mainpanel, 1, wx.EXPAND)
		self.mainpanel.SetSizer(self.panelsz)
		self.SetSizer(self.mainsz)
		
	def initCtrls(self):
		self.mainpanel = wx.Panel(self,-1)
		self.data_panel = ui.DataPanel(self.mainpanel)
		self.graph_panel = ui.GraphNoteBook(self.mainpanel)
		
	def initToolBar(self):
		self.toolbar = aux.CustomTB(self)
		self.toolbar.Realize()
		
	def initEvents(self):
		self.Bind(wx.EVT_TOOL, self.OnImport, self.toolbar.import_tool)
		self.Bind(wx.EVT_TOOL, self.OnLoadImage, self.toolbar.load_image_tool)
		self.Bind(wx.EVT_TOOL, self.OnFunction, self.toolbar.function_tool)
		self.Bind(wx.EVT_TOOL, self.OnPlot, self.toolbar.plot_tool)
		self.Bind(wx.EVT_TOOL, self.OnBar, self.toolbar.bar_tool)
		self.Bind(wx.EVT_TOOL, self.OnScatter, self.toolbar.scatter_tool)
		self.Bind(wx.EVT_TOOL, self.OnPie, self.toolbar.pie_tool)
		self.Bind(wx.EVT_TOOL, self.OnImage, self.toolbar.image_tool)
		
	def OnMenu(self,event):
		pass
		
	def OnImport(self,event):
		path = ""
		wildcard = "*.txt"
		dlg = wx.FileDialog(self, message="Seleccione un archivo",
		defaultDir=os.getcwd(), wildcard=wildcard, style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath()
			data = io.read_txt(path)
			self.data_panel.grid_data.SetArrayData(data)
		
			
	def OnLoadImage(self,event):
		path = ""
		wildcard = "*.png"
		dlg = wx.FileDialog(self, message="Seleccione una imagen",
		defaultDir=os.getcwd(), wildcard=wildcard, style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath()
			data = io.imread(path)
			self.data_panel.grid_data.SetArrayData(data)
			
	def OnFunction(self,event):
		x = np.linspace(0,10)
		dialog = wx.TextEntryDialog(None,"f(x)",
		DEFAULT_DIALOG_CAPTION, "x", style=wx.OK|wx.CANCEL)
		if dialog.ShowModal() == wx.ID_OK:
			fx = dialog.GetValue()
			fx = eval(fx)
			self.data_panel.grid_data.SetArrayData(np.array([x,fx]).transpose())
			self.data_panel.grid_data.SetColLabelValue(0,"x")
			self.data_panel.grid_data.SetColLabelValue(1,"f(x)")
		dialog.Destroy()
		
		
	def OnPlot(self,event):
		self.graph_panel.axes.cla()
		X = self.data_panel.grid_data.GetArrayData()
		rows,cols = X.shape
		if cols == 2: # Common case
			self.graph_panel.axes.plot(X[:,0],X[:,1])
		elif cols == 1:
			self.graph_panel.axes.plot(X[:,0])
		elif cols > 2:
			for col in range(cols):
				clabel = self.data_panel.grid_data.GetColLabelValue(col)
				self.graph_panel.axes.plot(X[:,col],label=clabel)
			self.graph_panel.axes.legend()
		self.graph_panel.axes.relim()
		self.graph_panel.canvas.draw()
		
	def OnBar(self,event):
		X = self.data_panel.grid_data.GetArrayData()
		rows,cols = X.shape
		if cols == 1: # Common case
			x = range(len(X[:,0]))
			self.graph_panel.axes.bar(x,X[:,0])
		self.graph_panel.canvas.draw()
		
	def OnScatter(self,event):
		X = self.data_panel.grid_data.GetArrayData()
		rows,cols = X.shape
		if cols == 2: # Common case
			self.graph_panel.axes.plot(X[:,0],X[:,1],"bo")
		elif cols == 1:
			self.graph_panel.axes.plot(X[:,0],"bo")
		self.graph_panel.canvas.draw()
		
	def OnPie(self,event):
		self.graph_panel.axes.cla()
		X = self.data_panel.grid_data.GetArrayData()
		rows,cols = X.shape
		if cols == 1:
			self.graph_panel.axes.pie(X[:,0])
		else:
			pass
		self.graph_panel.canvas.draw()
		
	def OnImage(self,event):
		self.graph_panel.axes.cla()
		X = self.data_panel.grid_data.GetArrayData()
		rows,cols = X.shape
		self.graph_panel.axes.imshow(X, cmap=cm.gray)
		self.graph_panel.canvas.draw()
		
	def OnAbout(self,event):
		aux.AboutDialog(None)

if __name__=='__main__':
	app = wx.App()
	frame = NanchiPlot(None)
	app.MainLoop()
