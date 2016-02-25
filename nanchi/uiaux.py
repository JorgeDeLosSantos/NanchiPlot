# -*- coding: utf-8 -*-
import wx
import wx.html as html
import webbrowser
import uibase as ui
from _const_ import *

class CustomTB(wx.ToolBar):
	def __init__(self,parent,**kwargs):
		wx.ToolBar.__init__(self,parent=parent,**kwargs)
		tbsize = (32,32)
		self.SetToolBitmapSize(tbsize)
		self.SetBackgroundColour("#ffffff")
		
		# Bitmaps
		import_bmp = wx.Bitmap(PATH_IMPORT_ICON)
		function_bmp = wx.Bitmap(PATH_FUNCTION_ICON)
		bivariable_function_bmp = wx.Bitmap(PATH_BIVARIABLE_FUNCTION_ICON)
		load_image_bmp = wx.Bitmap(PATH_LOAD_IMAGE_ICON)
		
		plot_bmp = wx.Bitmap(PATH_PLOT_ICON)
		#~ polar_bmp = wx.Bitmap(PATH_POLAR_ICON)
		bar_bmp = wx.Bitmap(PATH_BAR_ICON)
		scatter_bmp = wx.Bitmap(PATH_SCATTER_ICON)
		pie_bmp = wx.Bitmap(PATH_PIE_ICON)
		image_bmp = wx.Bitmap(PATH_IMAGE_ICON)
		contour_bmp = wx.Bitmap(PATH_CONTOUR_ICON)
		contourf_bmp = wx.Bitmap(PATH_CONTOURF_ICON)
		
		zoom_box_bmp = wx.Bitmap(PATH_ZOOM_BOX_ICON)
		reset_view_bmp = wx.Bitmap(PATH_RESET_VIEW_ICON)
		
		# Toolbar components
		self.import_tool = self.AddLabelTool(-1, "Importar datos...", 
		import_bmp, shortHelp="Importar datos...")
		
		self.load_image_tool = self.AddLabelTool(-1, "Importar imagen...", 
		load_image_bmp, shortHelp="Importar imagen...")
		
		self.function_tool = self.AddLabelTool(-1, "Generar datos...", 
		function_bmp, shortHelp=u"Generar datos de función...")
		
		self.bivariable_function_tool = self.AddLabelTool(-1, "Generar datos...", 
		bivariable_function_bmp, shortHelp=u"Generar datos de función bivariable...")
		
		self.AddSeparator()
		self.AddSeparator()
		self.AddSeparator()
		self.AddSeparator()
		
		self.plot_tool = self.AddLabelTool(-1, u"Líneas", 
		plot_bmp, shortHelp=u"Líneas")
		
		#~ self.polar_tool = self.AddLabelTool(-1, u"Polar", 
		#~ polar_bmp, shortHelp=u"Polar")
		
		self.bar_tool = self.AddLabelTool(-1, "Barras", 
		bar_bmp, shortHelp=u"Barras")
		
		self.scatter_tool = self.AddLabelTool(-1, "Scatter", 
		scatter_bmp, shortHelp=u"Scatter")
		
		self.pie_tool = self.AddLabelTool(-1, "Pie", 
		pie_bmp, shortHelp=u"Pastel")
		
		self.image_tool = self.AddLabelTool(-1, "Imagen", 
		image_bmp, shortHelp=u"Imagen")
		
		self.contour_tool = self.AddLabelTool(-1, "Contorno", 
		contour_bmp, shortHelp=u"Contorno")
		
		self.contourf_tool = self.AddLabelTool(-1, "Contorno relleno", 
		contourf_bmp, shortHelp=u"Contorno relleno")
		
		self.AddSeparator()
		self.AddSeparator()
		self.AddSeparator()
		self.AddSeparator()
		
		self.zoom_box_tool = self.AddLabelTool(-1, "Zoom Box", 
		zoom_box_bmp, shortHelp=u"Zoom Box")
		
		self.reset_view_tool = self.AddLabelTool(-1, "Reset view", 
		reset_view_bmp, shortHelp=u"Vista inicial")
		

