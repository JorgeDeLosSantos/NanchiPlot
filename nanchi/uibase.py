# -*- coding: utf-8 -*-
import wx
import wx.aui as aui
import wx.grid as grid
import wx.lib.scrolledpanel as scrolled
import os
import numpy as np
import matplotlib
#matplotlib.use('WXAgg')

import matplotlib.pyplot as plt
#from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from uimpl import FigureCanvas
from matplotlib.figure import Figure

import pickle 

import setplot
import uimpl
from util import isempty, rgb2hex
from _const_ import *  # String & Constants values

class NanchiNoteBook(aui.AuiNotebook):
    def __init__(self, parent):
		_styles = aui.AUI_NB_TOP | aui.AUI_NB_TAB_SPLIT | aui.AUI_NB_TAB_MOVE
		aui.AuiNotebook.__init__(self, parent=parent, style=_styles)
		
		self.graphs = GraphPanel(self)
		self.data = DataPanel(self)
		#self.setup = SetupPanel(self)

		self.AddPage(self.graphs, u"Gráficas")
		self.AddPage(self.data, u"Datos")
		#self.AddPage(self.setup, u"Configurar")

		self.axes = self.graphs.axes
		self.figure = self.graphs.figure
		self.canvas = self.graphs.canvas

		self.Bind(aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self.OnPageChanged)

    def OnPageChanged(self, event):
		pass
		#gp = pickle.load(open("graph_properties.dat","rb"))
		#self.axes.set_xlabel(gp["xlabel"])
		#self.axes.set_ylabel(gp["ylabel"])
		#self.canvas.draw() # Draw canvas 
        


