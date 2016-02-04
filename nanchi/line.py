# -*- coding: utf-8 -*-
import wx
import os
import sympy
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import sin,cos,tan,log,sqrt,exp,linspace

class Line(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent,-1)
		#self.pcanvas = wx.Panel(self,-1)
		self.pctrls = wx.Panel(self,-1)
		
		# Sizers
		self.szmain = wx.BoxSizer(wx.VERTICAL)
		self.szctrls = wx.BoxSizer(wx.HORIZONTAL)
		
		self.initCanvas()
		self.initCtrls()
		
		self.SetSizer(self.szmain)
		self.pctrls.SetSizer(self.szctrls)
		
		self.szmain.Add(self.canvas, 15, wx.EXPAND|wx.ALL, 5)
		self.szmain.Add(self.pctrls, 1, wx.EXPAND|wx.ALL, 5)
		
		self.intervalo = [0.0,10.0]
		self.xlabel = "x"
		self.ylabel = "y"
		
	def initCanvas(self):
		# Creamos Figure
		self.figure = Figure()
		self.axes = self.figure.add_subplot(111)
		
		# FigureCanvas
		self.canvas = FigureCanvas(self, -1, self.figure)
		
	def initCtrls(self):
		colores = "rojo verde azul negro amarillo".split()
		estilos = "- -- -.".split()
		self.label = wx.StaticText(self.pctrls, -1, " f(x) ")
		self.fun = wx.TextCtrl(self.pctrls, -1)
		self.bot = wx.Button(self.pctrls, -1, "Graficar")
		self.color = wx.ComboBox(self.pctrls, -1, choices = colores, value='Color')
		self.estilo = wx.ComboBox(self.pctrls, -1, choices = estilos, value='Estilo')
		
		# Fuente
		mod_font = self.label.GetFont()
		mod_font.SetPointSize(12)
		mod_font.SetWeight(wx.BOLD)
		self.label.SetFont(mod_font)
		self.fun.SetFont(mod_font)
		self.fun.SetForegroundColour((100,100,255))
		
		self.Bind(wx.EVT_BUTTON, self.graficar, self.bot)
		
		self.szctrls.Add(self.label, 1, wx.EXPAND|wx.ALL, 5)
		self.szctrls.Add(self.fun, 7, wx.EXPAND|wx.ALL, 5)
		self.szctrls.Add(self.color, 2, wx.EXPAND|wx.ALL, 5)
		self.szctrls.Add(self.estilo, 2, wx.EXPAND|wx.ALL, 5)
		self.szctrls.Add(self.bot, 2, wx.EXPAND|wx.ALL, 5)
		
	
	def graficar(self,event):
		# Equivalencia de colores
		list_color = {'rojo': (1,0,0),
		'verde': (0,1,0),
		'azul': (0,0,1),
		'negro': (0,0,0),
		'amarillo': (1,1,0)}
		f = self.fun.GetValue() # f(x)
		estilo = self.estilo.GetValue() 
		color = self.color.GetValue()
		if estilo == 'Estilo':
			estilo = '-' # Linea continua por default
		if color == 'Color':
			color = 'negro' # Color negro default
		color = list_color.get(color)
		x = linspace(self.intervalo[0], self.intervalo[1])
		try:
			y = eval(f)
		except:
			wx.MessageBox(u'Inserte una funcion f(x)','msg')
			return # go out
		
		self.axes.cla() # Limpiar axes 
		hLine = self.axes.plot(x, y, lw = 2, linestyle=estilo, color=color) # Gráfica
		from numpy import sin,cos,tan,log,sqrt,exp,linspace
		x = sympy.Symbol('x')
		f = sympy.latex(eval(f))
		self.axes.set_title('$f(x) = ' + f + "$") # Configurar título de la gráfica
		self.axes.set_xlabel(self.xlabel)
		self.axes.set_ylabel(self.ylabel)
		self.axes.grid(True) # Coloca rejilla
		self.canvas.draw() # Redibuja el elementos "canvas"
		
if __name__=='__main__':
	app = wx.App()
	fr = wx.Frame(None, -1, "Hi !!!", size=(800,600))
	Line(fr)
	fr.Maximize(True)
	fr.Show()
	app.MainLoop()
	