class FunctionDialog(wx.Dialog):
	def __init__(self,parent,**kwargs):
		#_styles = (wx.CLOSE_BOX|wx.CAPTION)
		wx.Dialog.__init__(self,parent=parent,title=DEFAULT_DIALOG_CAPTION,
						  size=(200,150))
		self.LABEL_FONT = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)
		self.initCtrls()
		self.initSizers()
		
		# Output properties
		self.data = ""
		self.out_fun = ""
		self.out_a = ""
		self.out_b = ""
		
		self.Centre(True)
		#self.Show()
		
	def initSizers(self):
		self.mainsz = wx.BoxSizer(wx.VERTICAL)
		self.pfunsz = wx.BoxSizer(wx.HORIZONTAL)
		self.prangesz = wx.BoxSizer(wx.HORIZONTAL)
		self.pbuttonsz = wx.BoxSizer(wx.HORIZONTAL)
		
		self.pfunsz.Add(self._fun, 1, wx.ALIGN_LEFT|wx.ALL, 5)
		self.pfunsz.Add(self.fun, 4, wx.ALIGN_LEFT|wx.ALL, 5)
		self.prangesz.Add(self._a, 1, wx.ALIGN_LEFT|wx.ALL, 5)
		self.prangesz.Add(self.a, 4, wx.ALIGN_LEFT|wx.ALL, 5)
		self.prangesz.Add(self._b, 1, wx.ALIGN_LEFT|wx.ALL, 5)
		self.prangesz.Add(self.b, 4, wx.ALIGN_LEFT|wx.ALL, 5)
		
		self.pbuttonsz.Add(self.okbutton, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
		self.pbuttonsz.Add(self.cancelbutton, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
		
		for panel in [self.pfun, self.prange, self.pbutton]:
			self.mainsz.Add(panel, 1, wx.EXPAND)
		
		self.pfun.SetSizer(self.pfunsz)
		self.prange.SetSizer(self.prangesz)
		self.pbutton.SetSizer(self.pbuttonsz)
		self.SetSizer(self.mainsz)
		
	def initCtrls(self):
		self.pfun = wx.Panel(self, -1)
		self.prange = wx.Panel(self, -1)
		self.pbutton = wx.Panel(self, -1)
		self._fun = wx.StaticText(self.pfun, -1, u"f(x)", size=(-1,25))
		self.fun = wx.TextCtrl(self.pfun, -1, u"x**2", size=(-1,25))
		self._a = wx.StaticText(self.prange, -1, u"a", size=(-1,25))
		self.a = wx.TextCtrl(self.prange, -1, u"0", size=(50,25))
		self._b = wx.StaticText(self.prange, -1, u"b", size=(-1,25))
		self.b = wx.TextCtrl(self.prange, -1, u"10", size=(50,25))
		
		self.okbutton = wx.Button(self.pbutton, wx.ID_OK, u"Aceptar", size=(-1,25))
		self.cancelbutton = wx.Button(self.pbutton, wx.ID_CANCEL, u"Cancelar", size=(-1,25), 
								style=wx.ID_CANCEL)
		
		for ctrl in [self._fun,self._a,self._b]:
			ctrl.SetFont(self.LABEL_FONT)
			
	def GetData(self):
		self.out_fun = self.fun.GetValue()
		self.out_a = self.a.GetValue()
		self.out_b = self.b.GetValue()
		self.data = (self.out_fun, self.out_a, self.out_b)
		return self.data
		

class BivariableFunctionDialog(wx.Dialog):
	def __init__(self,parent,**kwargs):
		#_styles = (wx.CLOSE_BOX|wx.CAPTION)
		wx.Dialog.__init__(self,parent=parent,title=DEFAULT_DIALOG_CAPTION,
						  size=(220,180))
		self.LABEL_FONT = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)
		self.initCtrls()
		self.initSizers()
		
		# Output properties
		self.data = ""
		self.out_fun = ""
		self.out_x = ""
		self.out_y = ""
		
		self.Centre(True)
		#self.Show()
		
	def initSizers(self):
		self.mainsz = wx.BoxSizer(wx.VERTICAL)
		self.pfunsz = wx.BoxSizer(wx.HORIZONTAL)
		self.prangexsz = wx.BoxSizer(wx.HORIZONTAL)
		self.prangeysz = wx.BoxSizer(wx.HORIZONTAL)
		self.pbuttonsz = wx.BoxSizer(wx.HORIZONTAL)
		
		self.pfunsz.Add(self._fun, 1, wx.ALIGN_LEFT|wx.ALL, 5)
		self.pfunsz.Add(self.fun, 4, wx.ALIGN_LEFT|wx.ALL, 5)
		self.prangexsz.Add(self._x1, 1, wx.ALIGN_LEFT|wx.ALL, 5)
		self.prangexsz.Add(self.x1, 4, wx.ALIGN_LEFT|wx.ALL, 5)
		self.prangexsz.Add(self._x2, 1, wx.ALIGN_LEFT|wx.ALL, 5)
		self.prangexsz.Add(self.x2, 4, wx.ALIGN_LEFT|wx.ALL, 5)
		self.prangeysz.Add(self._y1, 1, wx.ALIGN_LEFT|wx.ALL, 5)
		self.prangeysz.Add(self.y1, 4, wx.ALIGN_LEFT|wx.ALL, 5)
		self.prangeysz.Add(self._y2, 1, wx.ALIGN_LEFT|wx.ALL, 5)
		self.prangeysz.Add(self.y2, 4, wx.ALIGN_LEFT|wx.ALL, 5)
		
		self.pbuttonsz.Add(self.okbutton, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
		self.pbuttonsz.Add(self.cancelbutton, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
		
		for panel in [self.pfun, self.prangex, self.prangey, self.pbutton]:
			self.mainsz.Add(panel, 1, wx.EXPAND)
		
		self.pfun.SetSizer(self.pfunsz)
		self.prangex.SetSizer(self.prangexsz)
		self.prangey.SetSizer(self.prangeysz)
		self.pbutton.SetSizer(self.pbuttonsz)
		self.SetSizer(self.mainsz)
		
	def initCtrls(self):
		self.pfun = wx.Panel(self, -1)
		self.prangex = wx.Panel(self, -1)
		self.prangey = wx.Panel(self, -1)
		self.pbutton = wx.Panel(self, -1)
		self._fun = wx.StaticText(self.pfun, -1, u"f(x,y)", size=(-1,25))
		self.fun = wx.TextCtrl(self.pfun, -1, u"(x*y)/(x**2+y**2)", size=(-1,25))
		self._x1 = wx.StaticText(self.prangex, -1, u"x1", size=(-1,25))
		self.x1 = wx.TextCtrl(self.prangex, -1, u"-10", size=(50,25))
		self._x2 = wx.StaticText(self.prangex, -1, u"x2", size=(-1,25))
		self.x2 = wx.TextCtrl(self.prangex, -1, u"10", size=(50,25))
		self._y1 = wx.StaticText(self.prangey, -1, u"y1", size=(-1,25))
		self.y1 = wx.TextCtrl(self.prangey, -1, u"-10", size=(50,25))
		self._y2 = wx.StaticText(self.prangey, -1, u"y2", size=(-1,25))
		self.y2 = wx.TextCtrl(self.prangey, -1, u"10", size=(50,25))
		
		self.okbutton = wx.Button(self.pbutton, wx.ID_OK, u"Aceptar", size=(-1,25))
		self.cancelbutton = wx.Button(self.pbutton, wx.ID_CANCEL, u"Cancelar", size=(-1,25), 
								style=wx.ID_CANCEL)
		
		for ctrl in [self._fun,self._x1, self._x2, self._y1, self._y2]:
			ctrl.SetFont(self.LABEL_FONT)
			
	def GetData(self):
		self.out_fun = self.fun.GetValue()
		self.out_x = [self.x1.GetValue(), self.x2.GetValue()]
		self.out_y = [self.y1.GetValue(), self.y2.GetValue()]
		self.data = (self.out_fun, self.out_x, self.out_y)
		return self.data


class AboutDialog(wx.Frame):
	def __init__(self,parent,*args,**kwargs):
		_styles = wx.CAPTION|wx.CLOSE_BOX
		wx.Frame.__init__(self,parent=parent,title=NANCHI_MAIN_CAPTION,
		size=(350,200), style=_styles)
		self.winhtml = HTMLWindow(self)
		self.winhtml.LoadPage("nanchi/help/about.html")
		self.Centre(True)
		self.Show()


class HTMLWindow(html.HtmlWindow):
	def __init__(self,parent,**kwargs):
		html.HtmlWindow.__init__(self,parent=parent,**kwargs)
	
	def OnLinkClicked(self, link):
		webbrowser.open(link.GetHref())


class StatusBar(wx.StatusBar):
	def __init__(self,*args,**kwargs):
		wx.StatusBar.__init__(self,*args,**kwargs)
		

class BusyInfo(object):
    def __init__(self, msg, parent=None, bgColour="#f0f0f0", fgColour="#8080ff"):
        self.frame = _InfoFrame(parent, msg, bgColour, fgColour)
        self.frame.Show()
        self.frame.Refresh()
        self.frame.Update()
        
    def __del__(self):
        self.Close()
        
    def Close(self):
        """
        Hide and close the busy info box
        """
        if self.frame:
            self.frame.Hide()
            self.frame.Close()
            self.frame = None
    
    # Magic methods for using this class as a Context Manager 
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Close()
        return False


class _InfoFrame(wx.Frame):
    def __init__(self, parent, msg, bgColour=None, fgColour=None):
        wx.Frame.__init__(self, parent, style=wx.BORDER_SIMPLE|wx.FRAME_TOOL_WINDOW|wx.STAY_ON_TOP)

        bgColour = bgColour if bgColour is not None else wx.Colour(253, 255, 225)
        fgColour = fgColour if fgColour is not None else wx.BLACK

        panel = wx.Panel(self)
        text = wx.StaticText(panel, -1, msg)
        
        for win in [panel, text]:
            win.SetCursor(wx.HOURGLASS_CURSOR)
            win.SetBackgroundColour(bgColour)
            win.SetForegroundColour(fgColour)
            
        size = text.GetBestSize()
        self.SetClientSize((size.width + 60, size.height + 40))
        panel.SetSize(self.GetClientSize())
        text.Center()
        self.Center()


class LogCtrl(wx.TextCtrl):
	def __init__(self,parent,**kwargs):
		wx.TextCtrl.__init__(self, parent=parent, id=wx.ID_ANY,
							 style=wx.TE_MULTILINE, **kwargs)
		self.font = wx.Font(10, wx.MODERN, wx.NORMAL, wx.BOLD)
		self.SetFont(self.font)
		self.SetForegroundColour("#5555dd")
		
	def write(self,string):
		self.cvalue = self.GetValue()
		_nvalue = "%s\n>> %s"%(self.cvalue, string)
		self.SetValue(_nvalue)
	

class ImportDialog(wx.Dialog):
	def __init__(self,parent,**kwargs):
		wx.Dialog.__init__(self,parent=parent,title=DEFAULT_DIALOG_CAPTION,
						  size=(800,600))
		self.LABEL_FONT = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)
		self.initCtrls()
		self.initSizers()		
		
		self.Centre(True)

	def initSizers(self):
		self.mainsz = wx.BoxSizer(wx.VERTICAL)
		self.panelsz = wx.BoxSizer(wx.HORIZONTAL)
		self.plogsz = wx.BoxSizer(wx.HORIZONTAL)
		self.pctrlssz = wx.BoxSizer(wx.VERTICAL)
		self.pbuttonsz = wx.BoxSizer(wx.HORIZONTAL)
		
		#
		self.pctrlssz.Add(self._dlm, 0, wx.EXPAND|wx.ALL, 5)
		self.pctrlssz.Add(self.dlm, 0, wx.EXPAND|wx.ALL, 5)
		self.pctrlssz.Add(self._skiprows, 0, wx.EXPAND|wx.ALL, 5)
		self.pctrlssz.Add(self.skiprows, 0, wx.EXPAND|wx.ALL, 5)
		
		self.panelsz.Add(self.fctrl, 1, wx.EXPAND|wx.ALL, 5)
		self.panelsz.Add(self.pctrls, 1, wx.EXPAND|wx.ALL, 5)
		self.panelsz.Add(self.grid, 2, wx.EXPAND|wx.ALL, 5)
		
		self.plogsz.Add(self.log, 1, wx.EXPAND|wx.ALL, 5)
		
		self.pbuttonsz.Add(self.okbutton, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
		self.pbuttonsz.Add(self.cancelbutton, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
		
		self.mainsz.Add(self.panel, 5, wx.EXPAND|wx.ALL, 5)
		self.mainsz.Add(self.plog, 1, wx.EXPAND|wx.ALL, 5)
		self.mainsz.Add(self.pbutton, 1, wx.EXPAND|wx.ALL, 5)
		
		self.pctrls.SetSizer(self.pctrlssz)
		self.panel.SetSizer(self.panelsz)
		self.plog.SetSizer(self.plogsz)
		self.pbutton.SetSizer(self.pbuttonsz)
		self.SetSizer(self.mainsz)
		
	def initCtrls(self):
		self.panel = wx.Panel(self, -1)
		self.plog = wx.Panel(self, -1)
		self.pbutton = wx.Panel(self, -1)
		self.pctrls = wx.Panel(self.panel, -1)
		
		self.fctrl = wx.FileCtrl(self.panel, -1)
		self.grid = ui.DataGrid(self.panel, (10,10))
		
		# Controles conf.
		self._dlm = wx.StaticText(self.pctrls, -1, u"Delimitador", size=(-1,25))
		self.dlm = wx.TextCtrl(self.pctrls, -1, u",", size=(-1,25))
		self._skiprows = wx.StaticText(self.pctrls, -1, u"Leer a partir de fila:", size=(-1,25))
		self.skiprows = wx.SpinCtrl(self.pctrls, -1, min=1, max=100)
		
		# Log 
		self.log = LogCtrl(self.plog)
		
		# Botones
		self.okbutton = wx.Button(self.pbutton, wx.ID_OK, u"Aceptar", size=(-1,25))
		self.cancelbutton = wx.Button(self.pbutton, wx.ID_CANCEL, u"Cancelar", size=(-1,25), 
								style=wx.ID_CANCEL)
		
		self.Bind(wx.EVT_SPINCTRL, self.OnSpin)
		
	def OnSpin(self,event):
		self.log.write("Valor actual: %s"%(self.skiprows.GetValue(),))
			
	def GetData(self):
		self.data = self.fctrl.GetPath()
		return self.data


def test_toolbar():
	app = wx.App()
	fr = wx.Frame(None, -1, "Hi !!!", size=(800,600))
	sz = wx.BoxSizer(wx.VERTICAL)
	tb = CustomTB(fr)
	sz.Add(tb, 0, wx.EXPAND)
	fr.SetSizer(sz)
	tb.Realize()
	fr.Show()
	app.MainLoop()	
	
	
def test_about():
	app=wx.App()
	fr = AboutDialog(None)
	app.MainLoop()


def test_function():
	app = wx.App()
	fr = BivariableFunctionDialog(None)
	if fr.ShowModal() == wx.ID_OK:
		print fr.GetData()
	fr.Destroy()
	app.MainLoop()


def test_import():
	app = wx.App()
	fr = ImportDialog(None)
	if fr.ShowModal() == wx.ID_OK:
		print fr.GetData()
	fr.Destroy()
	app.MainLoop()

if __name__=='__main__':
	test_import()