class SetupPanel(wx.Panel):
	def __init__(self,parent,*args,**kwargs):
		wx.Panel.__init__(self,parent,*args,**kwargs)
		# Fonts
		self.COMBO_BOX_FONT = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)
		
		self.initCtrls()
		self.initSizers()
		
	def initCtrls(self):
		self.plabels = wx.Panel(self, -1, style=wx.BORDER_SIMPLE)
		self.pstyles = wx.Panel(self, -1, style=wx.BORDER_SIMPLE)
		self.pbuttons = wx.Panel(self, -1, style=wx.BORDER_SIMPLE)
		
		# Labels controls
		self._xlabel = wx.StaticText(self.plabels, -1, "Etiqueta X")
		self._ylabel = wx.StaticText(self.plabels, -1, "Etiqueta Y")
		self.xlabel = wx.TextCtrl(self.plabels, -1)
		self.ylabel = wx.TextCtrl(self.plabels, -1)
		
		# Styles controls
		self._line_style = wx.StaticText(self.pstyles, -1, u"Estilo de línea")
		self.line_style = wx.ComboBox(self.pstyles, -1, choices=LINE_STYLES, 
									  size=(80,-1), value="'-'")
		self.line_style.SetFont(self.COMBO_BOX_FONT)
		
		self._line_color = wx.StaticText(self.pstyles, -1, u"Color de línea")
		self.line_color = wx.ColourPickerCtrl(self.pstyles, -1, col=LINE_COLOR)
		
		self._line_width = wx.StaticText(self.pstyles, -1, u"Grosor de línea")
		self.line_width = wx.SpinCtrl(self.pstyles, -1, min=1, max=20, 
									  initial=1, size=(60,-1))
		
		self._grid_color = wx.StaticText(self.pstyles, -1, u"Color de rejilla")
		self.grid_color = wx.ColourPickerCtrl(self.pstyles, -1, col=GRID_COLOR)
		
		# Buttons for save or discard changes
		self.save_changes = wx.Button(self.pbuttons, -1, "Aplicar cambios")
		self.default_values = wx.Button(self.pbuttons, -1, "Valores predeterminados")
		
		self.Bind(wx.EVT_BUTTON, self.OnSaveChanges, self.save_changes)
		
	def initSizers(self):
		self.mainsz = wx.BoxSizer(wx.VERTICAL)
		self.szplabels = wx.GridBagSizer(10,10)
		self.szpstyles = wx.GridBagSizer(10,10)
		self.szpbuttons = wx.BoxSizer(wx.HORIZONTAL)
		
		self.szplabels.Add(self._xlabel, (0,0), flag=wx.ALL, border=5)
		self.szplabels.Add(self.xlabel, (0,1), flag=wx.ALL, border=5)
		self.szplabels.Add(self._ylabel, (0,2), flag=wx.ALL, border=5)
		self.szplabels.Add(self.ylabel, (0,3), flag=wx.ALL, border=5)
		self.szplabels.AddGrowableRow(0)
		
		self.szpstyles.Add(self._line_style, (0,0), flag=wx.ALL, border=5)
		self.szpstyles.Add(self.line_style, (0,1), flag=wx.ALL, border=5)
		self.szpstyles.Add(self._line_color, (0,2), flag=wx.ALL, border=5)
		self.szpstyles.Add(self.line_color, (0,3), flag=wx.ALL, border=5)
		self.szpstyles.Add(self._line_width, (0,4), flag=wx.ALL, border=5)
		self.szpstyles.Add(self.line_width, (0,5), flag=wx.ALL, border=5)
		self.szpstyles.Add(self._grid_color, (1,0), flag=wx.ALL, border=5)
		self.szpstyles.Add(self.grid_color, (1,1), flag=wx.ALL, border=5)
		
		self.szpbuttons.Add(self.save_changes, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		self.szpbuttons.Add(self.default_values, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		
		self.mainsz.Add(self.plabels, 3, wx.EXPAND|wx.ALL, 5)
		self.mainsz.Add(self.pstyles, 3, wx.EXPAND|wx.ALL, 5)
		self.mainsz.Add(self.pbuttons, 1, wx.EXPAND|wx.ALL, 5)
		
		self.plabels.SetSizer(self.szplabels)
		self.pstyles.SetSizer(self.szpstyles)
		self.pbuttons.SetSizer(self.szpbuttons)
		self.SetSizer(self.mainsz)

	def OnSaveChanges(self,event):
		pass
		#xlabel = self.xlabel.GetValue()
		#ylabel = self.ylabel.GetValue()
		#graph_properties = {"xlabel":xlabel,"ylabel":ylabel}
		#pickle.dump(graph_properties, open('graph_properties.dat',"wb"))


class GraphPanel(wx.Panel):
	def __init__(self,parent,*args,**kwargs):
		wx.Panel.__init__(self,parent,-1)
		# Sizer
		self.mainsz = wx.BoxSizer(wx.VERTICAL)
		
		# Init canvas Figure & Axes
		self.initCanvas()
		
		# Color properties
		self.SetBackgroundColour(PANEL_BG_COLOR)
		
		# Configurar sizeR
		self.SetSizer(self.mainsz)
		
	def initCanvas(self):
		# Crear figure & axes
		self.figure = Figure()
		self.axes = self.figure.add_subplot(111)
		self.canvas = FigureCanvas(self, -1, self.figure)
		
		self.EVT_ON_RIGHT = self.canvas.mpl_connect('button_press_event', self.OnRightClick)
		# Graph properties
		setplot.set_default_params(self.axes,self.figure)
		# FigureCanvas
		self.mainsz.Add(self.canvas, 1, wx.EXPAND|wx.ALL, 2)
	
	def OnRightClick(self,event):
		if event.button == 3:
			self.InitPopUpMenu()
		else:
			pass
			

	def InitPopUpMenu(self):
		pum = wx.Menu()
		
		gs = wx.Menu()
		_gs_cont = wx.MenuItem(gs, -1, u"-")
		gs.AppendItem(_gs_cont)
		_gs_dashed = wx.MenuItem(gs, -1, u"--")
		gs.AppendItem(_gs_dashed)
		_gs_dotted = wx.MenuItem(gs, -1, u"dotted")
		gs.AppendItem(_gs_dotted)
		pum.AppendMenu(-1, "Estilo de rejilla", gs)
		gridcolor = wx.MenuItem(pum, -1, u"Color de rejilla")
		pum.AppendItem(gridcolor)
		
		pum.AppendSeparator()
		axbackg = wx.MenuItem(pum, -1, u"Color de fondo")
		pum.AppendItem(axbackg)
		aspax = wx.Menu()
		_aspax_auto = wx.MenuItem(aspax, -1, u"auto")
		aspax.AppendItem(_aspax_auto)		
		_aspax_equal = wx.MenuItem(aspax, -1, u"equal")
		aspax.AppendItem(_aspax_equal)
		pum.AppendMenu(-1, "Aspecto del axes", aspax)
		
		pum.AppendSeparator()
		xlabel = wx.MenuItem(pum, -1, u"Etiqueta X")
		pum.AppendItem(xlabel)
		ylabel = wx.MenuItem(pum, -1, u"Etiqueta Y")
		pum.AppendItem(ylabel)
		title = wx.MenuItem(pum, -1, u"Insertar título")
		pum.AppendItem(title)
		intext = wx.MenuItem(pum, -1, u"Insertar texto/anotación")
		pum.AppendItem(intext)
		
		pum.AppendSeparator()
		zoom_box = wx.MenuItem(pum, -1, u"Zoom Box")
		pum.AppendItem(zoom_box)
		
		# Binds
		self.Bind(wx.EVT_MENU, self.OnText, intext)
		self.Bind(wx.EVT_MENU, self.OnBackground, axbackg)
		self.Bind(wx.EVT_MENU, self.OnGridColor, gridcolor)
		self.Bind(wx.EVT_MENU, self.OnXLabel, xlabel)
		self.Bind(wx.EVT_MENU, self.OnYLabel, ylabel)
		self.Bind(wx.EVT_MENU, self.OnTitle, title)
		self.Bind(wx.EVT_MENU, self.OnZoom, zoom_box)
		self.Bind(wx.EVT_MENU, self.OnGridStyle, _gs_cont)
		self.Bind(wx.EVT_MENU, self.OnGridStyle, _gs_dashed)	
		self.Bind(wx.EVT_MENU, self.OnGridStyle, _gs_dotted)
		self.Bind(wx.EVT_MENU, self.OnAxesAspect, _aspax_equal)
		self.Bind(wx.EVT_MENU, self.OnAxesAspect, _aspax_auto)
		
		# Show
		self.PopupMenu(pum)
		pum.Destroy()
			
			
	def OnText(self,event):
		self.TEXT_EVT = self.canvas.mpl_connect("button_press_event", self.set_text)
		
	def set_text(self,event):
		cx = event.xdata
		cy = event.ydata
		dialog = wx.TextEntryDialog(self,
		"Inserte el texto",
		NANCHI_MAIN_CAPTION, "", style=wx.OK|wx.CANCEL)
		if dialog.ShowModal() == wx.ID_OK:
			self.axes.text(cx, cy, unicode(dialog.GetValue()))
			self.canvas.draw()
		dialog.Destroy()
		self.canvas.mpl_disconnect(self.TEXT_EVT)
		
	def OnBackground(self,event):
		dlg = wx.ColourDialog(self)
		if dlg.ShowModal() == wx.ID_OK:
			color = dlg.GetColourData().Colour
			r,g,b = color.Red(),color.Green(),color.Blue()
			self.axes.set_axis_bgcolor(rgb2hex(r,g,b))
		dlg.Destroy()
		self.canvas.draw()
		
	def OnAxesAspect(self,event):
		aspect = event.GetEventObject().GetLabel(event.GetId())
		self.axes.set_aspect(aspect)
		self.canvas.draw()
		
		
	def OnGridColor(self,event):
		dlg = wx.ColourDialog(self)
		if dlg.ShowModal() == wx.ID_OK:
			color = dlg.GetColourData().Colour
			r,g,b = color.Red(),color.Green(),color.Blue()
			self.axes.grid(color=rgb2hex(r,g,b))
		dlg.Destroy()
		self.canvas.draw()
		
	def OnGridStyle(self,event):
		_gs = event.GetEventObject().GetLabel(event.GetId())
		self.axes.grid(ls=_gs)
		self.canvas.draw()
		
	def OnXLabel(self,event):
		dialog = wx.TextEntryDialog(self,
		"Inserte la etiqueta en X",
		NANCHI_MAIN_CAPTION, "", style=wx.OK|wx.CANCEL)
		if dialog.ShowModal() == wx.ID_OK:
			self.axes.set_xlabel(dialog.GetValue())
			self.canvas.draw()
		dialog.Destroy()
		
	def OnYLabel(self,event):
		dialog = wx.TextEntryDialog(self,
		"Inserte la etiqueta en Y",
		NANCHI_MAIN_CAPTION, "", style=wx.OK|wx.CANCEL)
		if dialog.ShowModal() == wx.ID_OK:
			self.axes.set_ylabel(dialog.GetValue())
			self.canvas.draw()
		dialog.Destroy()
		
	def OnTitle(self,event):
		dialog = wx.TextEntryDialog(self,
		u"Inserte el título",
		NANCHI_MAIN_CAPTION, "", style=wx.OK|wx.CANCEL)
		if dialog.ShowModal() == wx.ID_OK:
			self.axes.set_title(dialog.GetValue())
			self.canvas.draw()
		dialog.Destroy()
		
	def OnZoom(self,event):
		self.canvas.zoomit()
		


class GraphWindow(wx.Frame):
	def __init__(self,parent,title,*args,**kwargs):
		wx.Frame.__init__(self,parent=parent,title=title,*args,**kwargs)
		self.SetBackgroundColour(FRAME_BG_COLOR)
		self.Centre(True)
		
		
class DataPanel(scrolled.ScrolledPanel):
	def __init__(self,parent,*args,**kwargs):
		scrolled.ScrolledPanel.__init__(self,parent,-1,size=(100,-1),
		style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER)
				
		self.initCtrls()
		self.initSizers()
		self.initEvents()
		self.SetupScrolling()
		# Color properties
		self.SetBackgroundColour(PANEL_BG_COLOR)
		
	def initCtrls(self):
		self.grid_data = DataGrid(self,(10,2))
		
	def initSizers(self):
		# Create sizers
		self.mainsz = wx.BoxSizer(wx.VERTICAL)
		# Add to sizers
		self.mainsz.Add(self.grid_data, 5, wx.EXPAND|wx.ALL, 2)

		# Set Sizers
		self.SetSizer(self.mainsz)
		
	def initEvents(self):
		pass
		

class DataGrid(grid.Grid):
	def __init__(self,parent,gridsize,**kwargs):
		grid.Grid.__init__(self,parent=parent,id=-1,**kwargs)
		rows = int(gridsize[0])
		cols = int(gridsize[1])
		self.CreateGrid(rows,cols)
		self.SetRowLabelSize(20)
		self.Bind(grid.EVT_GRID_CELL_CHANGE, self.OnCellEdit)
		self.Bind(grid.EVT_GRID_CELL_RIGHT_CLICK, self.OnRightClick)
		
	def UpdateGridSize(self,rows,cols):
		self.ClearGrid()
		ccols = self.GetNumberCols()
		crows = self.GetNumberRows()
		
		if rows > crows:
			self.AppendRows(rows-crows)
		elif rows < crows:
			self.DeleteRows(0,crows-rows)
			
		if cols > ccols:
			self.AppendCols(cols-ccols)
		elif cols < ccols:
			self.DeleteCols(0,ccols-cols)
			
	def SetArrayData(self,data):
		"""
		Data must be a numpy array
		"""
		r,c = data.shape # For numpy array
		self.UpdateGridSize(r,c)
		for i in range(r):
			for j in range(c):
				val = str(data[i][j])
				self.SetCellValue(i,j,val)
		
	def GetArrayData(self):
		nrows = self.GetNumberRows()
		ncols = self.GetNumberCols()
		X = np.zeros((nrows,ncols))
		for i in range(nrows):
			for j in range(ncols):
				cval = self.GetCellValue(i,j)
				if not isempty(cval):
					X[i][j] = float(cval)
				else:
					X[i][j] = np.nan
		return X
		
	def GetSelectedCols(self):
		scols = []
		top_left = self.GetSelectionBlockTopLeft()
		bottom_right = self.GetSelectionBlockBottomRight()
		if not isempty(bottom_right) and not isempty(top_left):
			max_col = bottom_right[0][1]
			min_col = top_left[0][1]
			scols = range(min_col,max_col+1)
		return scols
		
	def GetSelectedRows(self):
		srows = []
		top_left = self.GetSelectionBlockTopLeft()
		bottom_right = self.GetSelectionBlockBottomRight()
		if not isempty(bottom_right) and not isempty(top_left):
			max_row = bottom_right[0][0]
			min_row = top_left[0][0]
			srows = range(min_row,max_row+1)
		return srows
		
	def OnCellEdit(self,event):
		"""
		"""
		row,col = (event.GetRow(),event.GetCol())
		cval = self.GetCellValue(row,col)
		if cval.startswith("="):
			try:
				cval = str(eval(cval[1:]))
				self.SetCellValue(row,col,cval)
			except:
				pass
		try:
			cval = float(cval)
		except ValueError:
			cval = np.nan
		self.SetCellValue(row,col,str(cval))
		
			
	def OnRightClick(self,event):
		pum = wx.Menu()
		delrows = wx.MenuItem(pum, -1, "Eliminar filas")
		pum.AppendItem(delrows)
		delcols = wx.MenuItem(pum, -1, "Eliminar columnas")
		pum.AppendItem(delcols)
		pum.AppendSeparator()
		addrow = wx.MenuItem(pum, -1, "Agregar fila...")
		pum.AppendItem(addrow)
		addcol = wx.MenuItem(pum, -1, "Agregar columna...")
		pum.AppendItem(addcol)
		pum.AppendSeparator()
		editcollabel = wx.MenuItem(pum, -1, "Editar etiqueta de columna")
		pum.AppendItem(editcollabel)
		pum.AppendSeparator()
		randomfill = wx.MenuItem(pum, -1, "Rellenar columna aleatoriamente")
		pum.AppendItem(randomfill)
		
		
		# Binds
		pum.Bind(wx.EVT_MENU, self.del_rows, delrows)
		pum.Bind(wx.EVT_MENU, self.del_cols, delcols)
		pum.Bind(wx.EVT_MENU, self.add_row, addrow)
		pum.Bind(wx.EVT_MENU, self.add_col, addcol)
		pum.Bind(wx.EVT_MENU, self.edit_collabel, editcollabel)
		pum.Bind(wx.EVT_MENU, self.random_fill, randomfill)
		# Show 
		self.PopupMenu(pum)
		pum.Destroy()

	def del_rows(self,event):
		rows = self.GetSelectedRows()
		self.DeleteRows(rows[0],len(rows))
		
	def del_cols(self,event):
		cols = self.GetSelectedCols()
		self.DeleteCols(cols[0],len(cols))
		
	def add_row(self,event):
		self.AppendRows(1)
		
	def add_col(self,event):
		self.AppendCols(1)
		
	def edit_collabel(self,event):
		ccols = self.GetSelectedCols()
		dlg = wx.TextEntryDialog(None, "Inserte etiqueta...",
		DEFAULT_DIALOG_CAPTION)
		if dlg.ShowModal() == wx.ID_OK:
			label = dlg.GetValue()
		for col in ccols:
			self.SetColLabelValue(col,label)
	
	def random_fill(self,event):
		col = self.GetSelectedCols()[0]
		nrows = self.GetNumberRows()
		data = np.random.random((nrows,1))
		for i in range(nrows):
			val = str(data[i][0])
			self.SetCellValue(i,col,val)

		
if __name__=='__main__':
	app = wx.App()
	fr = GraphWindow(None,"Hi",size=(600,400))
	sz = wx.BoxSizer(wx.VERTICAL)
	p = NanchiNoteBook(fr)
	#p = DataPanel(fr)
	sz.Add(p, 1, wx.EXPAND|wx.ALL, 5)
	fr.SetSizer(sz)
	fr.Show()
	app.MainLoop()
